from db import connect_db

def add_column_role():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Add the new column 'role' to the 'progress' table
    cursor.execute("""
    ALTER TABLE progress ADD COLUMN role TEXT;
    """)
    
    conn.commit()
    conn.close()
    print("Column 'role' added to 'progress' table.")

# Run the migration
add_column_role()