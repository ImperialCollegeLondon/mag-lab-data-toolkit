from cdflib import xarray
from pathlib import Path

def load_cdf(inputPath: Path):
    """
    Wraps cdlibs xarray reader
    """
    if inputPath.is_file():
        return xarray.cdf_to_xarray(inputPath)
    else:
        raise FileExistsError()