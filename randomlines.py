#! /usr/bin/env python
import random
import sys
def showMessage():
	print('Usage: randomlines.py input_file_name [output_file_name]\n'
		'Options:\n'
		'input_file_name - specify the name of the file you are going to proceed\n'
		'output_file_name - specify the name of the file you want to put the output, if null, the output_file_name = input_filen_name + \'_res\'\n')
if __name__ == '__main__':
	if len(sys.argv) <= 1:
		showMessage()
		exit()
	try:
		fp1=open(sys.argv[1])
	except:
		print('No such file: %s found!' % sys.argv[1])
		exit()
	out = ''
	if len(sys.argv) == 2:
		print('No output_file_name specified, generate ressult into %s_res' % sys.argv[1])
		out = sys.argv[1] + '_res'
	else:
		out = sys.argv[2]
	fp2=open(out,'w')
	list_of_all_lines = fp1.readlines()
	num = len(list_of_all_lines)
	randarry=[0] * num
	for i in range(num):
		index = random.randint(1,num)	
		while index in randarry:
			index = random.randint(1,num)	
		randarry[i] = index
	
	fp1.close()
	for i in range(num):
		fp2.write(list_of_all_lines[randarry[i]-1])
	fp2.close()
	
