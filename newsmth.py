# smth bbs

from bs4 import BeautifulSoup
import urllib2
import re

# url = "http://www.nature.com/nature/current_issue.html"
# url = "http://www.nature.com/nature/journal/v534/n7606/index.html"
url = "http://www.newsmth.net/bbsdoc.php?board=Career_Campus"

content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, "lxml")

print len(soup.prettify())
print soup.prettify()[0:1000]

for tag in soup.find_all("script"):
 	print(tag.string)

tag = soup.find_all("script")
words = tag[5].string.split(";")
for word in words:
	info = word.split(",")
	if len(info) > 5 and (info[3] != u"'d '") : 
		print info[5]
		print "http://www.newsmth.net/bbscon.php?bid=943&id=" + info[1]
