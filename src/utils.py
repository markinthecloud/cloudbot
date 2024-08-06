import re

MODULES = """
            Linux, Bash Scripting, Docker, Python, Git & GitHub, Basic Networking,
            AWS or Azure, Terraform, CI/CD - Github Actions, Ansible, Build Projects
            """

def convert_str_to_list(strings:str):
    list = [string.strip() for string in strings.split(",")]
    return list

def calculate_progress_pc(modules: list, completed: list):
    progress_pc = len(completed)/len(modules)*100
    formatted_pc = f"{progress_pc:.2f}"
    return float(formatted_pc)

def extract_topic(command:str):
    match = re.match(r'!complete (.+)', command)
    if match:
        topic_name = match.group(1).strip()
        return topic_name
    else:
        return None
    
def extract_role(command:str):
    match = re.match(r'!role (.+)', command)
    if match:
        topic_name = match.group(1).strip()
        return topic_name
    else:
        return None


