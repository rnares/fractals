import matplotlib.pyplot as plt


def fractal(x,y,size,depth=1):
	rectangle = plt.Rectangle((x+size,y+size), size, size, fc='black',ec="black")
	plt.gca().add_patch(rectangle)
	#if size/3<0.02:	return 0
	if depth>max_depth:	return 0
	if depth==2 or depth==3:	print(depth)
	depth +=1

	squares = [[x+size*i,y+size*j] for i in range(0,3) for j in range(0,3)]
	size /= 3
	for coord in squares:
		#print(size)
		fractal(coord[0],coord[1],size,depth)
		#rectangle = plt.Rectangle((coord[0],coord[1]), size, size, fc='black',ec="black")
		#plt.gca().add_patch(rectangle)	


plt.axes()
rectangle = plt.Rectangle((0,0), 9, 9, fc='blue',ec="red")
plt.gca().add_patch(rectangle)
plt.axis('scaled')
plt.axis('off')

max_depth=5
fractal(0,0,3)
plt.show()