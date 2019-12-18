from dataclasses import dataclass

from taiga_client.models.fields import Field


@dataclass
class Base:
    id: int = Field()
    created_date: str = Field()
    modified_date: str = Field()
