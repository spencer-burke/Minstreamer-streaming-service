from fastapi import APIRouter 

router = APIRouter(
    prefix="/test",
    tags=["test"],
    dependencies=[],
    responses={404: {"description": "Not found"}}
)

@router.get("/hello")
async def test():
    return {"message": "hello world"}
