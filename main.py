import os
import sys
import logging
from utils.logger import setup_logging
from scraper.scraper import QuoteScraper
from scraper.exceptions import (
    ScraperSetupError,
    ScraperNavigationError,
    ScraperPageError,
    ScraperSaveError,
)


def main():
    """
    Entry point of the application.
    Sets up logging and runs scraper.
    """

    debug_mode = os.getenv("DEBUG") == "1"

    setup_logging(debug=debug_mode)

    logger = logging.getLogger(__name__)

    url = "https://quotes.toscrape.com"
    scraper = QuoteScraper(base_url=url)

    try:
        scraper.run()

    except ScraperSetupError:
        logger.critical("Browser failed to launch. Check Playwright installation.")
        sys.exit(1)

    except ScraperNavigationError:
        logger.error("Site unreachable after all retries. Check URL or network.")
        sys.exit(1)

    except ScraperPageError:
        logger.error("Scrape interrupted mid-run. Partial data may have been saved.")
        sys.exit(1)

    except ScraperSaveError:
        logger.critical("Data was scraped but could not be saved. \
        Check disk space and permissions.")
        sys.exit(1)

    except Exception:
        logger.critical("Unexpected error.", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
