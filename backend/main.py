from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_db_connection
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SalesData(BaseModel):
    product: str
    sales: int

@app.get("/sales", response_model=List[SalesData])
async def get_sales_data():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT product, sales FROM sales")
        data = cursor.fetchall()
        return data
    finally:
        cursor.close()
        conn.close()