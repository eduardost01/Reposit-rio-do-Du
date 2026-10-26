from lista import ListaEncadeada
from pilha import Pilha
from fila import Fila

print("testando a lista encadeada")
l1 = ListaEncadeada()
l1.adicionar(10)
l1.adicionar(5)
l1.adicionar(20)
l1.adicionar(15)

print("lista original:")
l1.imprimir()

print("Menor elemento (min):", l1.min())
print("Maior elemento (max):", l1.max())
print("Soma dos elementos (sum):", l1.sum())
print("Média dos elementos (avg):", l1.avg())
print("Total de elementos (len):", l1.len())

print("\ntestando o append")
l2 = ListaEncadeada()
l2.adicionar(30)
l2.adicionar(40)
l1.append(l2)
l1.imprimir()

print("\ntestando revers")
l1.reverse()
print("Lista invertida:")
l1.imprimir()


print("\ntestando a pilha")
p = Pilha()
p.empilhar(5)
p.empilhar(10)
p.empilhar(5)
p.empilhar(20)
p.empilhar(10)

print("Pilha inicial:")
p.imprimir()

print("buscando o elemento 20:", p.buscar(20))
print("editando o elemento 20 para 99...")
p.editar(20, 99)
p.imprimir()

print("removendo o elemnto 99:")
p.remover(99)
p.imprimir()

print("removendo valores repetidos")
p.remover_repetidos()
p.imprimir()


print("\ntestando a fila")
f = Fila()
f.enfileirar(3)
f.enfileirar(7)
f.enfileirar(3)
f.enfileirar(9)

print("Fila inicial:")
f.imprimir_fila()

print("Buscando o elemento 7 na fila:", f.buscar(7))
print("Editando o 7 para 50 na fila...")
f.editar(7, 50)
f.imprimir_fila()

print("Removendo o elemento repetido (3):")
f.remover(3)
f.imprimir_fila()

print("Removendo todos os repetidos restantes:")
f.remover_repetidos()
f.imprimir_fila()
