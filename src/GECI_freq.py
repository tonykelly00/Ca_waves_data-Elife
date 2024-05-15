# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:26:02 2023

@author: Tony Kelly
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import integrate

import os


os.chdir('../data')
print("File location using os.getcwd():", os.getcwd())

def main():
    # Import and organize data
    file_name = 'CaWaves_overview.xlsx'
    
    cell = pd.read_excel(file_name)
     
    return cell

if __name__ == "__main__":
    cell=main()
