import nmap

print(r"""
███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ███╗ █████╗ ██████╗ 
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗ ████║██╔══██╗██╔══██╗
███████╗██║     ███████║██╔██╗ ██║██╔████╔██║███████║██████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝ 
                    by: Caco Abud                                               
""")

scan = nmap.PortScanner()

print("Bem vindo ao ScanMap, um simples NMAP scan feito para estudar Python e Pentest")
print("---------------------------------------------------------------------------------")

ip_alvo = input("IP Alvo: ")
print("IP a ser escaneado: ", ip_alvo)
type(ip_alvo)

tipo_script = input(""" \nSelecione o método:
                        1) SYN ACK Scan
                        2) UDP Scan
                        3) Comprehensive Scan\n""")
print("Método escolhido: ", tipo_script)

if tipo_script == '1':
    print("Nmap Version: ", scan.nmap_version())
    scan.scan(ip_alvo, '1-1024', '-v -sS')
    print(scan.scaninfo())
    print("IP Status: ", scan[ip_alvo].state())
    print(scan[ip_alvo].all_protocols())
    print("Portas: ", scan[ip_alvo]['tcp'].keys())

elif tipo_script == '2':
    print("Nmap Version: ", scan.nmap_version())
    scan.scan(ip_alvo, '1-1024', '-v -sU')
    print(scan.scaninfo())
    print("IP Status: ", scan[ip_alvo].state())
    print(scan[ip_alvo].all_protocols())
    print("Portas: ", scan[ip_alvo]['udp'].keys())

elif tipo_script == '3':
    print("Nmap Version: ", scan.nmap_version())
    scan.scan(ip_alvo, '1-1024', '-v -sS -sV -sC -A -O')
    print(scan.scaninfo())
    print("IP Status: ", scan[ip_alvo].state())
    print(scan[ip_alvo].all_protocols())
    print("Portas: ", scan[ip_alvo]['udp'].keys())

elif tipo_script >= '4':
    print("Escolha uma opção válida: ")