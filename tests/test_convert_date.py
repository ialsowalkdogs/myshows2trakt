import pytest
from unittest.mock import patch, Mock
import pandas as pd
from src.main import convert_date

# Tests for convert_date
@pytest.mark.parametrize("input_date,expected", [
    ('2024-01-14', '2024-01-14T00:00:00.000Z'),
    ('2023-12-31', '2023-12-31T00:00:00.000Z'),
    ('2024-02-29', '2024-02-29T00:00:00.000Z'),  # Leap year
])
def test_convert_date_regular_cases(input_date, expected):
    assert convert_date(input_date) == expected

@pytest.mark.parametrize("null_value", [
    pd.NA,
    None,
    pd.NaT
])
def test_convert_date_null_cases(null_value):
    assert convert_date(null_value) is None

@pytest.mark.parametrize("invalid_date", [
    '14/01/2024',  # Wrong format
    '2024-13-01',  # Invalid month
])
def test_convert_date_invalid_format(invalid_date):
    with pytest.raises(ValueError):
        convert_date(invalid_date)

