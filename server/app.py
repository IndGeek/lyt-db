from fastapi import FastAPI, HTTPException
from db_engine.storage import StorageEngine

app = FastAPI()

db_engine = StorageEngine()

@app.post("/create/{db_name}")
async def create_database(db_name: str):
    if db_engine.create_database(db_name):
        return {"message": f"Database '{db_name}' created successfully."}
    raise HTTPException(status_code=400, detail=f"Database '{db_name}' already exists.")

@app.get("/read/{db_name}")
async def read_database(db_name: str):
    data = db_engine.read_database(db_name)
    if data is not None:
        return {"data": data}
    raise HTTPException(status_code=404, detail=f"Database '{db_name}' not found.")

@app.post("/write/{db_name}")
async def write_to_database(db_name: str, data: dict):
    if db_engine.write_to_database(db_name, data):
        return {"message": f"Data written to '{db_name}' successfully."}
    raise HTTPException(status_code=404, detail=f"Database '{db_name}' not found.")
