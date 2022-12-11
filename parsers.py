from models import SummaryModel, MembersModel


class SummaryParser:
    def __init__(self, nodes_res, services_res, leader_res, protocol_res):
        self._node_res = nodes_res
        self._services_res = services_res
        self._leader_res = leader_res
        self.protocol_res = protocol_res

    def parse(self):
        return SummaryModel(registered_nodes=self._nodes_num(),
                            registered_services=self._services_num(),
                            leader=self._leader(),
                            cluster_protocol=self._protocol())

    def _nodes_num(self):
        try:
            return len(self._node_res.json())
        except:
            return 0

    def _services_num(self):
        try:
            return len(self._services_res.json())
        except:
            return 0

    def _leader(self):
        try:
            return self._leader_res.content
        except:
            return "No leader"

    def _protocol(self):
        try:
            return self.protocol_res.json()["Member"]["ProtocolCur"]
        except:
            return "No protocol"


class MembersParser:
    def __init__(self, nodes_res):
        self._node_res = nodes_res

    def parse(self):
        return MembersModel(registered_nodes=self._nodes())

    def _nodes(self):
        nodes_names = []
        try:
            nodes = self._node_res.json()
            for node in nodes:
                nodes_names.append(node["Node"])
            return nodes_names
        except:
            return 0


