from fastapi import APIRouter 
import boto3

router = APIRouter(
    prefix="/test",
    tags=["test"],
    dependencies=[],
    responses={404: {"description": "Not found"}}
)

@router.get("/hello")
async def test():
    return {"message": "hello world"}

@router.get("/film")
async def test_stream():
    pass