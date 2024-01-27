from fastapi import FastAPI, APIRouter, WebSocket
import sub.sub as sub

app = FastAPI()
router = APIRouter()
app.include_router(sub.router)
app.include_router(router)

@app.get("/")
async def root():
  return {"message": "This is root "}

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  while True:
    data = await websocket.receive_text()
    await websocket.send_text(f"Message text was: {data}")