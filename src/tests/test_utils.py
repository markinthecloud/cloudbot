"""
Testing Suite
"""
import pytest
from utils import calculate_progress_pc, convert_str_to_list, extract_topic, extract_role

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
    response = calculate_progress_pc(modules, completed)
    assert response == "'Division Error - Speak to Mark'"

def test_extract_topic():
    """
    Tests that the extract_topic function correctly extracts the topic from the comment string
    """
    test_command = "!complete Python"
    extracted_topic = extract_topic(test_command)
    assert extracted_topic == "Python"

def test_extract_topic_is_none():
    """
    Tests that the extract_topic function returns None if an no topic is provided
    """
    test_command = "!complete"
    extracted_topic = extract_topic(test_command)
    assert extracted_topic == None

def test_extract_role():
    """
    Tests that the extract_role function correctly extracts the role from the comment string
    """
    test_command = "!role DevOps Engineer"
    extracted_topic = extract_role(test_command)
    assert extracted_topic == "DevOps Engineer"

def test_extract_role_is_none():
    """
    Tests that the extract_role function returns None if an no role is provided
    """
    test_command = "!role"
    extracted_topic = extract_role(test_command)
    assert extracted_topic == None
