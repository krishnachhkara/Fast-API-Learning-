import psycopg2 as ps
from psycopg2.extras import RealDictCursor

def get_connection():
    try:
        connection = ps.connect(
        host="localhost",
        database="fastapi_db",
        user="fastapi_user",
        password="asdf",
        cursor_factory=RealDictCursor
        )
    except Exception as e:
        print(f"You got error {e}")    

    return connection
    
