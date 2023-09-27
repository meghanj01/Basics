from contextlib import contextmanager
import psycopg2.pool


# Create a connection pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=5,
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="your_host",
)


# Define a context manager for the connection pool
@contextmanager
def get_db_connection():
    """_summary_

    Yields:
        _type_: _description_
    """
    connection = connection_pool.getconn()
    try:
        yield connection
    finally:
        connection_pool.putconn(connection)


# Example of using the context manager
with get_db_connection() as conn:
    cursor = conn.cursor()
    # Execute SQL queries here
    cursor.close()

# Connection is automatically returned to the pool when the 'with' block exits
