""" (c) Shae Erisson 2013 get Google Voice SMS messages from your gmail account via imap4
released under the GPLv3 license"""
import sqlite3 as lite

import imaplib
import email

# this is for pynotify
import pygtk
pygtk.require('2.0')
import pynotify
import sys

gmailusername = 'shae.erisson@gmail.com'
gmailpassword = 'password'

def gnotify(key,value):
    if not pynotify.init("GNotify"):
        print "Needs GNotify, FAIL"
        sys.exit(1)

    n = pynotify.Notification(key, value)

    if not n.show():
        print "Failed to send notification"

createtable = "CREATE TABLE SMS(Id INTEGER PRIMARY KEY, messageid varchar(255), Subject varchar(255),Body text"

# assume db has been setup correctly
def createtyrnidb():
    # We get these keys from Python's email lib when it reads a message:
    """msg.keys ['Delivered-To', 'Received', 'Return-Path', 'Received-SPF', 
    'Authentication-Results', 'Received', 'DKIM-Signature', 'MIME-Version', 
    'Received', 'References', 'Message-ID', 'Date', 'Subject', 'From', 'To', 
    'Content-Type']
    "First Last (SMS)" <12566610043.12565551212.7x9KSZ6JSG@txt.voice.google.com>
    SMS from First Last [(256) 555-1212]"""
    con = lite.connect('tyrni.db')
    with con:
        cur = con.cursor()
        cur.execute(createtable)

def getsms():
    totalsms = 0
    errorsms = 0
    con = lite.connect('tyrni.db')
    cur = con.cursor()
    # pull out all message-id values from the local db
    midrows = cur.execute('select messageid from sms;').fetchall()
    mids = map(lambda x:x[0], midrows)
    # print 'mids are', mids
    imap = imaplib.IMAP4_SSL('imap.gmail.com')
    imap.login(gmailusername, gmailpassword)
    imap.select()
    # Google Voice SMS email will have Subject starting with 'SMS'
    typ, data = imap.search(None, 'SUBJECT', 'SMS')
    for num in data[0].split():
        totalsms += 1
        typ, data = imap.fetch(num,'(RFC822)')
        msg = email.message_from_string(data[0][1])
        # ignore message-id values we've already seen
        this_mid = msg['Message-ID']
        # print 'checking', this_mid
        if (msg['Message-ID'] not in mids):
            # print 'inserting', this_mid, msg['Subject']
            try:
                cur.execute("INSERT INTO SMS(messageid, subject, body)  VALUES(?, ?, ?);",
                            (msg['Message-ID'], msg['Subject'], msg.get_payload()))
                gnotify(msg['Subject'], msg.get_payload())
            except lite.InterfaceError, err:
                errorsms += 1
                print err,"good luck with that"
        # else: print "we've already got", this_mid
    con.commit()
    print 'ok, latest messages loaded into the database'
    print totalsms, ' total messages found and ',
    print errorsms, 'messages had errors when inserting to the db.'
    # Is this the right order?
    imap.close()
    imap.logout()


def vartest():
    con = lite.connect('tyrni.db')
    cur = con.cursor()
    midrows = cur.execute('select messageid from sms;').fetchall()
    mids = map(lambda x:x[0], midrows)
    print 'mids are', mids
    print "is 'test' in mids?"
    if 'test' in mids:
        print 'we found it!'
    else:
        print "You wish!"

if __name__ == '__main__':
    getsms()
    #vartest()
