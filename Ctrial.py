import numpy as np
import pandas as pd
import urllib.request

#importing from csv file

urllib.request.urlretrieve('https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 
    'climate.txt')

#creating array
climate_data=np.genfromtxt('climate.txt',delimiter=',',skip_header=1)



weights = np.array([0.3, 0.2, 0.5])
yields=climate_data@weights

#adding yields to climate data
climate_results=np.concatenate((climate_data,yields.reshape(10000,1)),axis=1)

#convert back to csv file
np.savetxt('climate_results.csv', 
           climate_results, 
           fmt='%.2f', 
           delimiter=',',
           header='temperature,rainfall,humidity,yeild_apples', 
           comments=' ')

#fmt:formatting

final_results=np.genfromtxt('climate_results.txt',delimiter=',',skip_header=0)
print(final_results)

#printing out data hehe
data=pd.read_csv("climate_results.csv")
print(data)