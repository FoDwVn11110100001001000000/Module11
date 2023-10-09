from fastapi import APIRouter

router = APIRouter(prefix="/contact")


@router.get("/")
async def list_contact():
    return {}

@router.get("/{contact_id}")
async def get_contact_details(contact_id: int):
    return {"contact_id": contact_id}