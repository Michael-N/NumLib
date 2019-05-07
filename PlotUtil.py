'''
# PlottingUtil
- Code By Michael Sherif Naguib
- license: (see LICENSE file)
- Date: 5/5/2019
- @University of Tulsa
- Description: This is a class that uses other plotting software to make
               it more convenient for plotting...2.0 added support for slower matplotlib
'''
#imports
from datashader import transfer_functions as tf
from datashader.colors import inferno, viridis
from colorcet import palette
import bokeh.plotting as bp
from datashader.bokeh_ext import InteractiveImage
import numpy as np, pandas as pd, datashader as ds
import matplotlib.pyplot as plt
import random


#setup
palette["viridis"]=viridis
palette["inferno"]=inferno

# a class for plotting the points
class PlotUtil():
    def __init__(self,point_data,plot_w=500,plot_h=500,colormap=inferno):
        #store the point data
        self.point_data = point_data
        #dimensions
        self.plot_height = plot_h
        self.plot_width = plot_w
        #prepare the data
        self.prepare_data()
        #color
        self.colormap = colormap
    #Puts the data into a dataframe
    def prepare_data(self):
        self.df_data = pd.DataFrame(dict(x=np.array(self.point_data[0]),y=np.array(self.point_data[1])))
    #sets new data
    def set_data(self,point_data):
        self.point_data=point_data
        self.prepare_data()
    #image callback: this funtion returns a curried function for interactive image plotting
    def image_callback(self):
        def callback(x_range, y_range, w, h, name=None):
            # setup a plot
            cvs = ds.Canvas(plot_width=w, plot_height=h, x_range=x_range, y_range=y_range)
            agg = cvs.points(self.df_data, 'x', 'y')
            img = tf.shade(agg, cmap=self.colormap, name=None)
            return img
        return callback
    #creates a bokeh interactive plot for the data
    def interactive_plot(self):
        bp.output_notebook()
        p = bp.figure(tools='pan,wheel_zoom,reset', x_range=(-5, 5), y_range=(-5, 5), \
            plot_width=self.plot_width, plot_height=self.plot_height,background_fill_color='black')
        return InteractiveImage(p, self.image_callback())
    @staticmethod
    def plot(data,x_name="x",y_name="y",title="Graph"):
        #setup
        plt.title(title)
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.scatter(data['data'][0], data['data'][1], c=[(random.random(),random.random(),random.random())], s=np.pi * 3, alpha=0.5, label=data['name'])
        plt.legend(loc='upper left');
        plt.show()
    # Plotting Code: Passed a series list [series1,series2] where series {name:"",x:[],y:[]}
    # NOTE! CAN ONLY PLOT 3 colors before it starts using random values for colors
    @staticmethod
    def plotSeries(series, x_name="x", y_name="y", title="Graph", x_key='x',y_key='y'):  # Code adapted from my chaotic IFS project
        colors = [(70 / 255, 240 / 255, 240 / 255), (240 / 255, 50 / 255, 230 / 255), (210 / 255, 245 / 255, 60 / 255)]
        plt.title(title)
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        idx = 0
        r = random.random
        for group in series:
            # Plot the points
            plt.scatter(group[x_key], group[y_key], c=[colors[idx] if idx < len(colors) else (r(), r(), r())],
                        s=np.pi * 3, alpha=0.5, label=group['name'])
            idx += 1
        plt.legend(loc='upper left')
        plt.show()