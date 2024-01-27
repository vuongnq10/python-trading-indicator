from fastapi import APIRouter

router = APIRouter(
  prefix='/add',
  tags = ['addition']
)

@router.get("/")
async def add_root():
  return {"message": "/add root"}

@router.get("/addition")
async def add_addition():
  return {"message": "/add/addition"}