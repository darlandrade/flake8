from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila

# fila_teste = FilaNormal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
#
# print(fila_teste.chama_cliente(4))
# print(fila_teste.chama_cliente(2))
#
# fila_teste2 = FilaPrioritaria()
# fila_teste2.atualiza_fila()
# fila_teste2.atualiza_fila()
# fila_teste2.atualiza_fila()
# fila_teste2.atualiza_fila()
#
# print(fila_teste2.chama_cliente(8))
# print(fila_teste2.chama_cliente(5))
# print(fila_teste2.estatistica("17/02/2022", 1988, 'detail'))

teste_fila = FabricaFila.pega_fila('N')
teste_fila.atualiza_fila()
teste_fila.atualiza_fila()
teste_fila.atualiza_fila()

print(teste_fila.chama_cliente(5))
