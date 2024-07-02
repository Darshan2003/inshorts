from fastapi import APIRouter
from database.schema import CreateShorts
from database.admin_db import create_shorts

router = APIRouter(
    prefix="/api",
    tags=["Admin"]
)

@router.post("/shorts/create")
def post_short(short: CreateShorts):
    sid = create_shorts(short)
    return {"message":"Short added successfully", "short_id": sid, "status_code": 200}