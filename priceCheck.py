import requests
from bs4 import BeautifulSoup


def searchAmazon(product):
    # Check the first 3 products
    amazonLink = ('https://www.amazon.ca/s?k=' + product)
    cookies = dict(cookies_are='working')
    print ('searching for ' + product)
    amazon = requests.get(amazonLink, cookies=cookies)
    soup = BeautifulSoup(amazon.text, 'html.parser')
    data = []
    for span in soup.find_all('span', {'class','a-price-whole'}):
        values = [span.text for div in span.find_all('span')]
        data.append(values)
    price1 = data[0]
    print(price1)
    # print(re.findall("\d", price1))

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


searchAmazon(product)
# searchEbay(product)
# searchKijiji(product)
# searchWalmart(product)
# searchFacebook(product)



