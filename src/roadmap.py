import sqlite3
from db import connect_db
from utils import convert_str_to_list, calculate_progress_pc

MODULES = """
            Linux, Bash Scripting, Docker, Python, Git & GitHub, Basic Networking,
            AWS or Azure, Terraform, CI/CD - Github Actions, Ansible, Build Projects
            """

def create_db_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        modules TEXT NOT NULL,
        completed TEXT
        role TEXT
    )
    """)
    conn.commit()
    conn.close()

def add_new_user(user):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Check if the user already exists
    check_user_command = """
    SELECT 1 FROM progress WHERE name = ?
    """
    cursor.execute(check_user_command, (user,))
    result = cursor.fetchone()
    
    if result:
        return f"{user} has previously joined. Try !progress to see where you're at."
    else:
        # Insert the new user
        sql_command = """
            INSERT INTO progress (name, modules, completed) 
            VALUES (?, ?, ?)
            """
        cursor.execute(sql_command, (user, MODULES, None))
        conn.commit()
        conn.close()
        return f"{user} has joined the revolution!"
    

def retrieve_progress_data(user):
    conn = connect_db()
    cursor = conn.cursor()
    sql_command = """
                    SELECT modules, completed 
                    FROM progress 
                    WHERE name = ?
                    """
    cursor.execute(sql_command, (user,))
    result = cursor.fetchone()
    conn.close()

    if result:
        modules, completed = result
        module_list = convert_str_to_list(modules) if modules else []
        completed_list = convert_str_to_list(completed) if completed else []
        return module_list, completed_list
    else:
        print("No record found for the given user.")
        return [], []

def complete_topic(user, topic):
    conn = connect_db()
    cursor = conn.cursor()
    
    sql_select = """
    SELECT modules, completed 
    FROM progress 
    WHERE name = ?
    """
    
    cursor.execute(sql_select, (user,))
    result = cursor.fetchone()

    if not result:
        print("No record found for the given user.")
        conn.close()
        return
    
    modules, completed = result

    # Convert modules to a list
    modules_list = [module.strip() for module in modules.split(",")]

    # Check if the topic is in the modules list
    if topic not in modules_list:
        conn.close()
        return f"Invalid topic, please try !modules to find a correct list."
    
    # Remove the topic from modules list
    modules_list.remove(topic)
    new_modules = ", ".join(modules_list)
    
    # Add the topic to completed list
    if completed:
        completed_list = [comp.strip() for comp in completed.split(",")]
    else:
        completed_list = []
    completed_list.append(topic)
    new_completed = ", ".join(completed_list)
    
    # Update the database
    sql_update = """
    UPDATE progress
    SET modules = ?, completed = ?
    WHERE name = ?
    """
    
    cursor.execute(sql_update, (new_modules, new_completed, user))
    conn.commit()
    conn.close()
    
    return f"Topic {topic} moved to completed for {user}"

def update_role(user, role):
    conn = connect_db()
    cursor = conn.cursor()
    
    sql_select = """
    SELECT role 
    FROM progress 
    WHERE name = ?
    """
    
    cursor.execute(sql_select, (user,))
    result = cursor.fetchone()

    if not result:
        print("No record found for the given user.")
        conn.close()
        return

    # Update the database
    sql_update = """
    UPDATE progress
    SET role = ?
    WHERE name = ?
    """
    
    cursor.execute(sql_update, (role, user))
    conn.commit()
    conn.close()
    
    return f"{user} is now a {role}, congrats!"
