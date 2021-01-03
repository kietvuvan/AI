import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
from sklearn import linear_model

def cost(x):
	m=x_data.shape[0]
	return 0.5/m*np.linalg.norm(x_data.dot(x)-y_data,2)**2

def grad(x):
	m=x_data.shape[0]
	return 1/m*x_data.T.dot(x_data.dot(x)-y_data)

def gradient_descent(x_init,learning_rate,iteration):
	m=x_data.shape[0]
	x_list=[x_init]
	for i in range(iteration):
		x_new=x_list[-1]-learning_rate*grad(x_list[-1])
		if(np.linalg.norm(grad(x_new))/m)<0.3:
			break
		x_list.append(x_new)

	return x_list  #list of b and a coefficient in y=b+ax . x_list=[[a1,b1],[a2,b2]]

x_data=np.array([[2,9,7,9,11,16,25,23,22,29,29,35,37,40,46]]).T
y_data=np.array([[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]).T
ax=plt.axes(xlim=(-10,60),ylim=(-1,20))
plt.plot(x_data,y_data,'ro')
#plt.show()
#create linear regression formular
lr=linear_model.LinearRegression()
lr.fit(x_data,y_data)
x0_gd=np.linspace(1,46,2)
y0_sklearn=lr.intercept_[0]+lr.coef_[0][0]*x0_gd
plt.plot(x0_gd,y0_sklearn)

 #Add ones to x_data
ones=np.ones((x_data.shape[0],1),dtype=np.int8)

x_data=np.concatenate((ones,x_data),axis=1)

# init of a random line
x_init=np.array([[1],[2]])  #init b and a coefficient of y=b+ax
y_init=x_init[0][0]+x_init[1][0]*x0_gd # a=x_init[0][0] and b=x_init[1][0]
plt.plot(x0_gd,y_init)



#gradient descent
iteration=90
learning_rate=0.0001
x_list=gradient_descent(x_init,learning_rate,iteration)
# Draw
x0_gd=np.linspace(1,46,2)
for i in range(len(x_list)):
	y0_list=x_list[i][0]+x_list[i][1]*x0_gd
	plt.plot(x0_gd,y0_list)
print(len(x_list))
plt.show()
# draw cost and interation
cost_list=[]
interation_list=[]
for i in range(len(x_list)):
	interation_list.append(i)
	cost_list.append(cost(x_list[i]))
	plt.plot(interation_list,cost_list)
plt.show()
