#!/usr/bin/python
#!encoding: UTF-8
import sys 
import modulo
import time
import timeit

argumentos = sys.argv[1:]
if (len(argumentos) == 8):
	n = int (argumentos[0])
	aproximaciones = int (argumentos[1])
	umbral = []
	for i in range (2,7):
		umbral.append(float (argumentos[i]))
	nombre_fichero = argumentos[7]
else:
	print "Introduzca el numero de intervalos (n > 0):"
	n = int (raw_input ());
	print "Introduzca el numero de aproximaciones:"
	aproximaciones = int (raw_input ());
	print "Introduzca 5 umbrales de error:"
	umbral = []
	for i in range (5):
		print "Introduzca el umbral", i, ":"
		umbral.append(float (raw_input ()));
	print "Introduzca el nombre del fichero para almacenar los resultados:"
	nombre_fichero = raw_input ();
if (n > 0):
	try:
		fichero = open (nombre_fichero, "a")
	except:
		fichero = open (nombre_fichero, "w")
	fichero.write ("Nº de intervalos: %d\n" % (aproximaciones))
	for i in range (5):
		start = time.time()
		modulo.error (n, aproximaciones, umbral[i])
		finish = time.time() - start
		t1 = timeit.Timer("modulo.error (n, aproximaciones, umbral)","from __main__ import modulo; n=%d; aproximaciones=%d; umbral=%f" % (n, aproximaciones, umbral[i]))
		print t1.timeit(10)
		fichero.write ("%2.10f\n" % (finish))
	fichero.close ()
else:
	print "El valor de los intervalos debe ser mayor que 0"


