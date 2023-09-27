import psycopg2.pool

# Create a connection pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=5,
    dbname='your_database',
    user='your_username',
    password='your_password',
    host='your_host'
)

# Define a context manager for database connections
class DatabaseConnection:
    def __enter__(self):
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        # Commit and close the cursor
        self.cursor.close()
        
        # If there was an exception, roll back the transaction
        if exc_type is not None:
            self.connection.rollback()
        else:
            self.connection.commit()

        # Return the connection to the pool
        connection_pool.putconn(self.connection)

# Usage of the context manager
with DatabaseConnection() as cursor:
    # Execute SQL queries here
    cursor.execute("SELECT * FROM your_table")
    result = cursor.fetchall()

# The connection is automatically returned to the pool when the context is exited
