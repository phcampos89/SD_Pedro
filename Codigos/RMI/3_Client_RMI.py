import Pyro4

# Localiza o objeto remoto
math_server = Pyro4.Proxy("PYRONAME:math.server")

# Invoca os métodos remotos
a = 5
b = 3
soma = math_server.add(a, b)
print("Soma:", soma)

subtracao = math_server.subtract(a, b)
print("Subtração:", subtracao)

print("Info Objeto Remoto", math_server)