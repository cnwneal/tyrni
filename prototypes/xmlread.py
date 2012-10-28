from lxml import etree

tree = etree.parse("basic")
# now check the content tags, rip out the When: line
