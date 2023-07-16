import xmlrpc.client

# Conecta ao servidor RPC
server = xmlrpc.client.ServerProxy("http://localhost:8001/")

# Chama as funções remotas
result1 = server.add(5, 3)
result2 = server.subtract(10, 7)

# Exibe os resultados
print("Resultado da adição:", result1)
print("Resultado da subtração:", result2)
