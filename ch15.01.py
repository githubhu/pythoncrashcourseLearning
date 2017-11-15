import  matplotlib.pyplot as plt

x_values=[1,2,3,4,5]
y_values=[x**3 for x in x_values]

plt.plot(x_values,y_values)

#plt.show()


x_values=list(range(1,5000))
y_values=[x**3 for x in x_values]

plt.plot(x_values,y_values)

plt.show()
