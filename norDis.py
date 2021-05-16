import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
count=[]
mathScore=[]

pf=pd.read_csv("data.csv")

mean= sum(mathScore)/len(mathScore)
stddev=statistics.stdev(mathScore)
mode=statistics.mode(mathScore)
median=statistics.median(mathScore)

first_stddev_start=mean-1*stddev
first_stddev_end=mean+1*stddev
second_stdev_start=mean-2*stddev
second_stdev_end=mean+2*stddev
third_stdev_start=mean-3*stddev
third_stdev_end=mean+3*stddev

list_of_data_within_1_std_deviation = [result for result in dice_result if result > first_stddev_start and result < first_stddev_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
print(mean)
print(median)
print(mode)
print(stddev)
fig=ff.create_distplot([dice_result],['Result'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_stddev_start, first_stddev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_stddev_end, first_stddev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_stddev_start, first_stddev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_stddev_end, first_stddev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[third_stddev_start, first_stddev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[third_stddev_end, first_stddev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))

fig.show()