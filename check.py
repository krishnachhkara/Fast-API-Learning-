from fastapi import FastAPI, HTTPException
from db import get_connection

app = FastAPI()

@app.get("/products")
def get_products():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, price FROM products")
        products = cur.fetchall()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()
