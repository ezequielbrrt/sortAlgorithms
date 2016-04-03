#! /bin/python
# -*- coding: utf-8 -*-


def insertionSort(arreglo):
	if len(arreglo) <= 1:
		print "El arreglo ya está ordenado"
		return
	for x in range(1,len(arreglo)):
		key = arreglo[x]
		indice = x 
		while indice > 0 and key < arreglo[indice - 1] :
			arreglo[indice] = arreglo[indice-1]
			indice = indice-1
		arreglo[indice] = key
	return arreglo	
		
