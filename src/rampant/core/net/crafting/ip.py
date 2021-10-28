"""
Show anything
"""
from scapy.all import IP as ips


class IP:
    """
    Show anything
    """
    def __init__(self,
                 /,
                 src: str = '127.0.0.1',
                 dst: str = '8.8.8.8',
                 *,
                 ttl: int = 60):
        self.src = src
        self.dst = dst
        self.ttl = ttl
        #self.layer = 'Network'
        #self.id = 'IP'
        self.ip()

    def ip(self):
        self.packet = ips(**self.__dict__)
        return self.packet

    def show(self):
        self.packet.show()

    def __lshift__(self, kind):
        #self.kind = kind
        return ips(**self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[item]

    def to_dict(self):
        #self.kind = self.kind.__dict__
        return self.__dict__
