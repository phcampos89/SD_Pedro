import socket

def main():
    # Endereço IP e porta do servidor
    server_ip = "127.0.0.1"  # Pode ser alterado para o endereço IP do servidor desejado
    server_port = 12346  # Pode ser alterado para a porta do servidor desejada

    # Cria um socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conecta ao servidor
        client_socket.connect((server_ip, server_port))
        print("Conectado ao servidor:", server_ip, "porta:", server_port)

        # Envie dados para o servidor
        message = "Olá, servidor!"
        client_socket.sendall(message.encode())

        # Receba a resposta do servidor
        data = client_socket.recv(1024)
        print("Resposta do servidor:", data.decode())

    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor.")

    finally:
        # Fecha a conexão
        client_socket.close()

if __name__ == "__main__":
    main()
