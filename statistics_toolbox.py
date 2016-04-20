# the product is only as good as the process that produces it. - W. Edwards 
# Deming
# (c) 2016 Thomas Umhau
# Created for straightforward analysis of processes in the most efficient manner 
# possible.
# 
# include the list of Murphy's laws and corollaries as an easter egg. 
# eventually, also output data as .png or latex

import numpy
import bashplotlib

#import statistics

# ----------------------------------------------------------------------------- #

A_rank = [0.8,0.4,1.2,3.7,2.6,5.8]
#B_rank = [0.1,2.8,3.7,2.6,5,3.4]
#C_rank = [1.2,3.4,0.5,0.1,2.5,6.1]

#print(statistics.stdev(A_rank))

def control_chart(data):

	# ddof=0 (default, interprete data as population) or ddof=1 (interprete it as
    # samples, i.e. estimate true variance)

	arr = numpy.array([data])

	#numpy.mean(arr, axis=0)

	# returns standard deviation. Source: 
    # http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.std.html

	numpy.std(arr, axis=0, ddof=1)


# ----------------------------------------------------------------------------- #
def precontrol():
    # time between stoppages / 6 = how often you need to sample
    # use precontrol when you have sigma up to 4.5, a Cpk index of (4.5?)
    pass

    # show histogram;
    # took two readings, so data looks like this: [[a,b],[a,b],etc]
    # plot on precontrol chart. 
    # look for outliers:
    #     two reds, or two yellows in opposite zones = investigation

data = [
    [3.56, 3.50],
    [3.48, 3.52],
    [3.41, 3.49],
    [3.55, 3.50],
    [3.48, 3.40]
    ]

data = [
    3.56,
    3.48,
    3.41,
    3.55,
    3.48,
    5.0
    ]

from bashplotlib.histogram import plot_hist as ph
# from bashplotlib.histogram import run_demo as d
ph('ycoordinates.txt')
# d()

# ----------------------------------------------------------------------------- #





