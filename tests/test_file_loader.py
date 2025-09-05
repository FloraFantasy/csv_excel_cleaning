import unittest
from cleaner.file_loader import load_file
import pandas as pd
import pytest

def test_load_file():
    with pytest.raises(ValueError, match="Unknown file extension"):
        load_file("data/messy_data.txt")
