#! /usr/bin/python
# -*- coding: utf-8 -*-

import math
import insertionSort.insertionSort as insertion 
import mergeSort.mergeSort as merge
import quickSort.quickSort as quick

algoritmo = {
	1 : insertion.insertionSort,
	2 : merge.mergeSort,
	3 : quick.quickSort, 
}

ALGORITMO = 1

def main():
	salir = 0
	valores = []
	while salir != 1:
		try:
			numeros = int(raw_input("Escribe los números: "))
			valores.append(numeros)
	   	except:
	   		print "Iniciando Algoritmo"
	   		salir = 1
	print "Algoritmo: ",algoritmo[ALGORITMO]
	print algoritmo[ALGORITMO](valores)   

main()