# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:26:02 2023

@author: Tony Kelly
"""
import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import integrate

import os
import glob

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

os.chdir('../data')
print("File location using os.getcwd():", os.getcwd())



def main():
    # Import and organize data
    file_name = 'CaWaves_overview.xlsx'
    
    #organized_gamma_data = organize_gamma_data(gamma_data)
    
    cell = pd.read_excel(file_name)
    
    
     ###Plot initial EPSP v stim int
    #plot_initial_EPSP(gamma_data)
    
        # Set x and y limits
    # plt.xlim([0, 500])  # Adjust the limits according to your data
    # plt.ylim([0, 15])  # Adjust the limits according to your data

    # Set x and y ticks
    # plt.xticks(range(0,501,100))
    # plt.yticks(range(0,16,5))
    # Save the plot
    # plt.savefig(desktop + '/Initial_StimInt.svg',
    #             bbox_inches='tight', format='svg')
    # plt.show()
    
    
    
    return cell

if __name__ == "__main__":
    cell=main()
