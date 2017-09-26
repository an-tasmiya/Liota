import socket
import matplotlib.pyplot as plt
import csv

s = socket.socket()
port = 2021
s.bind(('', port))
s.listen(5)
my_list = []
i=0
x = []
y = []
print "Server listening on", port
count=0
while True:
    c, addr = s.accept()
    print "Got connection from", addr
    while True:
	data=c.recv(1000)
        #print (c.recv(1000))
	p=data.split(' ')
	print p[1]
	count=count+1
	my_list.append(p[1])
	if(count==10):
		break
    break
	

for val in my_list:#this part in datacenter
		print val
		print i
        	x.append(int(i))
        	y.append(float(val))
		i=i+1

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('Classes')
plt.ylabel('Probabilities')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()


