import socket
import concurrent.futures

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        
        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"Порт {port} открыт")
        
        sock.close()
    except Exception as e:
        print(f"Ошибка при проверке порта {port}: {e}")

def main():
    host = input("IP-адрес или домен: ")
    ports = range(1, 1025)  
    
    print(f"Сканирование {host}...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_port, host, port)

if __name__ == "__main__":
    main()

