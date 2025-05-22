import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

plt.rcParams['pdf.fonttype'] = 42

def solveC1(N):
    C1 = 2.7610*(N**0.2354)
    return C1

def meanSHDFinal(meanlam, N):
    C1 = solveC1(N)
    mnSHD = (C1*meanlam)
    return mnSHD

# Define function for formula of std(SHD)
def stdSHD(std_lamb, length):
    return (0.65 * (length ** (-0.45922))) * std_lamb

# Seq, N, mean_lambda, std_lambda, mean_SHD, std_SHD
Array = np.loadtxt(f'Fig2_SubplotWhole_Data/80PointsArray.txt', dtype=object, delimiter=',')
for i in range(1, 7):
    Array[:, i] = Array[:, i].astype(float)

# Plot the original data with different colors for each N value
N_data25 = np.array([25] * 16 + [50] * 16 + [100] * 16 + [200] * 16 + [400] * 16)
x_data25 = Array[:, 2]
y_data25 = Array[:, 4]

N_eval25 = meanSHDFinal(x_data25[N_data25 == 25], 25)
N_eval50 = meanSHDFinal(x_data25[N_data25 == 50], 50)
N_eval100 = meanSHDFinal(x_data25[N_data25 == 100], 100)
N_eval200 = meanSHDFinal(x_data25[N_data25 == 200], 200)
N_eval400 = meanSHDFinal(x_data25[N_data25 == 400], 400)

fig, axs = plt.subplots(2, 3, dpi=125, figsize=(8, 5))
#### Mean(Lambda) vs. Mean(SHD)
# Data points for mean(lambda) vs mean(SHD) without color
sc1 = axs[0, 0].scatter(Array[:, 2], Array[:, 4], c='k') # c=Array[:, 6], cmap=cmap, norm=norm
# Lines of Best Fit for mean(Lambda) vs. mean(SHD)
axs[0, 0].plot(x_data25[N_data25 == 25], N_eval25, c='blue')
axs[0, 0].plot(x_data25[N_data25 == 50], N_eval50, c='red')
axs[0, 0].plot(x_data25[N_data25 == 100], N_eval100, c='purple')
axs[0, 0].plot(x_data25[N_data25 == 200], N_eval200, c='green')
axs[0, 0].plot(x_data25[N_data25 == 400], N_eval400, c='orange')

#### std(Lambda) vs. Mean(SHD)
sc0 = axs[0, 1].scatter(Array[:, 3], Array[:, 4], c='k')

#### N vs. Mean(SHD)
sc0 = axs[0, 2].scatter(Array[:, 1], Array[:, 4], c='k')

#### Mean(Lambda) vs. std(SHD)
sc0 = axs[1, 0].scatter(Array[:, 2], Array[:, 5], c='k')

#### std(Lambda) vs. std(SHD)
sc0 = axs[1, 1].scatter(Array[:, 3], Array[:, 5], c='k')
# Lines of Best Fit for std(Lambda) vs. std(SHD)
fitstdSHD = np.empty(shape=len(Array[:, 3]))
for count, stdLam in enumerate(Array[:, 3]):
    if count < 16:
        fitstdSHD[count] = stdSHD(stdLam, 25)
    elif count < 32:
        fitstdSHD[count] = stdSHD(stdLam, 50)
    elif count < 48:
        fitstdSHD[count] = stdSHD(stdLam, 100)
    elif count < 64:
        fitstdSHD[count] = stdSHD(stdLam, 200)
    else:
        fitstdSHD[count] = stdSHD(stdLam, 400)
axs[1, 1].plot(Array[:16, 3], fitstdSHD[:16], c='blue', label='N = 25', linewidth=1.5, alpha=0.55)
axs[1, 1].plot(Array[16:32, 3], fitstdSHD[16:32], c='red', label='N = 50', linewidth=1.5, alpha=0.55)
axs[1, 1].plot(Array[32:48, 3], fitstdSHD[32:48], c='purple', label='N = 100', linewidth=1.5, alpha=0.55)
axs[1, 1].plot(Array[48:64, 3], fitstdSHD[48:64], c='green', linewidth=1.5, label='N = 200', alpha=0.55)
axs[1, 1].plot(Array[64:80, 3], fitstdSHD[64:80], c='orange', linewidth=1.5, label='N = 400', alpha=0.55)

#### N vs. std(SHD)
sc0 = axs[1, 2].scatter(Array[:, 1], Array[:, 5], c='k')


# axs[0, 1].scatter(Array[:, 2], Array[:, 4], color='blue')
# axs[0, 1].plot(Array[:16, 2], Array[:16, 4], color='blue', linewidth=2.0, alpha=0.55)
# axs[0, 1].plot(Array[16:32, 2], Array[16:32, 4], color='blue', linewidth=2.0, alpha=0.55)
# axs[0, 1].plot(Array[32:48, 2], Array[32:48, 4], color='blue', linewidth=2.0, alpha=0.55)
#
# axs[0, 2].scatter(Array[:, 1], Array[:, 4], color='blue')
# axs[0, 2].plot(Array[:16, 1], Array[:16, 4], color='blue', linewidth=2.0, alpha=0.55)
# axs[0, 2].plot(Array[16:32, 1], Array[16:32, 4], color='blue', linewidth=2.0, alpha=0.55)
# axs[0, 2].plot(Array[32:48, 1], Array[32:48, 4], color='blue', linewidth=2.0, alpha=0.55)
#
# axs[1, 0].scatter(Array[:, 3], Array[:, 5], color='blue')
# axs[1, 0].plot(Array[:16, 3], Array[:16, 5], color='blue', linewidth=2.0, alpha=0.55)
# axs[1, 0].plot(Array[16:32, 3], Array[16:32, 5], color='blue', linewidth=2.0, alpha=0.55)
# axs[1, 0].plot(Array[32:48, 3], Array[32:48, 5], color='blue', linewidth=2.0, alpha=0.55)
#
# axs[1, 1].scatter(Array[:, 2], Array[:, 5], color='blue')
# # axs[1, 1].plot(Array[:16, 2], Array[:16, 5], color='blue', linewidth=1.5, linestyle='--')
# # axs[1, 1].plot(Array[16:32, 2], Array[16:32, 5], color='blue', linewidth=1.5, linestyle='--')
# # axs[1, 1].plot(Array[32:48, 2], Array[32:48, 5], color='blue', linewidth=1.5, linestyle='--')
#
# axs[1, 2].scatter(Array[:, 1], Array[:, 5], color='blue')
# axs[1, 2].plot(Array[:16, 1], Array[:16, 5], color='blue', linewidth=2.0, alpha=0.55)
# axs[1, 2].plot(Array[16:32, 1], Array[16:32, 5], color='blue', linewidth=2.0, alpha=0.55)
# axs[1, 2].plot(Array[32:48, 1], Array[32:48, 5], color='blue', linewidth=2.0, alpha=0.55)

# Axis labels
axs[0, 0].set_ylabel('Mean(SHD)', fontweight='bold', labelpad=23)
axs[1, 0].set_ylabel('std(SHD)', fontweight='bold', labelpad=1)
axs[1, 0].set_xlabel('Mean(Lambda)', fontweight='bold')
axs[1, 1].set_xlabel('Std(Lambda)', fontweight='bold')
axs[1, 2].set_xlabel('N', fontweight='bold')


# Save and show plot
plt.savefig('Fig2_Old_A-F_NoColor.pdf')
plt.show()
