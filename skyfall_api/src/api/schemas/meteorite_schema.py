from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class MeteoriteCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        populate_by_name=True,
        str_strip_whitespace=True,
    )

    name: str = Field(min_length=1)
    nametype: Literal["Relict", "Valid"]
    recclass: str = Field(min_length=1)
    mass_g: float | None = Field(default=None, alias="mass (g)", ge=0)
    fall: Literal["Fell", "Found"]
    year: float | None = None
    reclat: float | None = Field(default=None, ge=-90, le=90)
    reclong: float | None = Field(default=None, ge=-180, le=180)
    geo_location: str | None = Field(default=None, alias="GeoLocation")
