from node import Node

class Pilha:
    def __init__(self):
        self.topo = None  # Início da pilha (topo)

    def empilhar(self, dado):
        novo_no = Node(dado)
        novo_no.proximo = self.topo
        self.topo = novo_no

    def desempilhar(self):
        if self.topo is None:
            return None
        removido = self.topo
        self.topo = self.topo.proximo
        return removido.dado

    # --- 3. EXERCÍCIOS DE PILHA ---

    def buscar(self, info):
        atual = self.topo
        posicao = 0
        while atual is not None:
            if atual.dado == info:
                return posicao
            atual = atual.proximo
            posicao = posicao + 1
        return -1

    def editar(self, info_antiga, info_nova):
        atual = self.topo
        encontrou = False
        while atual is not None:
            if atual.dado == info_antiga:
                atual.dado = info_nova
                encontrou = True
            atual = atual.proximo
        return encontrou

    def remover(self, info):
        auxiliar = Pilha()
        removeu = False

        while self.topo is not None:
            valor = self.desempilhar()
            if valor == info and not removeu:
                removeu = True
            else:
                auxiliar.empilhar(valor)

        while auxiliar.topo is not None:
            self.empilhar(auxiliar.desempilhar())
            
        return removeu

    def remover_repetidos(self):
        elementos_vistos = []
        auxiliar = Pilha()

        while self.topo is not None:
            valor = self.desempilhar()
            if valor not in elementos_vistos:
                elementos_vistos.append(valor)
                auxiliar.empilhar(valor)

        while auxiliar.topo is not None:
            self.empilhar(auxiliar.desempilhar())

    def imprimir(self):
        atual = self.topo
        print("--- TOPO DA PILHA ---")
        while atual is not None:
            print(f"| {atual.dado} |")
            atual = atual.proximo
        print("---------------------")
