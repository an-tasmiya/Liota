#!/usr/bin/python

import matplotlib.pyplot as plt
import csv

x = []
y = []
i=0

with open('data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
	arr = row[0].split(',')#send this arr to datacenter
	for val in arr:#this part in datacenter
		print val
		print i
        	x.append(int(i))
        	y.append(int(val))
		i=i+1

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('Classes')
plt.ylabel('Probabilities')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
