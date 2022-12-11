import requests
from config import Consts


class ConsulServices:

    @staticmethod
    def ping():
        requests.get(url=Consts.CONSUL_URL)

    @staticmethod
    def get_nodes():
        return requests.get(url=f"{Consts.CONSUL_URL}v1/catalog/nodes")

    @staticmethod
    def get_services():
        return requests.get(url=f"{Consts.CONSUL_URL}v1/catalog/services")

    @staticmethod
    def get_leader():
        return requests.get(url=f"{Consts.CONSUL_URL}v1/status/leader")

    @staticmethod
    def get_cluster_protocol():
        return requests.get(url=f"{Consts.CONSUL_URL}v1/agent/self")
