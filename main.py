from fastapi import FastAPI
from services import Services


app = FastAPI()


@app.get("/v1/api/consulCluster/status")
def get_status():
    """
    Get the consul server status
    """

    return Services.consul_status()


@app.get("/v1/api/consulCluster/summary")
def consul_summary():
    """
    Sample the consul API and get information
    """

    return Services.consul_summary()


@app.get("/v1/api/consulCluster/members")
def consul_members():
    """
    Get the consul registered nodes by name
    """

    return Services.consul_members()


@app.get("/v1/api/consulCluster/systemInfo")
def consul_system_info():
    """
    Get metrics taken from the docker container
    """

    return Services.consul_system_info()
