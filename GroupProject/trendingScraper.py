import urllib2
import bs4
import re

#gets the three most recent trending articles on the ftse 100 page

def trendingFTSE():

    #url for the trending stories on the ftse 100
    trending = "https://uk.finance.yahoo.com/quote/%5EFTSE/"

    requestTrending = urllib2.urlopen(trending)

    htmlTrending = requestTrending.read()

    soupTrending = bs4.BeautifulSoup(htmlTrending, "html.parser")

    #filter out required tags, up to the limit of 3 stories
    heads = soupTrending.find_all('div', class_='Py(14px) Pos(r)', limit=3)

    f = open('main2.html','w')

    message = """HEFKPFKOPWEJIFJEWIOUEFHWIWEJFIFWEHIO"""

    f.write(message)
    f.close()

    headline = []
    paragraph = []

    for first in heads:

        #filters the headline of the article
        a = str(first.h3.text.encode("utf-8"))
        headline = [a]

        #filters the main text summary of the article
        b = str(first.p.text.encode("utf-8"))
        paragraph = [b]

        #filters the link to the article
        c = first.h3.a

        #filters the date the article was published
        date = first.find('div', class_= 'C(#959595) Fz(11px) D(ib) Mb(6px)').text

        print
        print("  Headline  ")
        print(" , ".join(headline))
        headline.append(headline)
        print("  link   ")
        print("https://uk.finance.yahoo.com" + c.get('href'))
        print("  Summary  ")
        print(" , ".join(paragraph))
        paragraph.append(paragraph)
        print ("  Time  ")
        print(date)

trendingFTSE()
