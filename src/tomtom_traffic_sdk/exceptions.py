from __future__ import annotations


class TomTomTrafficError(Exception):
    """Base SDK error."""


class ValidationError(TomTomTrafficError):
    """Raised when SDK inputs are invalid."""


class ApiError(TomTomTrafficError):
    """Raised when an HTTP response is not successful."""

    def __init__(self, *, status_code: int, message: str, body: str | bytes | None = None) -> None:
        super().__init__(f"HTTP {status_code}: {message}")
        self.status_code = status_code
        self.message = message
        self.body = body
