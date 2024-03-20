# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class FormData(BaseModel):
#     name: str

# @app.post("/submit-form")
# async def submit_form(data: FormData):
#     with open("data.txt", "a") as file:
#         file.write(data.name + "\n")
#     return {"message": "Form data stored successfully."}


# from fastapi import FastAPI
# from pydantic import BaseModel
# import yaml

# app = FastAPI()

# class FormData(BaseModel):
#     name: str

# @app.post("/submit-form")
# async def submit_form(data: FormData):
#     # Serialize form data to YAML
#     yaml_data = yaml.dump({"name": data.name})

#     # Write YAML data to file
#     with open("data.yaml", "a") as file:
#         file.write(yaml_data)

#     return {"message": "Form data stored successfully."}


from fastapi import FastAPI
from pydantic import BaseModel
import yaml

from cameras import router as cameras_router

app = FastAPI()

app.include_router(cameras_router)

class FormData(BaseModel):
    lane_name: str
    lane_id: str
    lane_type: str
    early_request_timeout: str

@app.post("/submit-form")
async def submit_form(data: FormData):
    # Serialize form data to YAML
    yaml_data = yaml.dump(data.dict())

    # Write YAML data to file
    with open("data.yaml", "a") as file:
        file.write(yaml_data)

    return {"message": "Form data stored successfully."}
