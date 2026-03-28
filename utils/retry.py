import time
from scraper.exceptions import ScraperNavigationError


def retry(func):
    """
    Retry decorator for handling transient failures.
    Retries only ScraperNavigationError.
    """

    def wrapper(self, *args, **kwargs):
        for attempt in range(1, self.retries + 1):
            try:
                self.logger.debug(
                    f"{func.__name__} attempt {attempt}/{self.retries}"
                )
                return func(self, *args, **kwargs)

            except ScraperNavigationError as e:
                self.logger.warning(
                    f"{func.__name__} navigation error on attempt {attempt}: {e}"
                )

                if attempt == self.retries:
                    self.logger.exception(
                        f"{func.__name__} failed after {self.retries} attempts"
                    )
                    raise

                time.sleep(self.delay * attempt)

            except Exception:
                self.logger.exception(
                    f"{func.__name__} Non-retryable error"
                )
                raise  # no retry

        raise RuntimeError(
            f"{func.__name__} failed unexpectedly without returning"
        )

    return wrapper
