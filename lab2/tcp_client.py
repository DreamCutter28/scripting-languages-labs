import socket


def start_tcp_client():
    """
    Функция запуска TCP клиента, который отправляет сообщение серверу
    и получает ответ.
    """
    # Создаем TCP сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Параметры сервера
    host = '127.0.0.1'
    port = 12345
    
    try:
        # Подключаемся к серверу
        client_socket.connect((host, port))
        print(f"[*] Подключено к серверу {host}:{port}")
        
        # Отправляем сообщение
        message = "Привет, TCP Сервер!"
        client_socket.send(message.encode())
        print(f"[*] Отправлено: {message}")
        
        # Получаем ответ
        response = client_socket.recv(1024).decode()
        print(f"[*] Получено: {response}")
        
    except Exception as e:
        print(f"[!] Ошибка клиента: {e}")
    finally:
        # Закрываем клиентский сокет
        client_socket.close()


if __name__ == "__main__":
    start_tcp_client()