import plotly.figure_factory as ff
import pandas as pd
import csv

df= pd.read_csv("classs108data.csv")
fig= ff.create_distplot([df["Height(Inches)"].tolist()],["Height"], show_hist= True)
fig.show()