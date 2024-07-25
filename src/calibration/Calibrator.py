from abc import ABC, abstractmethod
from enum import Enum
from src.calibration.calibrationFormat import CalibrationFormat, OffsetCollection, SingleCalibration, Unit
from xarray import Dataset
import numpy as np
from src.calibration import MatlabWrapper
from datetime import datetime

class CalibratorType(Enum):
    SPINAXIS = "SpinAxisCalibrator",
    SPINPLANE = "SpinPlaneCalibrator"

class Calibrator(ABC):
    
    @abstractmethod
    def generateOffsets(self, data) -> OffsetCollection:
        """ Generates a set of offsets """
    
    def generateCalibration(self, data) -> CalibrationFormat:
        singleCalibration = self.generateOffsets(data)
        calibration = CalibrationFormat(valid_start = singleCalibration.timestamps[0], valid_end = singleCalibration.timestamps[-1], calibrations=[singleCalibration])
        return calibration


class SpinAxisCalibrator(Calibrator):

    def __init__(self):
        self.name = CalibratorType.SPINAXIS

    def generateOffsets(self, data:Dataset) -> SingleCalibration:

        """
        TODO
        Integration with MATLAB to generate real offsets
        """
        (timestamps, spin_axis_offsets) = MatlabWrapper.simulateSpinAxisCalibration(data)

        offsetCollection = OffsetCollection(X = np.zeros(len(spin_axis_offsets)), Y=np.zeros(len(spin_axis_offsets)), Z = spin_axis_offsets)

        sensor_name = "MAGO"

        singleCalibration = SingleCalibration(timestamps = timestamps, 
                                              offsets = offsetCollection, 
                                              units = Unit.NT, 
                                              instrument = sensor_name, 
                                              creation_timestamp = datetime.now(),
                                              method = str(self.name))
        return singleCalibration



