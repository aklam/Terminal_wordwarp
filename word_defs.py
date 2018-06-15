from bs4 import BeautifulSoup

defs = open("wb1913_a.html",encoding='iso-8859-15')
soup = BeautifulSoup(defs,"lxml") 
word_defs = soup.body.find_all("p")

for wd in word_defs:
	print(wd.b.string)
	print(wd.contents[3][2:])
#print(soup.find_all("P"))