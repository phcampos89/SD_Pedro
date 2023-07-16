# Comando para iniciar servidor proxy de nomes (Caso tenha falha em localizar o nameserver)
# python -m Pyro4.naming

#Biblioteca do Phyton para usar RMI, não possui RMI nativo
import Pyro4

@Pyro4.expose
class RemoteMath(object):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


# Configura o servidor
daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(RemoteMath)
ns.register("math.server", uri)

print("Servidor URI:", uri)
print("Servidor NS:", ns)
print("Servidor RMI INICIADO!")

# Inicia o loop de atendimento
daemon.requestLoop()
