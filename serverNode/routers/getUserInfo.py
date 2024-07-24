from fastapi import APIRouter, HTTPException
import pandas as pd
from schemas.userData import User, Users
users = pd.read_json("config/app/users.json")
router = APIRouter(prefix="/users", tags=["GetUserInfo"])


@router.get("/get-user-by-uuid", response_model=User)
async def get_user_by_uuid(uuid: str):
    for index, row in users.iterrows():
        if row['uuid'] == uuid:
            return row.to_dict()
    raise HTTPException(status_code=404, detail="User not found")


@router.get("/get-user-by-username", response_model=User)
async def get_user_by_username(username: str):
    for index, row in users.iterrows():
        if row['username'] == username:
            return row.to_dict()
    raise HTTPException(status_code=404, detail="User not found")


@router.get("/get-users-by-status", response_model=Users)
async def get_users_by_status(status: str):
    return users[users['status'] == status].to_dict()


@router.get("/get-users-by-job-title", response_model=Users)
async def get_users_by_job_title(job_title: str):
    return users[users['job']['title'] == job_title].to_dict()


@router.get("/get-users-by-job-area", response_model=Users)
async def get_users_by_job_area(job_area: str):
    return users[users['job']['area'] == job_area].to_dict()


@router.get("/get-users-by-job-type", response_model=Users)
async def get_users_by_job_type(job_type: str):
    return users[users['job']['type'] == job_type].to_dict()


@router.get("/get-users-by-job-company", response_model=Users)
async def get_users_by_job_company(job_company: str):
    return users[users['job']['company'] == job_company].to_dict()


@router.get("/get-users-by-name", response_model=Users)
async def get_users_by_name(name: str):
    return users[users['name']['first'] == name].to_dict()


@router.get("/get-users-by-last-name", response_model=Users)
async def get_users_by_last_name(last_name: str):
    return users[users['name']['last'] == last_name].to_dict()


@router.get("/get-users-by-email", response_model=Users)
async def get_users_by_email(email: str):
    return users[users['email'] == email].to_dict()


@router.get("/get-user-by-phone-number", response_model=Users)
async def get_user_by_phone_number(phone_number: str):
    for index, row in users.iterrows():
        if row['phoneNumber'] == phone_number:
            return row.to_dict()
    raise HTTPException(status_code=404, detail="User not found")
