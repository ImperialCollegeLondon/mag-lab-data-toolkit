from datetime import datetime
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, model_validator
from typing import List, Optional
from typing_extensions import Self

class Unit(Enum):
    NT = "nT"
    UT = "uT"
    T = "T"

class Instrument(Enum):
    MAGO = "MAGO"
    MAGI = "MAGI"

class OffsetCollection(BaseModel):
    X: List[float]
    Y: List[float]
    Z: List[float]

    @model_validator(mode='after')
    def check_lengths_match(self) -> Self: 
        if len(self.X) != len(self.Y) or len(self.Y) != len(self.Z) or len(self.X) != len(self.Z):
            raise ValueError('Length of offset lists do not match')
        return self


class SingleCalibration(BaseModel):
    timestamps: List[datetime]
    offsets: OffsetCollection
    units: Unit
    instrument: Instrument
    creation_timestamp: datetime
    method: str
    comment: Optional[str] = None

class CalibrationFormat(BaseModel):
    valid_start: datetime
    valid_end: datetime
    calibrations: List[SingleCalibration]




