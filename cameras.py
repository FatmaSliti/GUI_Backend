from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import yaml

router = APIRouter()

class FormData(BaseModel):
    camera_name: str
    camera_id: str
    camera_ip: str
    camera_port: str
    camera_model: str
    soft_trigger: str
    category: str
    linked_lane: str
    username: str 
    password: str

@router.post("/submit-cameras-form")
async def submit_form(data: FormData):
    try:
        if not all(data.dict().values()):
            raise HTTPException(status_code=422, detail="All fields are required")
        
        yaml_data = yaml.dump(data.dict())

        with open("data.yaml", "a") as file:
            file.write(yaml_data)

        return {"message": "Form data stored successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
