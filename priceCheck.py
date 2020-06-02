import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
# ebay = requests.get('https://www.ebay.com/')
# kijiji = requests.get('https://www.kijiji.ca/')
# walmart = requests.get('https://www.walmart.com/')
# facebook = requests.get('https://www.facebook.com/marketplace/')

def searchAmazon(product):
    # Check the first 3 products
    amazonLink = ('https://www.amazon.ca/s?k=' + product + '&ref=nb_sb_noss_2')
    headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    cookies = dict(cookies_are='working')
    print ('Searching for product ' + product + ' on Amazon')
    amazon = requests.get(amazonLink, headers=headers)
    soup = BeautifulSoup(amazon.text, 'html.parser')
    data = []
    for span in soup.find_all('span', {'class','a-price-whole'}):
        values = [span.text for div in span.find_all('span')]
        data.append(values)
    links = []
    for link in soup.find_all('a', {'class','a-text-normal'}):
        links.append(link['href'])
    if(len(data) > 0):
        return (data, links)
    else:
        return(0)

def getAmazonInformation(theData, links):
    # Obtain the 3 top prices, as these are most likely the most related products to the user search
    if(len(theData) > 4):
        price1 = str(theData[0])
        price2 = str(theData[1])
        price3 = str(theData[2])
        price4 = str(theData[3])
        n = 4
        for i in range(n-1):
            for j in range(0, n-i-1):
                if(theData[j] > theData[j+1]):
                    theData[j], theData[j+1] = theData[j+1], theData[j]
    theLink = ""
    if(str(theData[0]) == price1):
        theLink = str(links[0])
    elif(str(theData[0]) == price2):
        theLink = str(links[2])
    elif(str(theData[0]) == price3):
        theLink = str(links[4])
    elif(str(theData[0]) == price4):
        theLink = str(links[6])
    theActualLink = 'amazon.ca' + theLink
    return (theActualLink, str(theData[0]))




def searchEbay(product):
    ebayLink = ('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312.R1.TR11.TRC2.A0.H0.Xla.TRS1&_nkw=' + product + '&_sacat=0')
    headers = {
        'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    cookies = dict(cookies_are='working')
    print ('Searching for product ' + product + ' on eBay')
    print('Please note ** eBay is constantly being updated and results may not be the 100% consistent **')
    ebay = requests.get(ebayLink, headers=headers)
    soup = BeautifulSoup(ebay.text, 'html.parser')
    data = []
    for span in soup.find_all('span', {'class','s-item__price'}):
        values = [span.text for div in span.find_all('span')]
        data.append(values)
    # print(data)
    links = []
    for link in soup.find_all('a', {'class','s-item__link'}):
        links.append(link['href'])
    # print(links)
    if(len(data) > 0):
        return (data, links)
    else:
        return(0)

def getEbayInformation(theData, links):
    if(len(theData) > 4):
        price1 = str(theData[0])
        price2 = str(theData[1])
        price3 = str(theData[2])
        price4 = str(theData[3])
        n = 4
        for i in range(n-1):
            for j in range(0, n-i-1):
                if(theData[j] > theData[j+1]):
                    theData[j], theData[j+1] = theData[j+1], theData[j]
    theLink = ""
    if(str(theData[0]) == price1):
        theLink = str(links[0])
    elif(str(theData[0]) == price2):
        theLink = str(links[1])
    elif(str(theData[0]) == price3):
        theLink = str(links[2])
    elif(str(theData[0]) == price4):
        theLink = str(links[3])
    theActualLink = theLink
    return (theActualLink, str(theData[0]))


# def searchKijiji(product):
#     webbrowser.open(kijiji, new=1)

# def searchWalmart(product):
#     webbrowser.open(walmart, new=1)
    
# def searchFacebook(product):
#     webbrowser.open(facebook, new=1)





product = input("Enter a product you'd like to search for: ")





amazonCount = 0
while ((amazonCount < 51)):
    result, links = searchAmazon(product)
    if(result == 0):
        amazonCount = amazonCount + 1
        print('attempted: '+ str(amazonCount))
    else:
        break

if(amazonCount == 51):
    print("Error occurred gathering information from Amazon..")
else:
    theLink, thePrice = getAmazonInformation(result, links)
    print("\n\nFound the cheapest price to be $" + thePrice)
    print('\n')
    print("This product can be found at: ")
    print(theLink)
    print('-------------------------------------------------')


ebayCount = 0
while ((ebayCount < 51)):
    ebayResult, ebayLinks = searchEbay(product)
# searchEbay(product)
    if(ebayResult == 0):
        ebayCount = ebayCount + 1
        print('attempted: '+ str(ebayCount))
    else:
        break

if(ebayCount == 51):
    print("Error occurred gathering information from eBay..")
else:
    theLink, thePrice = getEbayInformation(ebayResult, ebayLinks)
    print("\n\nFound the cheapest price to be $" + thePrice)
    print('\n')
    print("This product can be found at: ")
    print(theLink)
    print('-------------------------------------------------')


# print("outside of the statement")
# searchEbay(product)
# searchKijiji(product)
# searchWalmart(product)
# searchFacebook(product)



