from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("<h1>The Fett homepage</h1>")
    fett = "The is a python varable"
    return render(request, 'fett/fett_home.html', {'fett' : fett})

def plotResults(request):
    import matplotlib
    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    import numpy as np
    x = np.arange(0, 10, 1)
    y = np.sin(x)

    fig = Figure()
    ax=fig.add_subplot(1,1,1)

    ax.plot(x, y)

    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')

    canvas.print_png(response)
    return response
