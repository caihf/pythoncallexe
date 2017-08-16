#!/usr/bin/env python 

import subprocess

proc = subprocess.Popen(['test.exe'], stdout=subprocess.PIPE)
while True:
	line = proc.stdout.readline()
        if "OverTime: time limit" in line:
		print "will kill the process of test.exe"
		# f: forced to kill the process  im: image name(specifies the image name of the process to be terminated)
		#os.system("taskkill /f /im testKillProcess.exe")  
		proc.kill()
		
		print "to modify  parameter of inputdata.txt file"
		f = open("inputdata.txt", "r")
		lines= f.readlines()
		f.close()
		num = int(lines[-1])
		lines[-1] = str(num - 5)
		f = open("inputdata.txt", "w")
		f.writelines(lines)
		f.close()
		
		print "will start testKillProcess.exe"
		subprocess.call(['test.exe'])
		proc = subprocess.Popen(['test.exe'], stdout=subprocess.PIPE)
	if line != '':
		print "python: ", line.rstrip()
	else:
		break
