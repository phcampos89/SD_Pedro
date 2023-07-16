import xmlrpc.server


# Classe com as funções a serem chamadas remotamente
class MyFunctions:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y


# Inicializa o servidor RPC
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8001))
server.register_instance(MyFunctions())

# Inicia o servidor
print("Servidor em execução...")
server.serve_forever()
