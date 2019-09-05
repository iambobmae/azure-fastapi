from fastapi import FastAPI
import uvicorn

from api.api_v1.api import api_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        app,
        # access_log=False,
        # port=5000,
        debug=True,
        reload=True
    )