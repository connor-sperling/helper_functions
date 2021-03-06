import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def rename_files(path):
    """
    Currently, to remove a common string for many folders
    """
    part_folders = [i for i in os.listdir(results_path) if i.startswith('PASS') or i.startswith('FAIL')]
    for fld in part_folders:
        old_name = os.path.join(path,fld)
        new_name = os.path.join(path,'_'.join(fld.split('_')[1:]))

def num_files(path, screening_test):
    part_folders = [i for i in os.listdir(results_path) if i.startswith('PN')]
    for fld in part_folders:
        print(len(os.listdir(os.path.join(path, fld, screening_test))))

def save_dict_csv(data, path):
    data_df = pd.DataFrame.from_dict(data)
    data_df.to_csv(path, index=False)


def sort_files(filenames, path, method='time', sort='earliest'):
    if method == 'time' and sort == 'earliest':
        times = []
        unordered_list = []
        for f in filenames:
            times.append(os.stat(os.path.join(path, f)).st_ctime)
            unordered_list.append(f)
    return (unordered_list, times)    


def plot_fir(b, nyq):
    fig, ax = plt.subplots()
    for row in range(b.shape[0]):
        w, h = signal.freqz(b[row,:], [1])
        f = (w/np.pi)*nyq
        ax.plot(f, 20 * np.log10(abs(h)))
    ax.grid()


if __name__ == '__main__':


    """
    plot_fir:
        - plots FIR transfer functions on same plot
        - :param b: must be a numpy ndarray
            - impulse responses entered as rows
    """
    # b = np.zeros((5,50))
    # b[0,:] = np.array([-0.002106, 0.004378, -0.012032, 0.029883, -0.028465, 0.007858, 0.047056, -0.146993, 0.403520, -1.019856, 3.544822, -1.621523, -0.009617, 0.076008, -0.112945, -0.034440, 0.027466, -0.032429, -0.029626, 0.073208, -0.112311, 0.047091, -0.005626, -0.057679, 0.051338, -0.016895, -0.037539, 0.055665, -0.084572, 0.066815, -0.050282, 0.027860, -0.013075, 0.000743, -0.012403, 0.015195, -0.024146, 0.018186, -0.010577, -0.015554, 0.018869, -0.019355, -0.001908, 0.016203, -0.018010, 0.007818, -0.001455, -0.002166, -0.002677, -0.003721])
    # b[1,:] = np.array([-0.000463, -0.005508, 0.000431, 0.001879, 0.008185, -0.031064, 0.093639, -0.236445, 0.581115, -1.321835, 3.343456, -0.943206, -0.300890, 0.096126, -0.096481, -0.087747, 0.067109, -0.050112, -0.033139, 0.061740, -0.085225, 0.023887, 0.004181, -0.039129, 0.038633, -0.027341, -0.010812, 0.024584, -0.040462, 0.044869, -0.048047, 0.025207, -0.006001, -0.022293, 0.015888, -0.004437, -0.020028, 0.021052, -0.014563, -0.020664, 0.043783, -0.066485, 0.040778, -0.004864, -0.016993, 0.015972, -0.005015, -0.017902, 0.023279, -0.018642])
    # b[2,:] = np.array([0.010335, -0.005526, -0.007501, 0.014228, -0.017976, 0.004247, 0.056791, -0.226823, 0.580942, -1.339410, 3.359566, -0.902096, -0.327148, 0.106064, -0.106860, -0.085254, 0.048451, -0.032861, -0.016618, 0.032240, -0.059325, 0.013647, 0.008339, -0.037925, 0.035150, -0.045273, 0.001530, 0.016191, -0.044697, 0.042695, -0.035220, -0.000356, 0.006995, -0.011621, -0.015790, 0.028806, -0.049800, 0.040706, -0.026311, 0.000604, -0.005720, -0.018158, 0.021383, 0.006149, -0.013131, 0.013826, -0.001065, -0.015444, 0.010398, -0.011375])
    # b[3,:] = np.array([-0.000598, 0.000595, -0.001348, -0.003296, 0.005588, -0.015971, 0.036479, -0.085960, 0.190966, -0.412617, 0.976658, 0.107052, 0.081588, 0.083695, 0.033961, -0.006214, 0.037003, 0.001556, -0.000635, 0.021794, -0.010639, 0.003202, 0.002698, -0.008177, 0.009005, -0.006171, -0.001676, 0.006807, -0.014904, 0.014933, -0.011126, -0.002236, 0.004412, -0.005031, -0.004210, 0.004893, -0.006754, 0.000594, -0.000545, -0.007634, 0.003750, -0.012413, 0.001452, 0.000865, -0.005105, 0.006928, -0.005184, -0.004581, 0.009015, -0.012464])
    # b[4,:] = np.array([-0.000717, 0.000833, -0.001393, -0.003383, 0.005750, -0.016547, 0.037542, -0.088507, 0.195182, -0.421572, 0.987265, 0.140288, 0.098946, 0.097666, 0.041533, -0.004789, 0.035086, -0.001251, -0.005993, 0.016359, -0.016105, -0.002788, -0.003191, -0.013591, 0.003783, -0.010512, -0.005855, 0.003747, -0.018547, 0.012562, -0.013449, -0.004800, 0.002498, -0.006755, -0.006241, 0.003972, -0.007438, -0.000647, -0.000951, -0.007992, 0.002675, -0.012455, 0.000478, 0.000702, -0.005496, 0.007144, -0.004846, -0.004763, 0.009443, -0.012880])
    # plot_fir(b, 26.5625)
    # plt.show()
