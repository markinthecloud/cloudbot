"""
A collection of utility functions for use throughout the project
"""
import re

MODULES = """
        Linux, Bash Scripting, Docker, Python, Git & GitHub, Basic Networking,
        AWS or Azure, Terraform, CI/CD - Github Actions, Ansible, Build Projects
        """

def convert_str_to_list(strings:str):
    """
    Takes a string of values separated by a comma and splits into a list
    """
    new_list = [string.strip() for string in strings.split(",")]
    return new_list

def calculate_progress_pc(modules: list, completed: list):
    """
    Takes 2 lists, gets the length of both and then calculates a %
    """
    progress_pc = len(completed)/len(modules)*100
    formatted_pc = f"{progress_pc:.2f}"
    return float(formatted_pc)

def extract_topic(command:str):
    """
    Takes a string and uses regex to drop "!complete" from it in order
    to extract the remaining text
    """
    match = re.match(r'!complete (.+)', command)
    if match:
        topic_name = match.group(1).strip()
        return topic_name
    return None

def extract_role(command:str):
    """
    Takes a string and uses regex to drop "!role" from it in order
    to extract the remaining text
    """
    match = re.match(r'!role (.+)', command)
    if match:
        topic_name = match.group(1).strip()
        return topic_name
    return None
