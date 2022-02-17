from abc import abstractmethod, ABCMeta
from typing import List

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=ABCMeta):
    codigo = 0
    fila: list = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def insere_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    @abstractmethod
    def gera_senha_atual(self) -> None:
        ...

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    @abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        ...
