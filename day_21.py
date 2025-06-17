import requests
from bs4 import BeautifulSoup

url = input("Enter the URL: ")
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')


headlines = soup.find_all(['h1', 'h2', 'h3'])


for h in headlines:
    print(h.text)
    print("\n")



# CODE LOGIC

'''

1. We import two libraries:
   a. requests, to fetch the webpage content from the internet.
   b. BeautifulSoup from bs4, to parse the HTML content of the webpage.

2. We ask the user to input a URL:
   - input("Enter the URL: ") prompts the user to enter a website link.
   - The entered URL is stored in the variable 'url'.

3. We use requests.get(url) to send a GET request to the provided URL:
   - This fetches the HTML content of the webpage.
   - The result is stored in the variable 'page'.

4. We parse the HTML using BeautifulSoup:
   - soup = BeautifulSoup(page.text, 'html.parser') creates a parsed HTML object.
   - page.text contains the raw HTML content of the webpage.
   - 'html.parser' tells BeautifulSoup to use built-in HTML parser of python.

5. We extract all headings from the page:
   - soup.find_all(['h1', 'h2', 'h3']) searches for all <h1>, <h2>, and <h3> tags in the HTML.
   - These tags usually contain the main headlines on a page.
   - The results are stored in the 'headlines' list.

6. We loop through the headlines and print each one:
   - for h in headlines: loops through all the found heading tags.
   - h.text gets the visible text inside each heading tag.
   - print(h.text) displays the headline on the screen.

7. Result:
   - The script shows all major headings (h1/h2/h3) from the entered URL.
   - It's a simple way to extract headline-like content from any webpage.

'''
