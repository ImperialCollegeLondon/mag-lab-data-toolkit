from src.calibration.Calibrator import SpinAxisCalibrator
from src.calibration.calibrationFormatProcessor import CalibrationFormatProcessor
from src import CDFLoader
from pathlib import Path

inputFile = "examples/solo_L2_mag-rtn-ll-internal_20210915_V03.cdf"
outputFile="tmp/output.json"

inputPath = Path(inputFile)
outputPath = Path(outputFile)

inputData = CDFLoader.load_cdf(inputPath)
calibrator = SpinAxisCalibrator()
calibration = calibrator.generateCalibration(inputData)
CalibrationFormatProcessor.writeToFile(calibration, outputPath)

