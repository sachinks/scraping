import os
from logging_config import setup_logging
from scraper import QuoteScraper


def main():
    """
    Entry point of the application.
    Sets up logging and runs scraper.
    """

    debug_mode = os.getenv("DEBUG") == "1"

    setup_logging(debug=debug_mode)

    url = "https://quotes.toscrape.com"
    scraper = QuoteScraper(base_url=url)
    scraper.run()


if __name__ == "__main__":
    main()
