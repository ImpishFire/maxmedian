import numpy as np
import matplotlib.pyplot as plt
file = open("mc_counts_h1", "rb")
arr1 = np.load(file)
file2 = open("mc_counts_h2", "rb")
arr2 = np.load(file2)
print(arr2.shape)
t = np.linspace(10, 5000, num = 20, dtype=int)
sarr1 = np.poly1d(np.polyfit(t, arr1, 4))
sarr2 = np.poly1d(np.polyfit(t, arr2, 4))
with plt.style.context('Solarize_Light2'):

            fig, ax = plt.subplots()
            ax.plot(t, sarr1(t), color='blue', label='h(x) = $Kx^{3/4}logx + 1$')
            ax.plot(t, sarr2(t), color='orange', label='h(x) = $Kx^{4/5}$')
            ax.grid(True, which='both')
            ax.set_xlabel("time")
            ax.set_ylabel("% Best Arm Pulls")
plt.legend()
plt.show()
