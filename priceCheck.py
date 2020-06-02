import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


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
    print ('searching for ' + product)
    amazon = requests.get(amazonLink, headers=headers)
    soup = BeautifulSoup(amazon.text, 'html.parser')
    # ideas = soup.find('div', {'class':'sg-col-20-of-24 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-8-of-12 sg-col-12-of-16 sg-col-24-of-28'})
    
    # print(ideas)
    # print(soup)
    # data = soup.find_all('div')
    data = []
    for span in soup.find_all('span', {'class','a-price-whole'}):
        values = [span.text for div in span.find_all('span')]
        data.append(values)
    if(len(data) > 0):
        return (data)
    else:
        return(0)

def getAmazonInformation(theData):
    # Obtain the 3 top prices, as these are most likely the most related products to the user search
    if(len(theData) > 4):
        n = 4
        for i in range(n-1):
            for j in range(0, n-i-1):
                if(theData[j] > theData[j+1]):
                    theData[j], theData[j+1] = theData[j+1], theData[j]

    for i in range(4):
        print ("%s" %str(theData[i]))
    
    print("Cheapest Price Found For Product Searched On Amazon Is: $" + str(theData[0]))

    # print("Price 1 : " + price1)
    # print("Price 2 : " + price2)
    # print("Price 3 : " + price3)
    # if(price1>price3):
    #     print(price1 + " > " + price3)
    # else:
    #     print(price1 + " < " + price3)





# def searchEbay(product):
#     webbrowser.open(ebay, new=1)


# def searchKijiji(product):
#     webbrowser.open(kijiji, new=1)

# def searchWalmart(product):
#     webbrowser.open(walmart, new=1)
    
# def searchFacebook(product):
#     webbrowser.open(facebook, new=1)





product = input("Enter a product you'd like to search for: ")
# ebay = requests.get('https://www.ebay.com/')
# kijiji = requests.get('https://www.kijiji.ca/')
# walmart = requests.get('https://www.walmart.com/')
# facebook = requests.get('https://www.facebook.com/marketplace/')
# print(amazon.headers)
# print(soup)
amazonCount = 0
while ((amazonCount < 51)):
    result = searchAmazon(product)
    if(result == 0):
        amazonCount = amazonCount + 1
        print('attempted: '+ str(amazonCount))
    else:
        # print("Worked!")
        # print("\nResult Found Below:\n")
        # print(result)
        break

if(amazonCount == 51):
    print("Error occurred gathering information from Amazon..")
else:
    getAmazonInformation(result)


# print("outside of the statement")
# searchEbay(product)
# searchKijiji(product)
# searchWalmart(product)
# searchFacebook(product)



