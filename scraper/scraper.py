import json
import logging
from typing import List, Dict
from playwright.sync_api import sync_playwright

from utils.retry import retry
from utils.timeit import timeit


class QuoteScraper:
    """
    Production-grade scraper with logging, retry, and performance tracking.
    """

    def __init__(self, base_url: str, retries: int = 3, delay: int = 2):
        """
        Initialize scraper configuration.

        Args:
            retries (int): Number of retry attempts.
            delay (int): Delay between retries in seconds.
        """
        self.base_url = base_url
        self.data: List[Dict] = []
        self.browser = None
        self.page = None
        self.playwright = None
        self.retries = retries
        self.delay = delay
        self.logger = logging.getLogger(self.__class__.__name__)

    def setup(self) -> None:
        """
        Initialize Playwright and browser.
        """
        self.logger.debug("Entering setup()")

        try:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=False)
            self.page = self.browser.new_page()

            self.logger.info("Browser launched successfully")

        except Exception:
            self.logger.exception("Setup failed")
            raise

        finally:
            self.logger.debug("Exiting setup()")

    @retry
    @timeit
    def navigate(self) -> None:
        """
        Navigate to base URL with retry and timing.
        """
        self.logger.debug("Entering navigate()")

        try:
            self.logger.info(f"Navigating to {self.base_url}")

            self.page.goto(self.base_url, timeout=60000)

            self.logger.info("Page loaded successfully")

        except Exception:
            self.logger.exception("Navigation failed")
            raise

        finally:
            self.logger.debug("Exiting navigate()")

    @timeit
    def scrape(self) -> None:
        """
        Scrape quotes across all pages.
        """
        self.logger.debug("Entering scrape()")

        try:
            self.navigate()

            while True:
                self.page.wait_for_selector(".quote")

                quotes = self.page.locator(".quote")

                for i in range(quotes.count()):
                    try:
                        quote = quotes.nth(i)

                        text = quote.locator(".text").inner_text()
                        author = quote.locator(".author").inner_text()

                        self.data.append({
                            "text": text,
                            "author": author
                        })

                    except Exception:
                        self.logger.error(
                            f"Item extraction failed at index {i}"
                        )

                next_btn = self.page.locator(".next a")

                if next_btn.count() == 0:
                    self.logger.info("No more pages")
                    break

                next_btn.click()

        except Exception:
            self.logger.exception("Scrape failed")
            raise

        finally:
            self.logger.debug("Exiting scrape()")

    @timeit
    def save(self) -> None:
        """
        Save scraped data to JSON file.
        """
        self.logger.debug("Entering save()")

        try:
            with open("quotes.json", "w") as f:
                json.dump(self.data, f, indent=2)

            self.logger.info(f"Saved {len(self.data)} records")

        except Exception:
            self.logger.exception("Save failed")
            raise

        finally:
            self.logger.debug("Exiting save()")

    def cleanup(self) -> None:
        """
        Close browser and cleanup resources.
        """
        self.logger.debug("Entering cleanup()")

        try:
            if self.browser:
                self.browser.close()

            if self.playwright:
                self.playwright.stop()

            self.logger.info("Cleanup complete")

        except Exception:
            self.logger.error("Cleanup error")

        finally:
            self.logger.debug("Exiting cleanup()")

    def run(self) -> None:
        """
        Execute full scraping workflow.
        """
        self.logger.info("Run started")

        try:
            self.setup()
            self.scrape()
            self.save()

        except Exception:
            self.logger.exception("Run failed")

        finally:
            self.cleanup()
            self.logger.info("Run finished")
