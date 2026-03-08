"""Base class for API response schemas."""

from typing import Any

from pydantic import BaseModel


class APIModel(BaseModel):
    """Base API response model."""

    def as_json(self) -> str:
        """Generate a JSON representation of the model."""
        return self.model_dump_json(exclude_none=True, serialize_as_any=True)

    def as_dict(self) -> dict[str, Any]:
        """Generate a dictionary representation of the model."""
        return self.model_dump(exclude_none=True, serialize_as_any=True)

    def __eq__(self, other: object) -> bool:
        """Keep compatibility with pydantic v1 model-to-dict comparisons."""
        if isinstance(other, dict):
            return self.model_dump() == other

        return super().__eq__(other)


class GenericAPIModel(APIModel):
    """Base generic API response model."""
