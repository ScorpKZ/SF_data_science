import matplotlib.pyplot as plt
import numpy as np

#x=np.linspace(0,2*np.pi,100)
#y=np.sin(x)

#plt.plot(x,y)
#plt.xlabel('Value of x')
#plt.ylabel('Value of y')
#plt.title('Sine Wave')


#plt.show()


list_game3 =[8, 7, 6, 5, 7, 6, 4, 7, 6, 5, 7, 6, 3, 7, 6, 5, 7, 6, 4, 7, 6, 5, 7, 6, 7, 2, 6, 7, 5, 6, 7, 4, 6, 7, 5, 6, 7, 3, 6, 
7, 5, 6, 7, 4, 6, 7, 5, 6, 7, 1, 7, 6, 5, 7, 6, 4, 7, 6, 5, 7, 6, 3, 7, 6, 7, 5, 6, 7, 4, 6, 7, 5, 6, 7, 2, 7, 6, 5, 7, 6, 4, 7, 6, 5, 7, 6, 7, 3, 6, 7, 5, 6, 7, 4, 6, 7, 5, 6, 7]
x=[]
x = range(1,100)
y=list_game3

plt.plot(x,y,'bo')
plt.xlabel('Value of x')
plt.ylabel('attempts ')
plt.title('games 100')

plt.show()
