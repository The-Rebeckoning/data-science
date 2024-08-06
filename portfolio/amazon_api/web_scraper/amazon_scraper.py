import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

class AmazonScraper:
    def __init__(self, keyword, filename):
        self.keyword = keyword
        self.filename = filename 

    def get_amazon_page(self, keyword, page_number = 1, max_retries = 5):
        """ Returns response.txt, the html text for each page of keyword result"""
        url = f"https://www.amazon.com/s?k={keyword.replace(' ', '+')}&page={page_number}"
        headers = {
            "User-Agent": random.choice([
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15"
            ]),
            "Accept-Language": "en-US,en;q=0.5",
        }
        retries = 0
        while retries < max_retries:
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    return response.text
                elif response.status_code == 503:
                    print(f"503 error encountered. Retrying in {2 ** retries} seconds...")
                    time.sleep(2 ** retries)
                    retries += 1
                else:
                    response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                time.sleep(2 ** retries)
                retries += 1
        raise Exception("Max retries exceeded")

    def parse_amazon_page(self, html):
        """ Returns dictionary of corresponding items for each page of keyword result."""
        soup = BeautifulSoup(html, "html.parser")
        items = []
        for product in soup.find_all("div", {"data-component-type": "s-search-result"}):
            title = product.h2.text.strip()
            price = product.find("span", "a-offscreen").text.strip()
            try:
                rating = product.i.text.strip()
            except AttributeError:
                rating = "N/A"
            try:
                review_count = product.find("span", {"class": 'a-size-base s-underline-text'}).text.strip()
            except:
                review_count = "N/A"
            try:
                prime = "Yes" if product.find("i", {"class": "a-icon-prime"}) or product.find("span", {"class": "a-badge-text", "text": "Prime"}) else "No"
            except AttributeError:
                prime = "No"

            try:
                # Check for "Small Business" badge
                if product.find("span", {"class": "a-badge-text"}) and product.find("span", {"class": "a-badge-text"}).text.strip() == "Small Business":
                    sustainability = "No"
                else:
                    # Check for other span element
                    span_element = product.find("span", {"class": 'a-size-base a-color-base'})
                    if span_element and span_element.text.strip():
                        sustainability = "Yes"
                    else:
                        sustainability = "No"
            except AttributeError:
                # Handle any attribute errors that may occur
                sustainability = "No"
    
            items.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Review Count": review_count,
                "Prime": prime,
                "Sustainability": sustainability
            })
        
        return items

    def save_to_csv(self, items):
        """ Saves items to Panadas Dataframe."""
        items = items
        df = pd.DataFrame(items, columns=["Title", "Price", "Rating", "Review Count", "Prime", "Sustainability"])
        # Print DataFrame content for debugging
        print("DataFrame content before saving:")
        print(df.head())
        filename = f"{self.filename}.csv".replace(' ', '_')
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")


    def scrape_amazon(self):
        all_items = []
        seen_products = []
        page_number = 1
        duplicate_iteration = 0 
        while True:
            print(f"Scraping page {page_number}...")
            try:
                html = self.get_amazon_page(self.keyword, page_number)
                items = self.parse_amazon_page(html)
                if not items:
                    print("No more items found.")
                    break

                # Filter out items that are already seen
                new_items = [item for item in items if item not in seen_products]
        
                
                # If no new items are found, break the loop
                if not new_items and duplicate_iteration < 3:
                    print("No new items found on this page.")
                    duplicate_iteration += 1 
                elif duplicate_iteration == 3: 
                    break
                
                seen_products.extend(new_items)
                #print(f"Number of new items from page {page_number}: len{new_items}\n Number of total items {len(all_items)}")  
                all_items.extend(new_items)
                page_number += 1
                time.sleep(random.uniform(1, 3))  
            
            except Exception as e:
                print(f"Error while scraping page {page_number}: {e}")
                continue
        
        return all_items
    


    

    

