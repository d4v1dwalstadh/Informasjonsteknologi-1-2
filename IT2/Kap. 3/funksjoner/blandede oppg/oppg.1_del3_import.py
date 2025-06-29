import matplotlib.pyplot as plt
import numpy as np

aarstall = [1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 
            1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 
            1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 
            2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
            2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

eksportert = [325, 898, 1421, 2176, 907, 1859, 3174, 1569, 1644, 3373, 4767, 5259, 5607, 
              5703, 6877, 1570, 4250, 5493, 2501, 7154, 6704, 13847, 9130, 4627, 2180, 3320, 
              7355, 15166, 16241, 6049, 10109, 8486, 4968, 8962, 4236, 4874, 4412, 8776, 
              20529, 7162, 15002, 5587, 3842, 15695, 8947, 15320, 17291, 14633, 7123, 14329,
              22006, 15140, 21932, 22038, 22151, 21276, 18489, 12309, 24968, 25819]

importert = [-34, -54, -116, -117, -631, -344, -179, -221, -808, -458, -120, -66, -63, -83,
             -240, -2653, -845, -842, -2039, -1925, -642, -431, -860, -4083, -4212, -2983, 
             -1727, -314, -334, -3274, -1380, -587, -4836, -2300, -13212, -8692, -8046, -6857,
             -1474, -10760, -5329, -13472, -15334, -3653, -9802, -5284, -3414, -5650, -14673,
             -11255, -4190, -10135, -6347, -7411, -5741, -6112, -8340, -12353, -4496, -8235]



#graf 1
plt.subplot(2, 1, 1)
plt.plot(aarstall, eksportert)
plt.grid()

#graf 2
plt.subplot(2, 1, 2)
plt.plot(aarstall, importert)
plt.grid()

plt.show()







"""
#todelt vannrett søylediagram
importert_motsatt = [-x for x in importert] #gir oss liste ganget med -1

fig, ax = plt.subplots(figsize=(10, 5)) #angir størrelsen på figur område

y = np.arange(len(aarstall)) #gir liste med tall jevnt fordelt

ax.barh(y+0.2, eksportert, height=0.4, label="eksport") #offsetter ene litt opp og andre litt ned
ax.barh(y-0.2, importert_motsatt, height=0.4, label="import")
ax.set_yticks(y, aarstall)
ax.legend()

fig.subplots_adjust(left=0.4) #figur tar nå opp 60% av plassen, starter fra høyre

ax.grid(axis="x")
plt.show()
"""