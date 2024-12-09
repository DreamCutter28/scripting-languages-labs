import socket


def start_udp_client():
    """
    Функция запуска UDP клиента, который отправляет датаграмму серверу
    и получает ответ.
    """
    # Создаем UDP сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Параметры сервера
    host = '127.0.0.1'
    port = 12346

    try:
        # Отправляем сообщение
        message = "Привет, UDP Сервер!"
        client_socket.sendto(message.encode(), (host, port))
        print(f"[*] Отправлено: {message}")

        # Получаем ответ
        data, _ = client_socket.recvfrom(1024)
        response = data.decode()
        print(f"[*] Получено: {response}")

    except Exception as e:
        print(f"[!] Ошибка клиента: {e}")
    finally:
        # Закрываем клиентский сокет
        client_socket.close()


if __name__ == "__main__":
    start_udp_client()
