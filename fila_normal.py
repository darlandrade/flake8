from fila_base import FilaBase
from constantes import CODIGO_NORMAL


class FilaNormal(FilaBase):
    def gera_senha_atual(self):
        self.senha_atual = f"{CODIGO_NORMAL}{self.codigo}"

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Cliente {cliente_atual}\nDirija-se ao caixa {caixa}"
