from pathlib import Path
from src.CDFLoader import load_cdf
from src.MatlabWrapper import runCalibration
from src.calibrationFormatProcessor import CalibrationFormatProcessor

class CalibrationWrapper:

    def generateCalibration(input_path: Path, output_path: Path):
        cdf = load_cdf(input_path)
        calibration = runCalibration(cdf)
        CalibrationFormatProcessor.writeToFile(calibration, output_path, createDirectory=True)

if __name__=="__main__":
    CalibrationWrapper.generateCalibration("examples/solo_L2_mag-rtn-ll-internal_20210915_V03.cdf", "tmp/calibration-example.json")


