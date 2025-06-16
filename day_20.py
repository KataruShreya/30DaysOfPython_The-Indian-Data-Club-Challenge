import requests

def fetch_page(url):
    try:
        response = requests.get(url, timeout=5)      
        response.raise_for_status()                  
    except requests.exceptions.RequestException as e:
        print("Could not fetch page:", e)
        return


    print("\nPage preview:\n")
    print(response.text[:500])

url = input("Enter URL: ").strip()
fetch_page(url)           



# CODE LOGIC

'''

1. We import the requests module:
   - It gives us the get() function that can send HTTP requests and return responses.

2. We define a helper function fetch_page(url) to grab the page at 'url' and print its entire HTML (or show an error).

3. Inside fetch_page we wrap the download in a 'try … except' block:
   a. response = requests.get(url, timeout=5)
      - Sends an HTTP GET request.
      - 'timeout=5' makes the call fail after 5 seconds instead of hanging forever.

   b. response.raise_for_status()
      - If the server answers with 4xx/5xx, this converts it into a Python exception.

   c. except requests.exceptions.RequestException as e
      - Catches anything that can go wrong (bad URL, no network, timeout, 404, 500…).
      - Prints a friendly 'Could not fetch page' message and then returns, so nothing else runs.

4. If no exception happened, we know the request succeeded:
   - We print a header line: '--- Page content start ---'
   - We print response.text[:500], which prints the first 500 characters of HTML (decoded by 'requests').
   - We finish with '--- Page content end ---' so users can see where it stops.

5. The last two lines at the bottom actually run the program:
   a. url = input('Enter URL: ').strip()
      - This line asks the user to type a website link (URL) and removes any extra spaces.

   b. fetch_page(url)
      - This line takes that link and tells the function to go open the webpage and show its contents.


6. Result:
   - If you type 'https://www.python.org', the first 500 characters of the HTML for python.org is shown.
   - If you type an invalid link or unplug your Wi-Fi, you get a clear error message instead of a crash.

'''
