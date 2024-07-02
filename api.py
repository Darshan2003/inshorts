from fastapi import APIRouter
from endpoints import (
    users_endp,
    admin_endp
)

router = APIRouter()
router.include_router(users_endp.router)
router.include_router(admin_endp.router)