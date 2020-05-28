from netCDF4 import Dataset as cdf4_ds

import numpy as np

from code_intern import plot_function as plt_int
from code_intern import Analyse_data as Ana_data
try:
    import cPickle as pickle
except ImportError:  # python 3.x
    import pickle



def get_mean_calc(data):
    tempe_moy = np.mean(data['tas'][:, :, :], axis=0)
    with open('../Stock_array/Array_mean_temp', 'wb') as fp:
        pickle.dump(tempe_moy, fp, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    "plot temps simulation"

    tas_nc_file = cdf4_ds('/Users/olivier1/Documents/Data_stage/tas_CA_Rockies_3km_P3_ERA5-1h_ISBA_USGS.nc')
    # print(tas_nc_file.variables)
    # plt_int.plot_graph(tas_nc_file,event=True,save=True).__call__()

    Ana_data.data_site('Alldata.csv',tas_nc_file).__call__()

