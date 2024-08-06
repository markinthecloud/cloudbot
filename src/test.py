import pytest
from utils import convert_str_to_list, calculate_progress_pc


def test_convert_str_to_list():
    converted_list = convert_str_to_list('Linux, Bash Scripting, Docker, Python')
    expected_result = ['Linux', 'Bash Scripting', 'Docker', 'Python']
    assert converted_list == expected_result

def test_calculate_progress_pc():
    modules = ['Linux', 'Bash Scripting', 'Docker', 'Python']
    completed = ['Windows', 'Powershell', 'GitBash', 'Docker']
    calculated_pc = calculate_progress_pc(modules, completed)
    assert calculated_pc == 100.00

def test_division_by_zero_error():
    modules = []
    completed = ['Windows', 'Powershell', 'GitBash', 'Docker']
    with pytest.raises(ZeroDivisionError) as excinfo:
        calculated_pc = calculate_progress_pc(modules, completed)
    assert excinfo.type is ZeroDivisionError