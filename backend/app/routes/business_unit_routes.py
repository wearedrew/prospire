from fastapi import APIRouter

router = APIRouter()

@router.get("/business_units")
async def get_business_units():
    return {"message": "Business units endpoint working"}