import matplotlib.pyplot as plt  #plotting i py

def f(x):
  return x**2

xverdier = []
yverdier = []

for xverdi in range(10):
  xverdier.append(xverdi)
  yverdier.append(f(xverdi))

plt.plot(xverdier, yverdier)
plt.scatter(xverdier, yverdier) #gir punktene
plt.show()