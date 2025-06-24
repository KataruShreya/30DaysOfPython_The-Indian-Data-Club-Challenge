import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    
    #Fetches the HTML content of the given URL. Raises an exception if the request fails.
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch webpage: {e}")
        return None

def extract_headlines(html):
        
    #Parses HTML and returns a list of h1, h2, h3 tag texts.
    
    soup = BeautifulSoup(html, 'html.parser')
    return [tag.get_text(strip=True) for tag in soup.find_all(['h1', 'h2', 'h3'])]

def display_headlines(headlines):
    
    # Displays each headline on a new line.
    
    if not headlines:
        print("No headlines found.")
    else:
        print("\nHeadlines:\n")
        for headline in headlines:
            print(headline)
            print("\n")

def main():
    
    # Main function to drive the script.
   
    url = input("Enter the URL: ").strip()
    html = fetch_webpage(url)
    if html:
        headlines = extract_headlines(html)
        display_headlines(headlines)

if __name__ == "__main__":
    main()








# CODE LOGIC

'''
1. We import the necessary modules:
   - requests: To make HTTP requests to fetch webpage content.
   - BeautifulSoup from bs4: To parse and extract HTML content.

2. We define the function fetch_webpage(url):
   - Takes a URL as input.
   - Sends a GET request using requests.
   - If the request is successful, it returns the HTML content.
   - If any exception occurs (e.g., invalid URL, no internet), it prints an error and returns None.

3. We define the function extract_headlines(html):
   - Takes the raw HTML content as input.
   - Parses it using BeautifulSoup.
   - Searches for all <h1>, <h2>, and <h3> tags and extracts their text.
   - Returns a list of cleaned headline strings.

4. We define the function display_headlines(headlines):
   - Takes a list of headlines.
   - Prints "No headlines found" if the list is empty.
   - Otherwise, prints each headline on a new line for better readability.

5. We define the main() function:
   - Prompts the user to enter a URL.
   - Fetches the HTML content using fetch_webpage().
   - If the content is valid, it extracts and displays the headlines.

6. We use the if __name__ == "__main__": block:
   - Ensures that main() only runs when this script is executed directly, not when imported as a module.

7. Result:
   - The script fetches a webpage, extracts h1-h3 headlines, and displays them cleanly on the console.
'''
