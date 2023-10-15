from fastapi import FastAPI, HTTPException
import psycopg2

app = FastAPI()

# Define the database connection parameters
db_params = {
    'host': 'postgres-alias',      # Update with your PostgreSQL container IP
    'port': 5432,             # Default PostgreSQL port
    'database': 'postgres',
    'user': 'postgres',
    'password': 'password',
}

def test_db_connection():
    try:
        connection = psycopg2.connect(**db_params)
        connection.close()
        return True
    except Exception as e:
        return False

@app.get("/")
def read_root():
    return {"status": "connected successfully"}

@app.get("/test_db_connection")
def test_database_connection():
    if test_db_connection():
        return {"message": "Database connection successful."}
    else:
        raise HTTPException(status_code=500, detail="Failed to connect to the database.")
