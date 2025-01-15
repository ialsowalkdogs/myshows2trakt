import pytest
from unittest.mock import patch, Mock
import pandas as pd
from src.main import convert_rating

# Tests for convert_rating
@pytest.mark.parametrize("input_rating,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8),
    (5, 10),
    (None, None)
])
def test_convert_rating(input_rating, expected):
    assert convert_rating(input_rating) == expected
