"""Module responsible for all sqlite database operations"""
from code_package.password_generator import generate_password, measure_strength


def insert_users_records(conn, user_count):
    """Generate all user records and insert it tho the database"""
    cursor = conn.cursor()
    result = []
    for _ in range(user_count):
        append_new_user_record(result)
    cursor.executemany('''INSERT INTO USER VALUES (?, ?, ?, ?, ?)''', result)
    conn.commit()


def append_new_user_record(result):
    """Append the user record to the result array."""
    password = generate_password(5)
    strength = measure_strength(password)
    result.append(('Name', 'name@gmail.com', '+42313313', password, strength,))


def generate_tables(conn):
    """Generate starting database tables"""
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS USER (
                    NAME text,
                    EMAIL text,
                    MOBILE_PHONE text,
                    PASSWORD text,
                    PASSWORD_STRENGTH real
                    )
                    """)
    conn.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS ADDRESS (
                    ID integer,
                    STREET_AND_NUMBER text
                    )
                    """)
    conn.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS BUILDING (
                    ID integer,
                    BUILDING_NAME text
                    )
                    """)
    conn.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS COMPANY (
                    ID integer,
                    NAME string                    
                    )
                    """)
    conn.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS SERVICE (
                    ID integer,
                    SERVICE_NAME string                    
                    )
                    """)
    conn.commit()
