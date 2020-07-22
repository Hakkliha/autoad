import csv


with open('Modellist.csv', 'r', encoding='utf-8-sig') as csv_file:
	csv_reader = csv.reader(csv_file)

	'''for line in csv_reader:
			print(line)'''

	with open('new_modellist_brands.py', 'w') as new_file:
		csv_writer = new_file
		for line in csv_reader:
				if line[0] == ';':
					csv_writer.write('\n')
				elif line[0] != '':
					csv_writer.write(line[0].upper().replace(' ', '') + '_MODEL_LIST = (')		


with open('Modellist.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	with open('new_modellist.py', 'w') as new_file:
		csv_writer = new_file
		for line in csv_reader:
				if line[1] == '':
					csv_writer.write(')\n')
				else:
					csv_writer.write('((\'' + line[1] + '\'), (\'' + line[1] + '\')), ')

g = open('new_modellist_brands.py', 'r').readlines()
f = open('new_modellist.py', 'r').readlines()


with open('model_list_file.py', 'w') as new_file:
	for i, line in enumerate(g):
		new_file.write(f'{g[i]} {f[i]}')

