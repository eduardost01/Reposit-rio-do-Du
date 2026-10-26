from node import Node

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, dado):
        novo_no = Node(dado)
        if self.fim is None:
            self.inicio = novo_no
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def desenfileirar(self):
        if self.inicio is None:
            return None
        removido = self.inicio
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        return removido.dado

    # --- 4. EXERCÍCIOS DE FILA ---

    def imprimir_fila(self):
        elementos = []
        atual = self.inicio
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        print("Início -> " + " -> ".join(elementos) + " <- Fim")

    def buscar(self, info):
        atual = self.inicio
        posicao = 0
        while atual is not None:
            if atual.dado == info:
                return posicao
            atual = atual.proximo
            posicao = posicao + 1
        return -1

    def editar(self, info_antiga, info_nova):
        atual = self.inicio
        encontrou = False
        while atual is not None:
            if atual.dado == info_antiga:
                atual.dado = info_nova
                encontrou = True
            atual = atual.proximo
        return encontrou

    def remover(self, info):
        auxiliar = Fila()
        removeu = False

        while self.inicio is not None:
            valor = self.desenfileirar()
            if valor == info and not removeu:
                removeu = True
            else:
                auxiliar.enfileirar(valor)

        while auxiliar.inicio is not None:
            self.enfileirar(auxiliar.desenfileirar())

        return removeu

    def remover_repetidos(self):
        elementos_vistos = []
        auxiliar = Fila()

        while self.inicio is not None:
            valor = self.desenfileirar()
            if valor not in elementos_vistos:
                elementos_vistos.append(valor)
                auxiliar.enfileirar(valor)

        while auxiliar.inicio is not None:
            self.enfileirar(auxiliar.desenfileirar())
