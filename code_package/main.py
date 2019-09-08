"""Executable entry point for Task 2"""
import sqlite3
from code_package.database_repository import generate_tables, insert_users_records


def director():
    """Director method for Task 2"""
    conn = sqlite3.connect('user.db')
    generate_tables(conn)
    insert_users_records(conn, 10**7)


try:
    director()
except ValueError as error:
    print('Caught this error: ' + repr(error))
