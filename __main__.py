import numpy as np
from xp_helpers import MC_Xtreme
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

path = "C:\\Users\\Dell\\Desktop\\in\\estimation\\project\\code\\efficient bandits\\ExtremeBandits_submission\\xp"
m = 5# Number of trajectories in each simulation! m=10000 in     the paper's experiments

params = {
        'MaxMedian': {'explo_func': lambda t: 1/t}
          }#'Threshold_Ascent': {'s': 100, 'delta': 0.1},'QoMax_ETC': {'size': (100, 10), 'q': 0.9}

# Reproducing experiments for previous papers
xp1 = {'arms': ['Par'] * 5, 'coef': [[2.1, 1], [2.3, 1], [1.3, 1], [1.1, 1], [1.9, 1]]}  # xp 1 from Bhatt et al.
xp2 = {'arms': ['Par'] * 7, 'coef': [[2.5, 1], [2.8, 1], [4, 1], [3, 1], [1.4, 1], [1.9, 1], [1.4, 1.1]]}  # xp 2 from Bhatt et al.
xp3 = {'arms': ['Exp'] * 10, 'coef': [2.1, 2.4, 1.9, 1.3, 1.1, 2.9, 1.5, 2.2, 2.6, 1.4]}  # xp 3 from Bhatt et al.
xp4 = {'arms': ['G'] * 20, 'coef': [[1, sig] for sig in [1.64, 2.29, 1.79, 2.67, 1.70, 1.36, 1.90, 2.19,
                                                         0.80, 0.12, 1.65, 1.19, 1.88, 0.89, 3.35, 1.5, 2.22, 3.03, 1.08, 0.48]]}
xp5 = {'arms': ['st'] * 5, 'coef': [3.5, 3.6, 3.7, 2, 4]}  # xp 3 from Bhatt et al.
# xp5 = {'arms': ['Par'] * 3, 'coef': [[5, 1], [1.1, 1], [2, 1]]}  # xp 1 from Carpentier et Valko
# xp6 = {'arms': ['Par'] * 2 + ['Mixture'], 'coef': [[1.5, 1], [3, 1], [('Dirac', 'Par'), (0.8, 0.2), (0, [1.1, 1])]]}  # xp 2 from Carpentier & Valko
# xp7 = {'arms': ['LG'] * 5, 'coef': [[1, 4], [1.5, 3], [2, 2], [3, 1], [3.5, 0.5]]}
# xp8 = {'arms': ['GenNorm'] * 8, 'coef': [0.2 * i for i in range(1, 9)]}

names_xp = ['xp'+str(i+5)+'_' for i in range(1)]  # change both names_xp and xp_list if running less xp
xp_list = [xp5]#, xp2, xp3, xp4
algs = ['MaxMedian']  # Selection of algorithms to test , 'Threshold_Ascent'
# T_list = [1000, 2500, 5000, 7500, 10000, 15000, 20000, 30000, 50000]  # Selection of times from the paper
# T_list = [1000, 2000, 3000, 4000, 5000]  # Sx ub-selection of times for testing
T_list = np.linspace(10, 5000, num = 20, dtype=int)
# T_list = [1000, 5000]
if __name__ == '__main__':
    for i, xp in enumerate(xp_list):
        mc_counts = []
        mc_counts_eh = []
        for T in T_list:
            print(T)
            batch_size, sample_size = int(np.log(T)**2) + 1, int(np.log(T)) + 1
            args = (xp['arms'], xp['coef'], algs, m, T, params)
            # res = MC_Xtreme(args)
            res = MC_Xtreme(args)
            mc_count =  (res['MaxMedian'][0])
            all_counts =  (res['MaxMedian'][1])
            all_maxima =  (res['MaxMedian'][2])
            # mc_count_eh =  (res['ExtremeHunter'][0])
            mc_counts.append(100*mc_count[3]/T)
            # mc_counts_eh.append(100*mc_count_eh[5]/T)
            print(mc_count)
        file = open("mc_counts_hst", "wb")
        np.save(file, mc_counts)
        file.close
        t = np.linspace(10, 5000, num = 20)
        # f=interp1d(T_list, mc_counts)
        # f_eh=interp1d(T_list, mc_counts_eh)
        # smooth_mc = f(t)
        # smooth_mc_eh = f_eh(t)
        # with plt.style.context('Solarize_Light2'):

        #     fig, ax = plt.subplots()
        #     ax.plot(t, mc_counts, color='blue', label='max-median')
        #     ax.plot(t, mc_counts_eh, color='red', label='extremehunter')
        #     ax.grid(True, which='both')
        #     ax.set_xlabel("time")
        #     ax.set_ylabel("% Best Arm Pulls")

        #     # best_arm = mc_count.index(max(mc_count))
        #     # print(best_arm)plt.plot(x*0.1, y, 'o-', color='lightgrey', label='No mask')
        # plt.legend()
        # plt.show()
        # # print(mc_count)
            
        print('_________________________________________________________________')
