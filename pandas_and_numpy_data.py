# Pandas Import and Export Data
import pandas as pandas
url = "http://apmonitor.com/pdc/uploads/Main/tclab_data2.txt"
data = pandas.read_csv(url)
data.to_csv("file.csv")

# Numpy Import and Export Data
import numpy as numpy
data = np.loadtxt("file.csv", delimiter=",", skiprows=1)
np.savetxt("file2.csv", data, delimiter=",",\ comments="", header="Index, Time, Q1, Q2, T1, T2")