from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from routers import API

app = FastAPI()
app.include_router(API.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0",
                reload=True, port=3000, log_level="debug",)
