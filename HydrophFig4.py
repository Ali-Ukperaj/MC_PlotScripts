import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

plt.rcParams['pdf.fonttype'] = 42
# define function for formula of std(SHD)
def stdSHD(std_lamb, length):
    stdSHD = (0.65 * (length ** (-0.45922))) * std_lamb
    return stdSHD

# Seq, N, mean_lambda, std_lambda, mean_SHD, std_SHD
Array = np.loadtxt(f'HydrophFig4Data/50PointsArray_Old', dtype=object, delimiter=',')
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

fig, axs = plt.subplots(2, 3)
# fig, axs = plt.subplots(2, 3, dpi=300, figsize=(6, 4))

dash_style = [4, 4]
# Plot scattered data points
sc0 = axs[0, 0].scatter(Array[:, 3], Array[:, 4], c=Array[:, 6], cmap=cmap, norm=norm)
# axs[0, 0].plot(Array[:16, 3], Array[:16, 4], c='blue', linewidth=2, linestyle='--', dashes=dash_style)
# axs[0, 0].plot(Array[16:32, 3], Array[16:32, 4], c='red', linewidth=2, linestyle='--', dashes=dash_style)
# axs[0, 0].plot(Array[32:48, 3], Array[32:48, 4], c='black', linewidth=2, linestyle='--', dashes=dash_style)


sc1 = axs[0, 1].scatter(Array[:, 2], Array[:, 4], c=Array[:, 6], cmap=cmap, norm=norm)
axs[0, 1].plot(Array[:16, 2], Array[:16, 4], c='blue', linewidth=2.0, label='N = 50', alpha=0.55)
axs[0, 1].plot(Array[16:32, 2], Array[16:32, 4], c='red', linewidth=2.0, label='N = 100', alpha=0.55)
axs[0, 1].plot(Array[32:48, 2], Array[32:48, 4], c='black', linewidth=2.0, label='N = 200', alpha=0.55)

sc2 = axs[0, 2].scatter(Array[:, 1], Array[:, 4], c=Array[:, 6], cmap=cmap, norm=norm)
axs[0, 2].plot(Array[:16, 1], Array[:16, 4], c='blue', linewidth=2.0, alpha=0.55)
axs[0, 2].plot(Array[16:32, 1], Array[16:32, 4], c='red', linewidth=2.0, alpha=0.55)
axs[0, 2].plot(Array[32:48, 1], Array[32:48, 4], c='black', linewidth=2.0, alpha=0.55)

sc3 = axs[1, 0].scatter(Array[:, 3], Array[:, 5], c=Array[:, 6], cmap=cmap, norm=norm)
axs[1, 0].plot(Array[:16, 3], Array[:16, 5], linewidth=2.0, alpha=0.55)
axs[1, 0].plot(Array[16:32, 3], Array[16:32, 5], c='red', linewidth=2.0, alpha=0.55)
axs[1, 0].plot(Array[32:48, 3], Array[32:48, 5], c='black', linewidth=2.0, alpha=0.55)

sc4 = axs[1, 1].scatter(Array[:, 2], Array[:, 5], c=Array[:, 6], cmap=cmap, norm=norm)
# axs[1, 1].plot(Array[:16, 2], Array[:16, 5], c='blue', linewidth=1.5, linestyle='--')
# axs[1, 1].plot(Array[16:32, 2], Array[16:32, 5], c='red', linewidth=1.5, linestyle='--')
# axs[1, 1].plot(Array[32:48, 2], Array[32:48, 5], c='black', linewidth=1.5, linestyle='--')

sc5 = axs[1, 2].scatter(Array[:, 1], Array[:, 5], c=Array[:, 6], cmap=cmap, norm=norm)
axs[1, 2].plot(Array[:16, 1], Array[:16, 5], c='blue', linewidth=2.0, alpha=0.55)
axs[1, 2].plot(Array[16:32, 1], Array[16:32, 5], c='red', linewidth=2.0, alpha=0.55)
axs[1, 2].plot(Array[32:48, 1], Array[32:48, 5], c='black', linewidth=2.0, alpha=0.55)


# Axis Labels
axs[0, 0].set_ylabel('Mean(SHD)', fontweight='bold', labelpad=23)
axs[1, 0].set_ylabel('Std(SHD)', fontweight='bold', labelpad=1)
axs[1, 0].set_xlabel('Std(Lambda)', fontweight='bold')
axs[1, 1].set_xlabel('Mean(Lambda)', fontweight='bold')
axs[1, 2].set_xlabel('N', fontweight='bold')
fig.legend()

# Ticks
axs[1, 2].set_xticks([50, 100, 200])
# set y-bounds for std(SHD)
y_min = np.min(Array[:-1, 5])
y_max = np.max(Array[:-1, 5])
# print(f"{y_min}\n{y_max}")
y_int = (y_max-y_min)/7
y_ticks = (np.arange(y_min, y_max + y_int, y_int)).round(decimals=3)
for ax in axs[1, :]:
    ax.set_yticks(y_ticks)
    ax.set_ylim(y_min, y_max)

# plt.tight_layout()

# set colorbars
cbar = fig.colorbar(sc0, ax=axs, location='right', boundaries=[0.4, 0.5, 0.6, 0.7], ticks=[0.4, 0.5, 0.6, 0.7])
cbar.set_label('Value', fontweight='bold')

plt.savefig('HydrophFig4.pdf')
plt.show()