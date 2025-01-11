import matplotlib.pyplot as plt 
x1=[10,15,20,25,30]
y1=[40,30,20,30,40]
x2=[10,15,20,25,30]
y2=[20,30,40,30,20]
plt.title("Ranji Trophy")
plt.plot(x1,y1,color='blue',linewidth=3,label='line1, width=3')
plt.plot(x2,y2,color='red',linewidth=5,label='line2, width=5')
plt.title("Two or more lines with different widths abd colors with suitable lengends ")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()