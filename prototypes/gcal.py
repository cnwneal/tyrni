import lxml
import urllib2
from lxml import etree

# don't keep the user's private calendar url in this script
calurl = "shae.cal"

# # create a request with the private calendar url
# req = urllib2.Request(open(calurl).read())
# # get a response from the created request
# resp = urllib2.urlopen(req)
# # read the text from the http server
# calxml = resp.read()

tree = etree.parse(open(calurl.read()) # throw the url into lxml, get back an ElementTree
