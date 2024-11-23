from fastapi import APIRouter, HTTPException
from db_engine.storage import StorageEngine

router = APIRouter()
storage = StorageEngine()

@router.post("/create/{db_name}")
async def create_database(db_name: str):
    try:
        storage.save(db_name, {})
        return {"message": f"Database '{db_name}' created successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/read/{db_name}")
async def read_database(db_name: str):
    try:
        data = storage.load(db_name)
        return {"db_name": db_name, "data": data}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Database not found.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
