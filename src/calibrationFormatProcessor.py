from src.calibrationFormat import CalibrationFormat 
from pathlib import Path
from pydantic import ValidationError
import yaml

class CalibrationFormatProcessor:

    def loadFromPath(calibrationPath: Path) -> CalibrationFormat:
        try:
            as_dict = yaml.safe_load(open(calibrationPath))
            model = CalibrationFormat(**as_dict)
            return model
        except ValidationError as e:
            print(e)
            return None
        except FileNotFoundError as e:
            print(e)
            return None
        
    def loadFromDict(calibrationDict: dict) -> CalibrationFormat:
        try:
            model = CalibrationFormat(**calibrationDict)
            return model
        except ValidationError as e:
            print(e)
            return None
        
    def writeToFile(CalibrationFormat: CalibrationFormat, filepath: Path):
        json = CalibrationFormat.model_dump_json()
        try:
            with open(filepath, "w+") as f:
                f.write(json)
        except Exception as e:
            print(e)
            print(f"Failed to write calibration to {filepath}")

        
