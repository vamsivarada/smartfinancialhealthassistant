"""
This script allows a user to input a query related to financial topics.
 It then scrapes Investopedia's search results for articles related to the query
 and displays the titles along with their links.

Please note:

Web scraping might violate website terms of service. Always check a website's terms and conditions
 and consider APIs or official data sources.
Websites might change their structure, so the scraping logic might need updates.
This example is just a starting point and doesn't provide full interaction or
 dynamic content retrieval from websites. For a more interactive experience,
  consider using APIs or developing a web-based chatbot.
"""
import requests
from bs4 import BeautifulSoup

def get_investopedia_articles(query):
    search_url = f"https://www.investopedia.com/search?q={query}"
    response = requests.get(search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        article_links = soup.select(".search-results .card-title a")

        if article_links:
            print(f"Here are some articles related to '{query}':")
            for link in article_links[:5]:  # Displaying the first 5 articles
                print(link.text.strip())
                print(link['href'])
        else:
            print("No articles found.")
    else:
        print("Failed to retrieve data.")

def main():
    print("Welcome! Ask me about a financial topic to find related Investopedia articles.")
    while True:
        user_query = input("You: ")
        if user_query.lower() == 'exit':
            print("Goodbye!")
            break
        get_investopedia_articles(user_query)

if __name__ == "__main__":
    main()
