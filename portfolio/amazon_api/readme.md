# Amazon API Web Scraper

This is a simple Amazon API Web Scraper designed to extract data from Amazon’s product listings for a specific keyword(s). It gathers data around product names, prices, ratings, whether or not the products are on Prime, and if they're categorized as sustainable. 

The data from the scraper exports in a CSV and can be used for data analysis purposes. 

# How it works

First, the user specifies the keyword of interest and the filename. Then, they create an instance of the Amazon Scraper. After this, they use the scrape_amazon function to get all matching products from Amazon. Finally, they save these results to a csv using the save_to_csv function.



