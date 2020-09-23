# -*- coding: utf-8 -*-
from random import randint
from random import seed
import timeit
import time

#Implemente uma função que receba uma lista de inteiros e ordena essa lista utilizando o Bubble Sort
def bubblesort(l):
  for _ in range(len(l)):
    for j in range(len(l) - 1):
      if l[j] > l[j+1]:
        l[j], l[j+1] = l[j+1], l[j]

#Escreva um programa que gere uma lista com 10.000 números inteiros 
# (gerados randomicamente no intervalo entre 1 e 10.000)
def gerarListaAleatoria(l):
    seed(1)
    for _ in range(10000):
        value = randint(1, 10000)
        l.append(value)

#Implementação do Quick Sort
def partition(l, inicio, fim):
    pivot = l[inicio]
    menor = inicio + 1
    maior = fim

    while True:
      while menor <= maior and l[maior] >= pivot:
        maior = maior - 1
      while menor <= maior and l[menor] <= pivot:
        menor = menor + 1
      if menor <= maior:
        l[menor], l[maior] = l[maior], l[menor]
      else:
        break
    l[inicio], l[maior] = l[maior], l[inicio]
    return maior

def quicksort(l, inicio, fim):
    if inicio >= fim:
        return
    p = partition(l, inicio, fim)
    quicksort(l, inicio, p-1)
    quicksort(l, p+1, fim)


l = []
#gerarListaAleatoria(l)
#print('lista com números aleatórios preenchidos: ')
#print(l)

#bubblesort(l)
#print('lista com números ordenados usando bubble sort: ')
#print(l)

#quicksort(l, 0, len(l) - 1)
#print('lista com números ordenados usando quick sort: ')
#print(l)

#Computar o tempo gasto para ordenar a lista usando o Bubble sort
gerarListaAleatoria(l)
inicio_bubble = timeit.default_timer()
bubblesort(l)
fim_bubble = timeit.default_timer()
#Imprimir os resultados obtidos, em milisegundos
print('Tempo gasto em Bubble Sort foi de:', (fim_bubble - inicio_bubble) * 1000, 'milisegundos')
#Computar o tempo gasto para ordenar a lista usando o Quicksort
gerarListaAleatoria(l)
inicio_quick = timeit.default_timer()
quicksort(l, 0, len(l) - 1)
fim_quick = timeit.default_timer()
#Imprimir os resultados obtidos, em milisegundos
print('Tempo gasto foi em Quick Sort de:', (fim_quick - inicio_quick) * 1000, 'milisegundos')

