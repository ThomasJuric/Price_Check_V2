import requests
from bs4 import BeautifulSoup


# def searchAmazon(product):

# def searchEbay(product):
#     webbrowser.open(ebay, new=1)


# def searchKijiji(product):
#     webbrowser.open(kijiji, new=1)

# def searchWalmart(product):
#     webbrowser.open(walmart, new=1)
    
# def searchFacebook(product):
#     webbrowser.open(facebook, new=1)












# product = input("Enter a product you'd like to search for")

amazon = requests.get('https://www.amazon.ca/')
# ebay = requests.get('https://www.ebay.com/')
# kijiji = requests.get('https://www.kijiji.ca/')
# walmart = requests.get('https://www.walmart.com/')
# facebook = requests.get('https://www.facebook.com/marketplace/')
# print(amazon.headers)
src = amazon.content
soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
print(links)
print("\n")


# searchAmazon(product)
# searchEbay(product)
# searchKijiji(product)
# searchWalmart(product)
# searchFacebook(product)



