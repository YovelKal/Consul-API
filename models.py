class StatusModel:
    def __init__(self, status, message):
        self.status = status
        self.message = message


class SummaryModel:
    def __init__(self, registered_nodes, registered_services, leader, cluster_protocol):
        self.registered_nodes = registered_nodes
        self.registered_services = registered_services
        self.leader = leader
        self.cluster_protocol = cluster_protocol


class MembersModel:
    def __init__(self, registered_nodes):
        self.registered_nodes = registered_nodes


class SystemInfo:
    def __init__(self, vCpus, MemoryGB, disk_usage, network_usage, system_uptime, processes):
        self.vCpus = vCpus
        self.MemoryGB = MemoryGB
        self.disk_usage = disk_usage
        self.network_usage = network_usage
        self.system_uptime = system_uptime
        self.processes = processes
