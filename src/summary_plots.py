import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from pathlib import Path


cwd=Path.cwd()
print(cwd)

def plot_instituteData(institute, parameter):
    folder_path = cwd / institute
    if folder_path.exists():
        #print("Directory exists")
        file_list = list(folder_path.glob("*.xlsx"))

    file_names = [file.stem for file in file_list]
    data = dict.fromkeys(file_names)

    for file in file_list:
        file_name = file.stem
        #print(f"Loading {file_name}")
        data[file_name] = pd.read_excel(file)

    prop=parameter
    d={}

    for name, path in data.items(): 
            #print(name)
            d[name]=data[name][prop]
        
    df=pd.DataFrame.from_dict(d)
    
    cm = 1/2.54
    fig, ax = plt.subplots(figsize=(4*cm, 10*cm))
    ax=sns.boxplot(data=df, showfliers=False)
    ax=sns.stripplot(data=df, jitter=True, marker='o', alpha=0.2, size=8, palette='dark:grey')
    return df, fig, ax

