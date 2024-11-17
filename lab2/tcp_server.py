import socket

def start_tcp_server():
    """
    Функция запуска TCP сервера, который принимает сообщения от клиента
    и отправляет их обратно (эхо-сервер).
    """
    
    # Создаем TCP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Параметры подключения
    host = '127.0.0.1'
    port = 12345
    
    try:
        # Привязываем сокет к адресу и порту
        server_socket.bind((host, port))
        
        # Переводим сервер в режим прослушивания (максимум 1 подключение в очереди)        
        server_socket.listen(1)
        print(f"[*] TCP Сервер слушает на {host}:{port}")     
           
        while True:
            # Принимаем подключение от клиента
            client_socket, client_address = server_socket.accept()
            print(f"[+] Принято подключение от {client_address}")
            
            try:
                # Получаем данные от клиента
                data = client_socket.recv(1024).decode()
                print(f"[*] Получено: {data}")
                
                # Отправляем эхо-ответ
                client_socket.send(data.encode())
                print(f"[*] Отправлен эхо-ответ")
                
            except Exception as e:
                print(f"[!] Ошибка при обработке клиента: {e}")
            finally:
                # Закрываем соединение с клиентом
                client_socket.close()
                
    except Exception as e:
        print(f"[!] Ошибка сервера: {e}")
    finally:
        # Закрываем серверный сокет
        server_socket.close()

if __name__ == "__main__":
    start_tcp_server()

