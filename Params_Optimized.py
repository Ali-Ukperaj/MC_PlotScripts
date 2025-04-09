import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

plt.rcParams['pdf.fonttype'] = 42
#Movements = np.loadtxt("Total_Movements123456", dtype=object, delimiter=',')
Movements = np.loadtxt("Params_Optimized_Data/Total_Movements246", dtype=object, delimiter=',')
SCD_Goal, SHD_Goal, SAD_Goal, delG_Goal = -5, 5.349, 0.028, -10

SCD = Movements[:, 1].astype(float)
SHD = Movements[:, 2].astype(float)
delG = Movements[:, 4].astype(float)
Comp = Movements[:, 5].astype(float)
Steps = len(Movements[:, 1])

# SCD_Goal = 0.0393
# SHD_Goal = 6.5
# delG_Goal = -11

# create colormap for composition
norm = plt.Normalize(Comp.min(), Comp.max())
colors = cm.coolwarm(norm(Comp))

fig = plt.figure()
ax = plt.axes(projection='3d')

for i in range(Steps-1):
    ax.plot3D(SCD[i:i+2], SHD[i:i+2], delG[i:i+2], color=colors[i], linewidth=2)
ax.scatter(SCD[0], SHD[0], delG[0], facecolor='green', label='Starting Point')
ax.scatter(SCD[-1], SHD[-1], delG[-1], facecolor='red', label='Ending Point')
plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.1)
mappable = cm.ScalarMappable(norm=norm, cmap=cm.coolwarm)
mappable.set_array(Comp)
cbar = fig.colorbar(mappable, ax=ax, fraction=0.02, pad=0.15)  # Adjust pad to control the distance from the plot
cbar.set_label('Composition (Comp)')


ax.legend()
ax.set_xlabel("SCD", fontweight='bold', labelpad=15)
ax.set_ylabel("SHD", fontweight='bold')
ax.set_zlabel("\u0394(G)", fontweight='bold')

ax.set_xticklabels([f'{x:.2f}' for x in ax.get_xticks()], rotation=45, ha='right')
ax.set_yticklabels([f'{y:.2f}' for y in ax.get_yticks()], rotation=0, ha='right', fontsize=10)
ax.set_zticklabels([f'{z:1.0f}' for z in ax.get_zticks()], rotation=0, ha='right', fontsize=10)

ax.tick_params(axis='x', which='major', labelsize=10, pad=-3)
ax.tick_params(axis='y', which='major', labelsize=10)  # Smaller tick labels
ax.tick_params(axis='z', which='major', labelsize=10)  # Smaller tick labels

# ax.set_title("Sequence Optimization Path", fontweight='bold')
# plt.show()

print(f"Original FUS: {Movements[0, 0]}\nFinal Seq: {Movements[-1, 0]}")

Amino_1 = ['A','R','N','D','C','Q','E','G','H','I','L','K','M',
           'F','P','S','T','W','Y','V']
NewSeq = list(Movements[-1, 0])
Length = len(NewSeq)
Ideal_Seq =list('MASNDYTQQATQSYGAYPTQPGQGYSQQSSQPYGQQSYSGYSQSTDTSGYGQSSYSSYGQSQNTGYGTQSTPQGYGSTGG'
                 'YGSSQSSQSSYGQQSSYPGYGQQPAPSSTSGSYGSSSQSSSYGQPQSGSYSQQPSYGGQQQSYGQQQSYNPPQGYGQQNQYNS')
CompositionOld = {amino: (len(np.where(np.array(Ideal_Seq) == amino)[0].tolist()))/(Length) for amino in Amino_1}
CompositionNew = {amino: (len(np.where(np.array(NewSeq) == amino)[0].tolist()))/(Length) for amino in Amino_1}
ResOld = {amino: (len(np.where(np.array(Ideal_Seq) == amino)[0].tolist())) for amino in Amino_1}
ResNew = {amino: (len(np.where(np.array(NewSeq) == amino)[0].tolist())) for amino in Amino_1}
print(f"Comp_Old: {CompositionOld}")
print(f"Comp_New: {CompositionNew}")

print(f"Total Residues FUS: {ResOld}")
print(f"Total Residues New: {ResNew}")
for key, value in ResOld.items():
    print(f"{key}: {(ResNew[key] - value)}, ")

x1 = np.linspace(0, Steps*10, Steps)
fig1, axs1 = plt.subplots(2, 2, dpi=200, figsize=(5, 4))
axs1[0, 0].plot(x1, SCD)
axs1[0, 0].plot(x1, [SCD_Goal]*Steps, '--r')
axs1[0, 0].set_title('SCD')
axs1[0, 1].plot(x1, SHD)
axs1[0, 1].plot(x1, [SHD_Goal]*Steps, '--r')
axs1[0, 1].set_title('SHD')
axs1[1, 0].plot(x1, delG)
axs1[1, 0].plot(x1, [delG_Goal]*Steps, '--r', label='Goal Value')
axs1[1, 0].set_title('\u0394(G)')
axs1[1, 0].set_xlabel('Steps')
fig1.legend(loc='center')
fig1.delaxes(axs1[1, 1])
plt.savefig('Param_Trajectory.pdf')
plt.tight_layout()
plt.show()

plt.plot(x1, SCD)
plt.plot(x1, [SCD_Goal]*Steps, '--r')
plt.title('SCD')
plt.xlabel('Monte Carlo Moves')
plt.show()

plt.plot(x1, SHD)
plt.plot(x1, [SHD_Goal]*Steps, '--r')
plt.title('SHD')
plt.xlabel('Monte Carlo Moves')
plt.show()

plt.plot(x1, delG)
plt.plot(x1, [delG_Goal]*Steps, '--r')
plt.title('delG')
plt.xlabel('Monte Carlo Moves')
plt.show()
