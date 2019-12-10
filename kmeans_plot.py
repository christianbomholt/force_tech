import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from plotly.offline import iplot
from plotly.offline import iplot,init_notebook_mode
init_notebook_mode
init_notebook_mode(connected=True)
pio.templates.default = "none"

def kmeans_plot(points,k,iter,initialize_centers,closest_centroid,move_centroids):
    # make figure
    fig_dict = {
        "data": [],
        "layout": {},
        "frames": []
    }
    # fill in most of layout
    fig_dict["layout"]["xaxis"] = {"range": [-1.5, 3], "title": "X1"}
    fig_dict["layout"]["yaxis"] = {"range": [-2, 3], "title": "Y1"}
    fig_dict["layout"]["hovermode"] = "closest"

    fig_dict["layout"]["updatemenus"] = [
        {
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 500, "redraw": False},
                                    "fromcurrent": True, "transition": {"duration": 300,
                                                                        "easing": "quadratic-in-out"}}],
                    "label": "Play",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                    "mode": "immediate",
                                    "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate"
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top"
        }
    ]

    # make data
    centroids = initialize_centers(points, k)
    closest = closest_centroid(points, centroids)

    data_dict = {
        "x": list(points[:, 0])+list(centroids[:, 0]),
        "y": list(points[:, 1])+list(centroids[:, 1]),
        "mode": "markers",
        "marker": {
            "sizemode": "area",
            "sizeref": 200000,
            "size": 8,
            "color": list(closest)+[4,4,4]
        }
    }
    fig_dict["data"].append(data_dict)

    for iter_ in range(iter):
        frame = {"data": [], "name": str(iter_)}
        closest = closest_centroid(points, centroids)
        centroids = move_centroids(points, closest, centroids)

        data_dict = {
        "x": list(points[:, 0])+list(centroids[:, 0]),
        "y": list(points[:, 1])+list(centroids[:, 1]),
        "mode": "markers",
        "marker": {
            "sizemode": "area",
            "sizeref": 200000,
            "size": 8,
            "color": list(closest)+[4,4,4]
            }
        #     name: "centroids"
        }
        frame["data"].append(data_dict)

        fig_dict["frames"].append(frame)


    return go.Figure(fig_dict)
