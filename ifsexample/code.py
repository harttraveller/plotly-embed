import random
import numpy as np
import plotly.graph_objects as go
from .env import SIMPLEX
from .template import MINIMAL


def sierpinski(n: int, dim: int) -> list[list[float]]:
    """
    Runs chaos game to generate n-dimensional [1, 4] sierpinski simplex.

    Args:
        n (int): number of points to generate
        dim (int): [1, 4] dimensionality of output simplex

    Returns:
        np.matrix: output point matrix
    """
    e, p = SIMPLEX[dim], [np.zeros(dim)]
    for i in range(n):
        p.append(((p[i] + random.choice(e)) / 2))
    return np.matrix(p)


def visualize(
    points, save=None, camera=None, width=480, height=480, xaxis=None, yaxis=None
):
    if isinstance(points, np.matrix):
        points = points.tolist()
    a, b, c, d = list(zip(*points))
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=d,
                y=b,
                z=c,
                mode="markers",
                marker=dict(
                    size=1.5,
                    color=a,  # set color equal to a variable
                    colorscale="Viridis",  # one of plotly colorscales
                    showscale=False,
                    reversescale=True,
                ),
                hoverinfo="skip",
            )
        ]
    )
    fig.update_layout(
        template=MINIMAL,
        autosize=False,
        width=width,
        height=height,
        margin=dict(l=10, r=10, b=10, t=10, pad=0),
    )
    if xaxis is not None:
        fig.update_xaxes(range=xaxis)
    if yaxis is not None:
        fig.update_xaxes(range=yaxis)
    if camera is None:
        camera = dict(
            up=dict(x=0, y=0, z=1), center=dict(x=0, y=0, z=0), eye=dict(x=0, y=2.5, z=0)
        )
    fig.update_layout(scene_camera=camera)
    if save is not None:
        fig.write_html(save)
    else:
        fig.show()
