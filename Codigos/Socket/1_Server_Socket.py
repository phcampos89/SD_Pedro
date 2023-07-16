import socket

def main():
    # Endereço IP e porta do servidor
    server_ip = "127.0.0.1"  # Pode ser alterado para um endereço IP específico ou deixado como "localhost"
    server_port = 12346  # Pode ser alterado para uma porta disponível

    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincula o socket a um endereço IP e porta
    server_socket.bind((server_ip, server_port))

    # Escuta por conexões
    server_socket.listen(1)
    print("Aguardando conexões...")

    while True:
        # Aceita uma nova conexão
        client_socket, client_address = server_socket.accept()
        print("Conexão estabelecida com:", client_address)

        # Recebe dados do cliente
        data = client_socket.recv(1024)
        print("Dados recebidos do cliente:", data.decode())

        # Envia uma resposta ao cliente
        response = "Olá, cliente!"
        client_socket.sendall(response.encode())

        # Fecha a conexão com o cliente
        client_socket.close()

if __name__ == "__main__":
    main()

