"""
Show
"""
from rampant import Rampant
#from scapy.all import Ether, IP

ramp = Rampant()
ramp.SCANNER = 'shoddan'

scanner = ramp.net.Scanner(scanner=ramp.SCANNER)

#result = scanner.run_scan('127.0.0.1', port_min=20, port_max=8080, arguments='-sV -Pn', superuser=False)
#print(result)

print("-"*60)
info = scanner.scan_info()
print(info)

r = Ether(src='00:11:22:33:44:55', dst='00:00:00:00:00:00') / IP(dst='8.8.8.8', src='34.234.121.59', ttl=100)


#scanner.save_json('salida')
#scanner.save_csv('salida', delimiter=';')
#scanner.save('salida', extension='txt')
