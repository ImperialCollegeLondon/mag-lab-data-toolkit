from datetime import datetime
from src.calibrationFormatProcessor import CalibrationFormatProcessor
from src.calibrationFormat import CalibrationFormat

def runCalibration(simulate=True) -> CalibrationFormat:
    """

    """
    example_calib_dict = {
        "valid_start":datetime(2024,4,5),
        "valid_end": datetime(2024,4,6),
        "calibrations": [
            {
                "timestamps": [datetime(2024,4,5)],
                "offsets": {
                    "X": [10],
                    "Y": [-12],
                    "Z": [8],
                },
                "units": "nT",
                "method": "Kepko",
                "instrument": "MAGO",
                "creation_timestamp": datetime.now()
            }
        ]
    }

    return CalibrationFormatProcessor.loadFromDict(example_calib_dict)