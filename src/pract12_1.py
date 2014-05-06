#!encoding: UTF-8
#!/usr/bin/python

import platform
import os

def SOFTinfo():
	softinfo={}
	softinfo={'Several':platform.uname() , 'S.O':platform.platform(), 'Pythons Version' :platform.python_version() , 'Date' :platform.python_build()}
	return softinfo

def CPUinfo():
# infofile on Linux machines:
	infofile = '/proc/cpuinfo'
	cpuinfo = {}
	if os.path.isfile(infofile):
		f = open(infofile, 'r')
		for line in f:
			try:
				name, value = [w.strip() for w in line.split(':')]
			except:
				continue
			if name == 'model name':
				cpuinfo['CPU type'] = value
			elif name == 'cache size':
				cpuinfo['cache size'] = value
			elif name == 'cpu MHz':
				cpuinfo['CPU speed'] = value + ' Hz'
			elif name == 'vendor_id':
				cpuinfo['vendor ID'] = value
		f.close()
	return cpuinfo

if __name__ == '__main__':
	softinfo = SOFTinfo()
	for keys in softinfo.keys():
		print softinfo[keys]
	cpuinfo = CPUinfo()
	for keys in cpuinfo.keys():
		print cpuinfo[keys]
  
	print "Introduzca el nombre del fichero para almacenar los resultados:"
	nombre_fichero = raw_input ();
	f = open(nombre_fichero,"w")
	for keys in softinfo.keys():
		if type (softinfo[keys]) is list:
			f.write('\n'.join(softinfo[keys]))
		else:
			f.write(str(softinfo[keys]))
			f.write('\n')
	for keys in cpuinfo.keys():
		if type (cpuinfo[keys]) is list:
			f.write('\n'.join(cpuinfo[keys]))
		else:
			f.write(str(cpuinfo[keys]))
			f.write('\n')
	f.close()


