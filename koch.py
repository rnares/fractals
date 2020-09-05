#matplotlib notebook
import matplotlib.pyplot as plt


def koch(x1,y1,x2,y2,depth=1):
	v=[(x2-x1)/3,(y2-y1)/3]
	nodes=[[x1,y1], [x1+v[0],y1+v[1]], [x1+v[0]+0.5*v[0]-(0.5*3**0.5)*v[1],y1+v[1]+0.5*v[1]+(0.5*3**0.5)*v[0]], [x1+2*v[0],y1+2*v[1]],  [x2,y2]]
	depth+=1
	
	if depth==max_depth:
		for i in range(0,4):
			line = plt.Line2D((nodes[i][0], nodes[i+1][0]), (nodes[i][1], nodes[i+1][1]), lw=1.5)
			plt.gca().add_line(line)
		return 0
	else:
		for i in range(0,4):
			koch(nodes[i][0],nodes[i][1],nodes[i+1][0],nodes[i+1][1],depth)
	
	

plt.axes()
rectangle = plt.Rectangle((0,0), 9, 9, fc='red',ec="red")
plt.gca().add_patch(rectangle)
plt.axis('scaled')
plt.axis('off')

max_depth=5
koch(0,3,9,3)
plt.show()