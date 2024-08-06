"""
Testing Suite
"""
import pytest
from utils import convert_str_to_list, calculate_progress_pc


def test_convert_str_to_list():
    """
    Tests that the convert_str_to_list function takes a string of items separated by commas 
    and converts to a list
    """
    converted_list = convert_str_to_list('Linux, Bash Scripting, Docker, Python')
    expected_result = ['Linux', 'Bash Scripting', 'Docker', 'Python']
    assert converted_list == expected_result

def test_calculate_progress_pc():
    """
    Tests that the calculate_progress_pc function calculates a percentage based on 2 lists
    """
    modules = ['Linux', 'Bash Scripting', 'Docker', 'Python']
    completed = ['Windows', 'Powershell', 'GitBash', 'Docker']
    calculated_pc = calculate_progress_pc(modules, completed)
    assert calculated_pc == 100.00

def test_division_by_zero_error():
    """
    Tests that the calculate_progress_pc function fails correctly when trying to divide by zero
    """
    modules = []
    completed = ['Windows', 'Powershell', 'GitBash', 'Docker']
    with pytest.raises(ZeroDivisionError) as excinfo:
        calculate_progress_pc(modules, completed)
    assert excinfo.type is ZeroDivisionError
