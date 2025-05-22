import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

plt.rcParams['pdf.fonttype'] = 42
# define function for formula of std(SHD)
def stdSHD(std_lamb, length):
    stdSHD = (0.65 * (length ** (-0.45922))) * std_lamb
    return stdSHD

# Seq, N, mean_lambda, std_lambda, mean_SHD, std_SHD
Array = np.loadtxt(f'Fig2_SubplotWhole_Data/80PointsArray', dtype=object, delimiter=',')
for i in range(1, 7):
    Array[:, i] = Array[:, i].astype(float)

# Set color values depending on the rounded values in the 7th column of the array (mean(lambda) identities)
unique_values = np.unique(Array[:, 6])
color_values = [0.4, 0.5, 0.6, 0.7]
norm = BoundaryNorm(boundaries=[0.4, 0.5, 0.6, 0.7, 0.8], ncolors=4, extend='neither')
set1_colors = plt.get_cmap('Dark2').colors
selected_colors = [set1_colors[i] for i in [0, 1, 2, 3]]  # First 3 (index 0, 1, 2) and 5th (index 4)
cmap = ListedColormap(selected_colors)
color_indices = np.array([np.digitize(val, color_values) - 1 for val in Array[:, 6]])


# fig, axs = plt.subplots(2, 3, dpi=100, figsize=(9, 3.8))
# # fig, axs = plt.subplots(2, 3, dpi=300, figsize=(6, 4))
#
# dash_style = [4, 4]
# # Plot scattered data points
# sc0 = axs[0, 0].scatter(Array[:, 3], Array[:, 4], c=Array[:, 6], cmap=cmap, norm=norm)
# # axs[0, 0].plot(Array[:16, 3], Array[:16, 4], c='blue', linewidth=2, linestyle='--', dashes=dash_style)
# # axs[0, 0].plot(Array[16:32, 3], Array[16:32, 4], c='red', linewidth=2, linestyle='--', dashes=dash_style)
# # axs[0, 0].plot(Array[32:48, 3], Array[32:48, 4], c='black', linewidth=2, linestyle='--', dashes=dash_style)
#
#
# sc1 = axs[0, 1].scatter(Array[:, 2], Array[:, 4], c=Array[:, 6], cmap=cmap, norm=norm)
# axs[0, 1].plot(Array[:16, 2], Array[:16, 4], c='blue', linewidth=2.0, label='N = 50', alpha=0.55)
# axs[0, 1].plot(Array[16:32, 2], Array[16:32, 4], c='red', linewidth=2.0, label='N = 100', alpha=0.55)
# axs[0, 1].plot(Array[32:48, 2], Array[32:48, 4], c='black', linewidth=2.0, label='N = 200', alpha=0.55)
#
# sc2 = axs[0, 2].scatter(Array[:, 1], Array[:, 4], c=Array[:, 6], cmap=cmap, norm=norm)
# axs[0, 2].plot(Array[:16, 1], Array[:16, 4], c='blue', linewidth=2.0, alpha=0.55)
# axs[0, 2].plot(Array[16:32, 1], Array[16:32, 4], c='red', linewidth=2.0, alpha=0.55)
# axs[0, 2].plot(Array[32:48, 1], Array[32:48, 4], c='black', linewidth=2.0, alpha=0.55)
#
# sc3 = axs[1, 0].scatter(Array[:, 3], Array[:, 5], c=Array[:, 6], cmap=cmap, norm=norm)
# axs[1, 0].plot(Array[:16, 3], Array[:16, 5], linewidth=2.0, alpha=0.55)
# axs[1, 0].plot(Array[16:32, 3], Array[16:32, 5], c='red', linewidth=2.0, alpha=0.55)
# axs[1, 0].plot(Array[32:48, 3], Array[32:48, 5], c='black', linewidth=2.0, alpha=0.55)
#
# sc4 = axs[1, 1].scatter(Array[:, 2], Array[:, 5], c=Array[:, 6], cmap=cmap, norm=norm)
# # axs[1, 1].plot(Array[:16, 2], Array[:16, 5], c='blue', linewidth=1.5, linestyle='--')
# # axs[1, 1].plot(Array[16:32, 2], Array[16:32, 5], c='red', linewidth=1.5, linestyle='--')
# # axs[1, 1].plot(Array[32:48, 2], Array[32:48, 5], c='black', linewidth=1.5, linestyle='--')
#
# sc5 = axs[1, 2].scatter(Array[:, 1], Array[:, 5], c=Array[:, 6], cmap=cmap, norm=norm)
# axs[1, 2].plot(Array[:16, 1], Array[:16, 5], c='blue', linewidth=2.0, alpha=0.55)
# axs[1, 2].plot(Array[16:32, 1], Array[16:32, 5], c='red', linewidth=2.0, alpha=0.55)
# axs[1, 2].plot(Array[32:48, 1], Array[32:48, 5], c='black', linewidth=2.0, alpha=0.55)
#
#
# # Axis Labels
# axs[0, 0].set_ylabel('Mean(SHD)', fontweight='bold', labelpad=23)
# axs[1, 0].set_ylabel('Std(SHD)', fontweight='bold', labelpad=1)
# axs[1, 0].set_xlabel('Std(Lambda)', fontweight='bold')
# axs[1, 1].set_xlabel('Mean(Lambda)', fontweight='bold')
# axs[1, 2].set_xlabel('N', fontweight='bold')
# fig.legend()
#
# # Ticks
# axs[1, 2].set_xticks([50, 100, 200])
# # set y-bounds for std(SHD)
# y_min = np.min(Array[:-1, 5])
# y_max = np.max(Array[:-1, 5])
# print(f"{y_min}\n{y_max}")
# y_int = (y_max-y_min)/7
# y_ticks = (np.arange(y_min, y_max + y_int, y_int)).round(decimals=3)
# for ax in axs[1, :]:
#     ax.set_yticks(y_ticks)
#     ax.set_ylim(y_min, y_max)
#
# plt.tight_layout()
# # set colorbars
# cbar = fig.colorbar(sc0, ax=axs, location='right', boundaries=[0.4, 0.5, 0.6, 0.7], ticks=[0.4, 0.5, 0.6, 0.7])
# cbar.set_label('Value', fontweight='bold')

# mean(lambda) vs mean(SHD)
# fig, axs = plt.subplots(2, 2, dpi=125, figsize=(8, 5))
fig, axs = plt.subplots(1, 2, dpi=125, figsize=(8, 5))
sc1 = axs[0].scatter(Array[:, 2], Array[:, 4], c='k') # c=Array[:, 6], cmap=cmap, norm=norm
# axs[0].plot(Array[:16, 2], Array[:16, 4], c='blue', linewidth=1.5, label='N = 25', alpha=0.55)
# axs[0].plot(Array[16:32, 2], Array[16:32, 4], c='red', linewidth=1.5, label='N = 50', alpha=0.55)
# axs[0].plot(Array[32:48, 2], Array[32:48, 4], c='purple', linewidth=1.5, label='N = 100', alpha=0.55)
# axs[0].plot(Array[48:64, 2], Array[48:64, 4], c='green', linewidth=1.5, label='N = 200', alpha=0.55)
# axs[0].plot(Array[64:80, 2], Array[64:80, 4], c='orange', linewidth=1.5, label='N = 400', alpha=0.55)
def solveC1(N):
    C1 = 2.7610*(N**0.2354)
    return C1

def meanSHDFinal(meanlam, N):
    C1 = solveC1(N)
    mnSHD = (C1*meanlam)
    return mnSHD


# Plot the original data with different colors for each N value
N_data25 = np.array([25] * 16 + [50] * 16 + [100] * 16 + [200] * 16 + [400] * 16)
x_data25 = Array[:, 2]
y_data25 = Array[:, 4]

axs[0].scatter(x_data25[N_data25 == 25], y_data25[N_data25 == 25], c='blue', label='N = 25', alpha=0.7)
axs[0].scatter(x_data25[N_data25 == 50], y_data25[N_data25 == 50], c='red', label='N = 50', alpha=0.7)
axs[0].scatter(x_data25[N_data25 == 100], y_data25[N_data25 == 100], c='purple', label='N = 100', alpha=0.7)
axs[0].scatter(x_data25[N_data25 == 200], y_data25[N_data25 == 200], c='green', label='N = 200', alpha=0.7)
axs[0].scatter(x_data25[N_data25 == 400], y_data25[N_data25 == 400], c='orange', label='N = 400', alpha=0.7)

N_eval25 = meanSHDFinal(x_data25[N_data25 == 25], 25)
N_eval50 = meanSHDFinal(x_data25[N_data25 == 50], 50)
N_eval100 = meanSHDFinal(x_data25[N_data25 == 100], 100)
N_eval200 = meanSHDFinal(x_data25[N_data25 == 200], 200)
N_eval400 = meanSHDFinal(x_data25[N_data25 == 400], 400)

axs[0].plot(x_data25[N_data25 == 25], N_eval25, c='blue')
axs[0].plot(x_data25[N_data25 == 50], N_eval50, c='red')
axs[0].plot(x_data25[N_data25 == 100], N_eval100, c='purple')
axs[0].plot(x_data25[N_data25 == 200], N_eval200, c='green')
axs[0].plot(x_data25[N_data25 == 400], N_eval400, c='orange')

axs[0].set_xlabel('Mean(Lambda)', fontweight='bold')
axs[0].set_ylabel('Mean(SHD)', fontweight='bold')

# std(lambda) vs std(SHD)
sc3 = axs[1].scatter(Array[:, 3], Array[:, 5], c='k') # c=Array[:, 6], cmap=cmap, norm=norm
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

axs[1].plot(Array[:16, 3], fitstdSHD[:16], c='blue', label='N = 25', linewidth=1.5, alpha=0.55)
axs[1].plot(Array[16:32, 3], fitstdSHD[16:32], c='red', label='N = 50', linewidth=1.5, alpha=0.55)
axs[1].plot(Array[32:48, 3], fitstdSHD[32:48], c='purple', label='N = 100', linewidth=1.5, alpha=0.55)
axs[1].plot(Array[48:64, 3], fitstdSHD[48:64], c='green', linewidth=1.5, label='N = 200', alpha=0.55)
axs[1].plot(Array[64:80, 3], fitstdSHD[64:80], c='orange', linewidth=1.5, label='N = 400', alpha=0.55)
axs[1].set_ylabel('Std(SHD)', fontweight='bold')
axs[1].set_xlabel('Std(Lambda)', fontweight='bold')

# N vs change in slope of mean(lambda) vs mean(SHD) (change in mean(SHD)/mean(lambda))
meanLam25 = Array[:16, 2]
meanSHD25 = Array[:16, 4]
meanLam50 = Array[16:32, 2]
meanSHD50 = Array[16:32, 4]
meanLam100 = Array[32:48, 2]
meanSHD100 = Array[32:48, 4]
meanLam200 = Array[48:64, 2]
meanSHD200 = Array[48:64, 4]
meanLam400 = Array[64:80, 2]
meanSHD400 = Array[64:80, 4]
slope_mean25 = [(meanSHD25[i+1]-meanSHD25[i])/(meanLam25[i+1]-meanLam25[i]) for i in range(len(meanLam50)-1)]
slope_mean50 = [(meanSHD50[i+1]-meanSHD50[i])/(meanLam50[i+1]-meanLam50[i]) for i in range(len(meanLam50)-1)]
slope_mean100 = [(meanSHD100[i+1]-meanSHD100[i])/(meanLam100[i+1]-meanLam100[i]) for i in range(len(meanLam50)-1)]
slope_mean200 = [(meanSHD200[i+1]-meanSHD200[i])/(meanLam200[i+1]-meanLam200[i]) for i in range(len(meanLam50)-1)]
slope_mean400 = [(meanSHD400[i+1]-meanSHD400[i])/(meanLam400[i+1]-meanLam400[i]) for i in range(len(meanLam50)-1)]

# axs[1, 0].scatter([25, 50, 100, 200, 400], [np.mean(slope_mean25), np.mean(slope_mean50), np.mean(slope_mean100), np.mean(slope_mean200), np.mean(slope_mean400)])
# axs[1, 0].set_xlabel('N', fontweight='bold')
# axs[1, 0].set_ylabel('\u0394(mean(SHD)/mean(Lambda))', fontweight='bold')

# change in slopes of std(lam) vs std(SHD)
stdLam25 = Array[:16, 3]
stdSHD25 = Array[:16, 5]
stdLam50 = Array[16:32, 3]
stdSHD50 = Array[16:32, 5]
stdLam100 = Array[32:48, 3]
stdSHD100 = Array[32:48, 5]
stdLam200 = Array[48:64, 3]
stdSHD200 = Array[48:64, 5]
stdLam400 = Array[64:80, 3]
stdSHD400 = Array[64:80, 5]
slope_std25 = [(stdSHD25[i+1]-stdSHD25[i])/(stdLam25[i+1]-stdLam25[i]) for i in range(len(meanLam50)-1)]
slope_std50 = [(stdSHD50[i+1]-stdSHD50[i])/(stdLam50[i+1]-stdLam50[i]) for i in range(len(meanLam50)-1)]
slope_std100 = [(stdSHD100[i+1]-stdSHD100[i])/(stdLam100[i+1]-stdLam100[i]) for i in range(len(meanLam50)-1)]
slope_std200 = [(stdSHD200[i+1]-stdSHD200[i])/(stdLam200[i+1]-stdLam200[i]) for i in range(len(meanLam50)-1)]
slope_std400 = [(stdSHD400[i+1]-stdSHD400[i])/(stdLam400[i+1]-stdLam400[i]) for i in range(len(meanLam50)-1)]

# axs[1, 1].scatter([25, 50, 100, 200, 400], [np.mean(slope_std25), np.mean(slope_std50), np.mean(slope_std100), np.mean(slope_std200), np.mean(slope_std400)])
# axs[1, 1].set_xlabel('N', fontweight='bold')
# axs[1, 1].set_ylabel('\u0394(std(SHD)/std(Lambda))', fontweight='bold')

def slope_calc(N):
    return ((0.65 * (N ** (-0.45922))))

x_slopecalc = np.linspace(25, 400, 100)
# axs[1, 1].plot(x_slopecalc, slope_calc(x_slopecalc),alpha=0.3, label='Slope Formula')
# axs[1, 1].legend()


y_min = np.min(Array[:-1, 5])
y_max = np.max(Array[:-1, 5])
print(f"{y_min}\n{y_max}")
y_int = (y_max-y_min)/7
y_ticks = (np.arange(y_min, y_max + y_int, y_int)).round(decimals=3)
axs[1].set_yticks(y_ticks)
axs[1].set_ylim(y_min, y_max)

axs[0].legend()
plt.savefig('Fig2_SubplotWhole.pdf')
plt.tight_layout()
plt.show()
