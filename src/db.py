"""
Helper module for connecting to the sqlite3 db
"""
import sqlite3

def connect_db():
    """
    Simply creates a connection to the db
    """
    return sqlite3.connect("devops.db")
