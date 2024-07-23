from datetime import datetime
from enum import Enum
from pathlib import Path

from pydantic import BaseModel
from typing import List, Optional

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

if __name__ == "__main__":
    path = Path("examples/calibrations.json")
    model = CalibrationFormat.parse_file(path)
    print(model)




