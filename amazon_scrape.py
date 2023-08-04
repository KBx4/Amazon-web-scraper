# Importing BeautifulSoup for parsing HTML and requests for making HTTP requests
from bs4 import BeautifulSoup
import requests

# Function to retrieve and list the products based on user's search
def products_page():
    prod = input("Enter the product you wanna search for: ")
    main_url = "https://www.amazon.in/s?k=" + prod
    main_page = requests.get(main_url).text
    soup = BeautifulSoup(main_page, 'lxml')
    products = soup.find_all("div",
                             class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16")
    i = 0
    prod_links = [] #List to store product links
    
    # Iterating through the products and retrieving the details
    for product in products:
        link = product.find('a', href=True)
        prod_link = "https://www.amazon.in" + link['href']
        prod_links.append(prod_link)
        i += 1
        name = product.find("span", class_="a-size-medium a-color-base a-text-normal").text.strip()
        print(str(i) + ": " + name)
        if i == 10:  #Limiting the output to the first 10 products
            break
    #Keeps looping until user decides to exit        
    while True:
        sr_no = input("Enter the serial number of the product you wanna know more about: ")
        url = prod_links[int(sr_no) - 1]
        product_info(url)
        print("Want information about other products?[y/n]")
        if input() == 'n':
            print("Thank you!")
            break

#Function to display detailed information about a selected product
def product_info(prod_url):
    product_page = requests.get(prod_url).text
    soup = BeautifulSoup(product_page, 'lxml')
    product = soup.find("span", class_='a-size-large product-title-word-break').text.strip()
    price = soup.find("span", class_='a-price-whole').text.strip()
    info = soup.find_all("li", class_='a-spacing-mini')
    print()
    print("Product name: " + product)
    print()
    print("Price: " + price)
    print()
    print("About the product:")
    print()
    for points in info:
        points = points.text.strip()
        print("-" + points)
        print()

#Call to initiate program 
products_page()









