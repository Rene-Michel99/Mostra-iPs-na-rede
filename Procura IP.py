import os
import socket

name=socket.gethostname()
machine_ip=socket.gethostbyname(name)

def get_begin():
    inicio=machine_ip[::-1]
    inicio=inicio[:inicio.find('.')]
    inicio=int(inicio[::-1])
    return inicio

def create_ip():
    tr=machine_ip[0:10]
    
    inicio=get_begin()
    
    ip=[]
    for i in range(inicio,255):
        x=tr+str(i)
        ip.append(x)
    return ip

def create_base():
    base=[]
    tr='tracert '
    ip=machine_ip[0:10]
    
    inicio=get_begin()
    
    for i in range(inicio,255):
        x=ip+str(i)
        base.append(tr+x)
    return base

def busca_parcial():
    ip=create_ip()
    base=create_base()
    print('iniciando busca parcial...')
    cont=0
    for i in range(0,len(ip)):
        info=os.popen(base[i],'r',1).read()
        if info.find('destino')==-1:
            if ip[i]==machine_ip:
                print('ip',ip[i],'na rede','(Você)')
            else:
                print('ip',ip[i],'na rede')
            cont=0
        else:
            cont+=1
        if cont==10:
            print('encerrado')
            break
        info=''

def busca_completa():
    ip=create_ip()
    base=create_base()
    print('iniciando busca completa...')
    for i in range(0,len(ip)):
        info=os.popen(base[i],'r',1).read()
        if info.find('destino')==-1:
            if ip[i]==machine_ip:
                print('ip',ip[i],'na rede','(Você)')
            else:
                print('ip',ip[i],'na rede')
        else:
            print('ip',ip[i],'não esta na rede')
        info=''

option=str(input('digite parcial ou completa para busca: '))
if option=='parcial':
    busca_parcial()
else:
    busca_completa()
