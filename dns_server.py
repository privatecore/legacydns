import logging
import threading
from dnslib import QTYPE, RR, A
from dnslib.server import DNSServer
from ipaddress import ip_address

SLD = "visibleip.com."
IPS = ["::1", "127.0.0.1"]

def start_dns_server(ip):
    server = DNSServer(dns_resolver(), port=53, address=ip, tcp=False)
    logging.info(f"Starting DNS server on {ip}:53")
    server.start()

class dns_resolver:
    def resolve(self, request, handler):
        reply = request.reply()
        for question in request.questions:
            if question.qtype == QTYPE.A and question.qname.matchSuffix(SLD):
                rr = create_a_record(str(question.qname))
                if rr: reply.add_answer(rr)

        return reply

def create_a_record(query_name):
    octets = query_name.split(".")
    try:
        ip = get_ip_from_query(octets)
        return RR(
            rname=query_name,
            rtype=QTYPE.A,
            rclass=1,
            ttl=0,
            rdata=A(ip)
        )
    except ValueError as e:
        logging.error(e)
        return None

def get_ip_from_query(octets):
    if len(octets) < 5:
        raise ValueError("Invalid query format")

    ip_str = ".".join(octets[:4])
    ip = ip_address(ip_str)
    return str(ip)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    threads = []
    for ip in IPS:
        thread = threading.Thread(target=start_dns_server, args=(ip,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
