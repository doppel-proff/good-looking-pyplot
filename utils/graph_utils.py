from matplotlib import pyplot as plt

def pretty_ax(ax : plt.axes, font_color : str = "#000000") -> plt.axes:
    ax.grid(True, linestyle='-.')
    ax.tick_params(labelcolor= font_color, labelsize='medium', width=3)
    ax.legend(fontsize = 12, loc= "upper left")
    return ax