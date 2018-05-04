import bs4
import urllib2

# ref:
# https://stackoverflow.com/questions/11790535/extracting-data-from-html-table
# http://www.pythonforbeginners.com/python-on-the-web/how-to-use-urllib2-in-python/

# Notes:
# - Need to have a table that has FTSE100 companies with the following LSE data; ISIN Number, Country, Currency, Segment Number -
#   to generate FourWayKey, to form the URL. DB said the FTSE100 list can be assumed to be static, so the table only needs
#   to be filled like this once.
#
#   FourWayKey Format: |ISIN Number|Country|Currency|Segment Number|
#
# - Need to carry out a check to make sure company is in FTSE100 i.e. return an error message if company isn't in the table.



def scrapePriceLSE(FourWayKey):
    # URL
    url = 'http://www.londonstockexchange.com/exchange/prices-and-markets/stocks/summary/company-summary/' + FourWayKey + '.html'

    # prepare request
    request = urllib2.Request(url, data=None, headers={'User-Agent': "WebScraper"})

    # send request and catch response
    response = urllib2.urlopen(request)

    # extract response
    html = response.read()

    # prepare HTML for parsing
    soup = bs4.BeautifulSoup(html, "html.parser")

    # parse and filter out required tag
    table = soup.find("table").find("tbody").find("tr").find_all("td", limit=2)

    # extract the price
    price = table[1].text           # 'price' extracted
    
    return price

