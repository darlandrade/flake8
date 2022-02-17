from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO
from typing import Dict, List, Union


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f"{CODIGO_PRIORITARIO}{self.codigo}"

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Cliente {cliente_atual}\nDirija-se ao caixa {caixa}"

    def estatistica(self, dia: str, agencia: int, flag: str):
        estatistica: Dict[str, Union[str, List[str], int]] = {}
        if flag != "detail":
            estatistica = {f"{agencia}-{dia}": len(self.clientes_atendidos)}
        else:
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes_atendidos'] = self.clientes_atendidos
            estatistica['quantidade_de_clientes_atendidos'] = len(self.clientes_atendidos)

        return estatistica
