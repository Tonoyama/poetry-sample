from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from routers import API
from model.database import create_database, create_session, Product, Engine
import default_value

create_database()
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
    # テーブルの初期値を挿入
    session = create_session()
    if "product" not in Engine.table_names():
        raise "productテーブルは存在しません"
    product = session.query(Product).all()
    if len(product) == 0:
        default_value.create_default_value()
    uvicorn.run(app="main:app", host="0.0.0.0",
                reload=True, port=3000, log_level="debug",)
