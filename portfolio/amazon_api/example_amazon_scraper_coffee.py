from web_scraper.amazon_scraper import AmazonScraper

keyword = "coffee beans"
filename = "coffee beans data"
scraper = AmazonScraper(keyword, filename)
items = scraper.scrape_amazon()
scraper.save_to_csv(items)
