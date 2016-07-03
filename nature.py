# Nature journal

from bs4 import BeautifulSoup
import urllib2

# url = "http://www.nature.com/nature/current_issue.html"

url = "http://www.nature.com/nature/journal/v534/n7606/index.html" 
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, "lxml")

# print soup.find_all("a")

# for tag in soup.find_all("a"):
#	print(tag.string)

# for tag in soup.find_all("article"):
#	print tag.a.string

# test
# print soup.prettify()[80000:90000]

for tag in soup.find_all("section"):
    if tag.find("span"):
	if tag.span.string in {"Articles", "Letters"}:
	     for t2 in tag.find_all("article"):
	            print t2.a.text
		    
# invalid_tags = ['b', 'i', 'u', 'sub']
		    # for t3 in invalid_tags: 
			# for match in t2.findAll(t3):
			#	match.replaceWithChildren()
		    # print t2.a
		    # print t2
	            # print t2.a.string



