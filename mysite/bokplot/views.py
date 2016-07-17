from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>The Fett homepage</h1>")
    return render(request, 'bokplot/index.html', {})

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components

def simple_chart(request):
    plot = figure()
    import numpy as np
    # x = np.arange(-10,10,0.1)
    # y = np.arange(-10,10,0.1)
    # plot.circle([1,2], [3,4])
    script, div = components(plot, CDN)


    tp, hp = np.loadtxt('/Users/sebastian/phd/data/phenEOB-data/phenP/hp.dat').T
    tc, hc = np.loadtxt('/Users/sebastian/phd/data/phenEOB-data/phenP/hc.dat').T

    # select the tools we want
    # TOOLS="reset,pan,wheel_zoom,box_zoom,save"


    # p1 = figure(tools=TOOLS, plot_width=300*2, plot_height=300)
    p1 = figure(plot_width=300*2, plot_height=300)
    p1.line(tp, hp, color="red", alpha=0.5)

    # p2 = figure(tools=TOOLS, plot_width=300*2, plot_height=300, x_range=p1.x_range, y_range=p1.y_range,)
    p2 = figure(plot_width=300*2, plot_height=300, x_range=p1.x_range, y_range=p1.y_range,)
    p2.line(tc, hc, color="blue", alpha=0.5)
    from bokeh.plotting import gridplot
    p = gridplot([[p1],[p2]])

    # plots = {'Red': p1, 'Blue': p2}

    # script, div = components(plots)
    script, div = components(p)

    return render(request, "bokplot/simple_chart.html", {"the_script": script, "the_div": div})


def simple_chart_same_axis(request):
    plot = figure()
    import numpy as np
    # x = np.arange(-10,10,0.1)
    # y = np.arange(-10,10,0.1)
    # plot.circle([1,2], [3,4])
    script, div = components(plot, CDN)


    tp, hp = np.loadtxt('/Users/sebastian/phd/data/phenEOB-data/phenP/hp.dat').T
    tc, hc = np.loadtxt('/Users/sebastian/phd/data/phenEOB-data/phenP/hc.dat').T

    # select the tools we want
    TOOLS="pan,wheel_zoom,box_zoom,reset,save"


    p1 = figure(tools=TOOLS, plot_width=300*4, plot_height=300*2)
    p1.line(tp, hp, color="red", alpha=0.5)
    p1.line(tc, hc, color="blue", alpha=0.5)

    script, div = components(p1, CDN)

    return render(request, "bokplot/simple_chart.html", {"the_script": script, "the_div": div})

def simple_chart_2(request):

    from bokeh.plotting import figure
    from bokeh.models import Range1d
    from bokeh.embed import components

    # create some data
    x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [0, 8, 2, 4, 6, 9, 5, 6, 25, 28, 4, 7]
    x2 = [2, 5, 7, 15, 18, 19, 25, 28, 9, 10, 4]
    y2 = [2, 4, 6, 9, 15, 18, 0, 8, 2, 25, 28]
    x3 = [0, 1, 0, 8, 2, 4, 6, 9, 7, 8, 9]
    y3 = [0, 8, 4, 6, 9, 15, 18, 19, 19, 25, 28]

    # select the tools we want
    TOOLS="pan,wheel_zoom,box_zoom,reset,save"

    # the red and blue graphs will share this data range
    xr1 = Range1d(start=0, end=30)
    yr1 = Range1d(start=0, end=30)

    # only the green will use this data range
    xr2 = Range1d(start=0, end=30)
    yr2 = Range1d(start=0, end=30)

    # build our figures
    p1 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_width=300, plot_height=300)
    p1.scatter(x1, y1, size=12, color="red", alpha=0.5)

    p2 = figure(x_range=xr1, y_range=yr1, tools=TOOLS, plot_width=300, plot_height=300)
    p2.scatter(x2, y2, size=12, color="blue", alpha=0.5)

    p3 = figure(x_range=xr2, y_range=yr2, tools=TOOLS, plot_width=300, plot_height=300)
    p3.scatter(x3, y3, size=12, color="green", alpha=0.5)

    # plots can be a single PlotObject, a list/tuple, or even a dictionary
    plots = {'Red': p1, 'Blue': p2, 'Green': p3}

    script, div = components(plots)

    return render(request, "bokplot/simple_chart.html", {"the_script": script, "the_div": div})
