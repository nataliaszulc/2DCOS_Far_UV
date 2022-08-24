import ploter
import calculations
import os

path = 'data/'
dir_list = os.listdir(path)

file = dir_list[0]

#for file in dir_list:
inputfile = path + file
sync, asyn = calculations.correlation(inputfile)
ploter.combine_plots(sync, asyn, inputfile)