import numpy as np
from matplotlib import pyplot as plt

n = 20
step = 0.1
x = np.arange(0, n + 1, step)
o1 = np.ones(int((n + 1) / step))
ologn = np.log2(x)
on2 = x ** 2
o2n = 2 ** x


plt.axis([0, n, 0, 45])
plt.xticks(range(1, n + 1, 2))
plt.xlabel("n")
plt.ylabel("f(n)")
plt.plot(x, o1, label="O(1)")
plt.plot(x, ologn, label="O(log(n))")
plt.plot(x, on2, label="O(n^2)")
plt.plot(x, o2n, label="O(2^n)")
plt.legend()
plt.grid()
plt.show()