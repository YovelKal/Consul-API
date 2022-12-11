import uvicorn
from fastapi import FastAPI
from services import Services


app = FastAPI()


@app.get("/v1/api/consulCluster/status")
def get_status():
    return Services.consul_status()


@app.get("/v1/api/consulCluster/summary")
def consul_summary():
    return Services.consul_summary()


@app.get("/v1/api/consulCluster/members")
def consul_members():
    return Services.consul_members()


@app.get("/v1/api/consulCluster/systemInfo")
def consul_system_info():
    return Services.consul_system_info()


if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)