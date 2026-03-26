import time
from playwright.sync_api import TimeoutError


def retry(func):
    """
    Retry decorator for handling transient failures.
    Retries only TimeoutError.
    """

    def wrapper(self, *args, **kwargs):
        for attempt in range(1, self.retries + 1):
            try:
                self.logger.debug(
                    f"{func.__name__} attempt {attempt}/{self.retries}"
                )
                return func(self, *args, **kwargs)

            except TimeoutError as e:
                self.logger.warning(
                    f"{func.__name__} timeout on attempt {attempt}: {e}"
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
