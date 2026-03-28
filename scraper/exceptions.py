class ScraperError(Exception):
    """
    Base exception for all scraper errors.
    Catch this to handle any scraper failure in one place.
    """
    pass


class ScraperSetupError(ScraperError):
    """
    Raised when Playwright or the browser fails to initialise.
    Not retryable — if the browser won't launch, retrying won't help.
    """
    pass


class ScraperNavigationError(ScraperError):
    """
    Raised when the scraper cannot load a URL.
    Retryable — transient network issues can resolve on their own.
    """
    pass


class ScraperPageError(ScraperError):
    """
    Raised when a page-level operation fails, e.g. waiting for a
    selector or clicking the next-page button.
    Retryable — the page may not have fully loaded yet.
    """
    pass


class ScraperExtractionError(ScraperError):
    """
    Raised when a single quote item cannot be extracted.
    Non-fatal — logged and skipped so the rest of the page still saves.
    """
    pass


class ScraperSaveError(ScraperError):
    """
    Raised when scraped data cannot be written to disk.
    Not retryable — likely a permissions or disk-space issue.
    """
    pass
