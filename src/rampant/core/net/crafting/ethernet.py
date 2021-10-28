"""
Show anything
"""
from scapy.all import Ether, IP

class Ethernet:
    """
    Show anything
    """
    def __init__(self, /, src: str = '00:00:00:00:00:00', dst: str = None, *, type: int = 60):
        self.src = src
        self.dst = dst
        self.type = type
        #self.layer = 'Datalink'
        #self.id = 'Ethernet'
        self.ethernet()

    def ethernet(self):
        self.packet = Ether(**self.__dict__)
        return self.packet

    def __truediv__(self, other):
        return Ether(**self.__dict__) / eval(f'{other.__class__.__name__}(**other.__dict__)')

    def show(self):
        self.packet.show()

    def __lshift__(self, kind):
        #self.kind = kind
        return self.packet / eval(f'{kind.__class__.__name__}(**kind.__dict__)')

    def __getitem__(self, item):
        return self.__dict__[item]

    def to_dict(self):
        print("HOLA")
        #self.kind = self.kind.__dict__
        return self.__dict__
