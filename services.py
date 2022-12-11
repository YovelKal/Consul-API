import requests
from config import Consts, Messages
from consul_services import ConsulServices
from models import StatusModel, SystemInfo
from parsers import SummaryParser, MembersParser
import psutil

class Services:
    def consul_status():
        try:
            ConsulServices.ping()
            return StatusModel(status=Consts.STATUS_RUNNING, message=Messages.CONSUL_RUNNING)

        except requests.exceptions.RequestException as e:
            return StatusModel(Consts.STATUS_NOT_RUNNING, f"{Messages.CONSUL_NOT_RUNNING}: {e}")

    def consul_summary():

        summary_parser = SummaryParser(nodes_res=ConsulServices.get_nodes(),
                                       services_res=ConsulServices.get_services(),
                                       leader_res=ConsulServices.get_leader(),
                                       protocol_res=ConsulServices.get_cluster_protocol())

        return summary_parser.parse()

    def consul_members():

        members_parser = MembersParser(nodes_res=ConsulServices.get_nodes())

        return members_parser.parse()

    def consul_system_info():

        bytes_to_GB_factor = 1073741824

        vCpus = psutil.cpu_count()
        MemoryGB = psutil.virtual_memory().total / bytes_to_GB_factor
        disk_total = psutil.disk_usage('/')[0] / bytes_to_GB_factor
        disk_used = psutil.disk_usage('/')[1] / bytes_to_GB_factor
        disk_usage = f"{disk_used} / {disk_total}"
        network_usage = f"Number of GB sent: {psutil.net_io_counters()[0] / bytes_to_GB_factor}" \
                        f" Number of GB received: {psutil.net_io_counters()[1] / bytes_to_GB_factor}"
        system_uptime = f"{psutil.boot_time() / 360} Hours"
        processes = len(psutil.pids())

        return SystemInfo(vCpus=vCpus,
                          MemoryGB=MemoryGB,
                          disk_usage=disk_usage,
                          network_usage=network_usage,
                          system_uptime=system_uptime,
                          processes=processes)
