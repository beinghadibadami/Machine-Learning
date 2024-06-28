import numpy as np 
from sklearn import linear_model 

def gradient_decent(x,y):
    m_curr=b_curr=0
    learning_rate=0.0002
    iterations=1000000
    n=len(x)
    for i in range(iterations):
        y_predicted=m_curr*x+b_curr
        cost=(1/n)*sum([val ** 2 for val in (y-y_predicted)])
        md=-(2/n)*sum(x*(y-y_predicted))
        bd=-(2/n)*sum(y-y_predicted)
        m_curr=m_curr-learning_rate*md
        b_curr=b_curr-learning_rate*bd
        print("M {},B {}, iteration {},Cost {}".format(m_curr,b_curr,i,cost))
x=np.array([92,56,88,70,80,49,65,35,66,67])
y=np.array([98,68,81,80,83,52,66,30,68,73])
gradient_decent(x,y)