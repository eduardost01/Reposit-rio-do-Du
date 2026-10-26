from node import Node

class ListaEncadeada:
    def __init__(self):
        self.inicio = None  # A lista começa vazia

    # Método tradicional para adicionar no final
    def adicionar(self, dado):
        novo_no = Node(dado)
        if self.inicio is None:
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no

    # --- 1. EXERCÍCIOS DE PERCURSO EM LISTA ---

    def min(self):
        if self.inicio is None:
            return None
        
        menor = self.inicio.dado
        atual = self.inicio.proximo
        while atual is not None:
            if atual.dado < menor:
                menor = atual.dado
            atual = atual.proximo
        return menor

    def max(self):
        if self.inicio is None:
            return None
        
        maior = self.inicio.dado
        atual = self.inicio.proximo
        while atual is not None:
            if atual.dado > maior:
                maior = atual.dado
            atual = atual.proximo
        return maior

    def sum(self):
        soma = 0
        atual = self.inicio
        while atual is not None:
            soma = soma + atual.dado
            atual = atual.proximo
        return soma

    def avg(self):
        total_elementos = self.len()
        if total_elementos == 0:
            return 0
        soma_total = self.sum()
        return soma_total / total_elementos

    def len(self):
        contador = 0
        atual = self.inicio
        while atual is not None:
            contador = contador + 1
            atual = atual.proximo
        return contador

    # --- 2. EXERCÍCIOS GERAIS DE LISTA ---

    def append(self, outra_lista):
        if outra_lista.inicio is None:
            return

        if self.inicio is None:
            self.inicio = outra_lista.inicio
            return

        atual = self.inicio
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = outra_lista.inicio

    def reverse(self):
        anterior = None
        atual = self.inicio
        
        while atual is not None:
            proximo_seguinte = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo_seguinte
            
        self.inicio = anterior

    def imprimir(self):
        elementos = []
        atual = self.inicio
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        print(" -> ".join(elementos))
