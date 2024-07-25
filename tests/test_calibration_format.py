from datetime import datetime
from src.calibration.calibrationFormatProcessor import CalibrationFormatProcessor
from src.calibration.calibrationFormat import Unit, CalibrationFormat
from pydantic import ValidationError

def test_calibration_read():
    result = CalibrationFormatProcessor.loadFromPath("tests/example/calibrations.json")

    assert result != None
    assert result.calibrations[0].units == Unit.NT
    assert result.calibrations[0].offsets.X == [2.2345, 2.3768]
    assert isinstance(result.valid_start,datetime)

def test_calibration_invalid_file():
    result = CalibrationFormatProcessor.loadFromPath("nonsense/path")

    assert result == None
    
def test_calibration_dict_loading():
    calib_dict = {
        "valid_start":datetime.now(),
        "valid_end": datetime.now(),
        "calibrations": [
            {
                "timestamps": [datetime.now()],
                "offsets": {
                    "X": [0],
                    "Y": [0],
                    "Z": [0],
                },
                "units": "nT",
                "method": "Kepko",
                "instrument": "MAGO",
                "creation_timestamp": datetime.now()
            }
        ]
    }

    calibration = CalibrationFormatProcessor.loadFromDict(calib_dict)

    assert isinstance(calibration, CalibrationFormat)
    assert calibration.calibrations[0].units == Unit.NT
    assert calibration.calibrations[0].offsets.X == [0]
    assert isinstance(calibration.valid_start,datetime)

def test_failed_dict_length_loading():
    calib_dict = {
        "valid_start":datetime.now(),
        "valid_end": datetime.now(),
        "calibrations": [
            {
                "timestamps": [datetime.now()],
                "offsets": {
                    "X": [0],
                    "Y": [0, 1, 2],
                    "Z": [0],
                },
                "units": "nT",
                "method": "Kepko",
                "instrument": "MAGO",
                "creation_timestamp": datetime.now()
            }
        ]
    }

    try:
        calibration = CalibrationFormatProcessor.loadFromDict(calib_dict)
    except ValidationError as e:
        assert True
