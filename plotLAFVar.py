import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['pdf.fonttype'] = 42
folder = 'LAFVar_Data/'
template = np.loadtxt(f"{folder}LAF1_SCD5_1Frac", dtype=float, delimiter=',')
length = len(template)
plt.rcParams['pdf.fonttype'] = 42

######################################### Start Plotting Averages #########################################
SCD_All = np.empty(shape=(3, 10, length+1))
frac_All = np.empty(shape=(3, 10, length))

SCD_Vals = [5, 10, 15]
for ct, j in enumerate(SCD_Vals):
    for i in range(1, 11):
        SCD_file = f"{folder}LAF1_SCD{j}_{i}"
        fracAcc_file = f"{folder}LAF1_SCD{j}_{i}Frac"

        SCD_All[ct, i-1, :] = np.loadtxt(SCD_file, usecols=(1), dtype=float, delimiter=',')
        frac_All[ct, i-1, :] = np.loadtxt(fracAcc_file, dtype=float, delimiter=',')

avg_SCD = np.empty(shape=[3, length+1])
avg_frac = np.empty(shape=[3, length])

for i in range(0, 3):
    avg_SCD[i, :] = np.average(SCD_All[i, :, :], axis=0)
    avg_frac[i, :] = np.average(frac_All[i, :, :], axis=0)

    times = np.arange(0, length+1, 1)
    fig, ax1 = plt.subplots()
    fig.suptitle(f'LAF1 Variant Average: SCD = -{SCD_Vals[i]}')
    color = 'tab:red'
    ax1.set_xlabel('Monte Carlo Moves')
    ax1.set_ylabel('SCD', color=color)
    ax1.plot(times, avg_SCD[i], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Fraction of Accepted Moves', color=color)  # we already handled the x-label with ax1
    ax2.plot(times[1:], avg_frac[i], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()

######################################### End Plotting Averages #########################################

############################################# Start LAF -5 #############################################
for i in range(1, 10):
    SCD_file = f"{folder}LAF1_SCD5_{i}"
    fracAcc_file = f"{folder}LAF1_SCD5_{i}Frac"

    SCD = np.loadtxt(SCD_file, usecols=(1), dtype=float, delimiter=',')
    fracAcc = np.loadtxt(fracAcc_file, dtype=float, delimiter=',')

    # iterations = np.linspace(0, len(SCD), len(SCD))

    ############### Start Plot ###############
    times = np.arange(0, len(SCD), 1)
    plt.plot(times, avg_SCD[0, :], 'k', linewidth=2, alpha=0.7)
    plt.plot(times, SCD, color='g', alpha=i/10)
    # fig, ax1 = plt.subplots()
    # fig.suptitle('LAF1-Variant: SCD = -5')
    # color = 'tab:red'
    # ax1.set_xlabel('Monte Carlo Moves')
    # ax1.set_ylabel('SCD', color=color)
    # ax1.plot(times, SCD, color=color)
    # ax1.tick_params(axis='y', labelcolor=color)
    #
    # ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis
    #
    # color = 'tab:blue'
    # ax2.set_ylabel('Fraction of Accepted Moves', color=color)  # we already handled the x-label with ax1
    # ax2.plot(times[1:], fracAcc, color=color)
    # ax2.tick_params(axis='y', labelcolor=color)
plt.xlabel('Monte Carlo Moves')
plt.ylabel('SCD')
plt.axhline(-5, color='r', linestyle='--')
plt.title('LAF-1; SCD = -5')
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig('LAF1_SCD5_Graph.pdf')
plt.show()
############### End Plot ###############

############################################# End LAF -5 #############################################



############################################# Start LAF -10 #############################################
for i in range(1, 10):
    SCD_file = f"{folder}LAF1_SCD10_{i}"
    fracAcc_file = f"{folder}LAF1_SCD10_{i}Frac"

    SCD = np.loadtxt(SCD_file, usecols=(1), dtype=float, delimiter=',')
    fracAcc = np.loadtxt(fracAcc_file, dtype=float, delimiter=',')

    plt.plot(times, avg_SCD[1, :], 'k', linewidth=2, alpha=0.7)
    plt.plot(times, SCD, color='g', alpha=i/10)
    # ############### Start Plot ###############
    # times = np.arange(0, len(SCD), 1)
    # fig, ax1 = plt.subplots()
    # fig.suptitle('LAF1-Variant: SCD = -10')
    # color = 'tab:red'
    # ax1.set_xlabel('Monte Carlo Moves')
    # ax1.set_ylabel('SCD', color=color)
    # ax1.plot(times, SCD, color=color)
    # ax1.tick_params(axis='y', labelcolor=color)
    #
    # ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis
    #
    # color = 'tab:blue'
    # ax2.set_ylabel('Fraction of Accepted Moves', color=color)  # we already handled the x-label with ax1
    # ax2.plot(times[1:], fracAcc, color=color)
    # ax2.tick_params(axis='y', labelcolor=color)
plt.xlabel('Monte Carlo Moves')
plt.ylabel('SCD')
plt.axhline(-10, color='r', linestyle='--')
plt.title('LAF-1; SCD = -10')
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig('LAF1_SCD10_Graph.pdf')
plt.show()
    ############### End Plot ###############

############################################# End LAF -10 #############################################


############################################# Start LAF -15 #############################################
for i in range(1, 10):
    SCD_file = f"{folder}LAF1_SCD15_{i}"
    fracAcc_file = f"{folder}LAF1_SCD15_{i}Frac"

    SCD = np.loadtxt(SCD_file, usecols=(1), dtype=float, delimiter=',')
    fracAcc = np.loadtxt(fracAcc_file, dtype=float, delimiter=',')

    # iterations = np.linspace(0, len(SCD), len(SCD))
    plt.plot(times, avg_SCD[2, :], 'k', linewidth=2, alpha=0.7)
    plt.plot(times, SCD, color='g', alpha=i / 10)
    # ############### Start Plot ###############
    # times = np.arange(0, len(SCD), 1)
    # fig, ax1 = plt.subplots()
    # fig.suptitle('LAF1-Variant: SCD = -15')
    # color = 'tab:red'
    # ax1.set_xlabel('Monte Carlo Moves')
    # ax1.set_ylabel('SCD', color=color)
    # ax1.plot(times, SCD, color=color)
    # ax1.tick_params(axis='y', labelcolor=color)
    #
    # ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis
    #
    # color = 'tab:blue'
    # ax2.set_ylabel('Fraction of Accepted Moves', color=color)  # we already handled the x-label with ax1
    # ax2.plot(times[1:], fracAcc, color=color)
    # ax2.tick_params(axis='y', labelcolor=color)
plt.xlabel('Monte Carlo Moves')
plt.ylabel('SCD')
plt.axhline(-15, color='r', linestyle='--')
plt.title('LAF-1; SCD = -15')
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig('LAF1_SCD15_Graph.pdf')
plt.show()
    ############### End Plot ###############

############################################# End LAF -15 #############################################