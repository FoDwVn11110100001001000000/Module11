from fastapi import APIRouter

from api.contact import router as contact_router

router = APIRouter(prefix="/v1")

router.include_router(contact_router)