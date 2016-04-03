#! /usr/bin/python
# -*- coding: utf-8 -*-

import Gnuplot
from tqdm import tqdm

def quickSort(lista):
   quickSortR(lista,0,len(lista)-1)
   return lista

def quickSortR(lista,primero,ultimo):
   if primero<ultimo:
       splitpoint = partir(lista,primero,ultimo)
       quickSortR(lista,primero,splitpoint - 1)
       quickSortR(lista,splitpoint + 1,ultimo)

def partir(lista,primero,ultimo):
   pivote = lista[primero]
   izquierda = primero + 1
   derecha = ultimo
   aux = False
   while not aux:
       while izquierda <= derecha and lista[izquierda] <= pivote:
           izquierda = izquierda + 1
       while lista[derecha] >= pivote and derecha >= izquierda:
           derecha = derecha - 1
       if derecha < izquierda:
           aux = True
       else:
           temp = lista[izquierda]
           lista[izquierda] = lista[derecha]
           lista[derecha] = temp
   temp = lista[primero]
   lista[primero] = lista[derecha]
   lista[derecha] = temp
   return derecha
