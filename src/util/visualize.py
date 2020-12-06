import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("./data/results_vader.csv")
print(df["polarity"].describe())

nyt_df = df[df["source"] == "The New York Times"]
fox_df = df[df["source"] == "Fox News"]
mond_df = df[df["source"] == "Mondoweiss"]
honrep_df = df[df["source"] == "HonestReporting"]

nyt_pos_df = nyt_df[nyt_df["sentiment"] == "positive"]
fox_pos_df = fox_df[fox_df["sentiment"] == "positive"]
mond_pos_df = mond_df[mond_df["sentiment"] == "positive"]
honrep_pos_df = honrep_df[honrep_df["sentiment"] == "positive"]

nyt_neg_df = nyt_df[nyt_df["sentiment"] == "negative"]
fox_neg_df = fox_df[fox_df["sentiment"] == "negative"]
mond_neg_df = mond_df[mond_df["sentiment"] == "negative"]
honrep_neg_df = honrep_df[honrep_df["sentiment"] == "negative"]

nyt_neut_df = nyt_df[nyt_df["sentiment"] == "neutral"]
fox_neut_df = fox_df[fox_df["sentiment"] == "neutral"]
mond_neut_df = mond_df[mond_df["sentiment"] == "neutral"]
honrep_neut_df = honrep_df[honrep_df["sentiment"] == "neutral"]

def viz_basic():
    x_axis = ["negative", "neutral", "positive"]
    nyt_y_axis = [len(nyt_neg_df), len(nyt_neut_df), len(nyt_pos_df)]
    fox_y_axis = [len(fox_neg_df), len(fox_neut_df), len(fox_pos_df)]
    mond_y_axis = [len(mond_neg_df), len(mond_neut_df), len(mond_pos_df)]
    honrep_y_axis = [len(honrep_neg_df), len(honrep_neut_df), len(honrep_pos_df)]

    plt.subplot(1,4,1)
    plt.title("NYT")
    plt.bar(x_axis, nyt_y_axis)

    plt.subplot(1,4,2)
    plt.title("FOX")
    plt.bar(x_axis, fox_y_axis)

    plt.subplot(1,4,3)
    plt.title("Mondoweiss")
    plt.bar(x_axis, mond_y_axis)

    plt.subplot(1,4,4)
    plt.title("HonestReporting")
    plt.bar(x_axis, honrep_y_axis)

    plt.show()

def plot_stacked_bar(data, series_labels, category_labels=None, 
                     show_values=False, value_format="{}", y_label=None, 
                     colors=None, grid=False, reverse=False):
    """Plots a stacked bar chart with the data and labels provided.

    Keyword arguments:
    data            -- 2-dimensional numpy array or nested list
                       containing data for each series in rows
    series_labels   -- list of series labels (these appear in
                       the legend)
    category_labels -- list of category labels (these appear
                       on the x-axis)
    show_values     -- If True then numeric value labels will 
                       be shown on each bar
    value_format    -- Format string for numeric value labels
                       (default is "{}")
    y_label         -- Label for y-axis (str)
    colors          -- List of color labels
    grid            -- If True display grid
    reverse         -- If True reverse the order that the
                       series are displayed (left-to-right
                       or right-to-left)
    """

    ny = len(data[0])
    ind = list(range(ny))

    axes = []
    cum_size = np.zeros(ny)

    data = np.array(data)

    if reverse:
        data = np.flip(data, axis=1)
        category_labels = reversed(category_labels)

    for i, row_data in enumerate(data):
        color = colors[i] if colors is not None else None
        axes.append(plt.bar(ind, row_data, bottom=cum_size, 
                            label=series_labels[i], color=color))
        cum_size += row_data

    if category_labels:
        plt.xticks(ind, category_labels)

    if y_label:
        plt.ylabel(y_label)

    plt.legend()

    if grid:
        plt.grid()

    if show_values:
        for axis in axes:
            for bar in axis:
                w, h = bar.get_width(), bar.get_height()
                plt.text(bar.get_x() + w/2, bar.get_y() + h/2, 
                         value_format.format(h), ha="center", 
                         va="center")

def viz_stacked():
    plt.figure(figsize=(6, 4))

    series_labels = ['Negative', 'Neutral', 'Positive']

    data = [
        [len(nyt_neg_df), len(fox_neg_df), len(mond_neg_df), len(honrep_neg_df)],
        [len(nyt_neut_df), len(fox_neut_df), len(mond_neut_df), len(honrep_neut_df)],
        [len(nyt_pos_df), len(fox_pos_df), len(mond_pos_df), len(honrep_pos_df)]
    ]


    category_labels = ['The New York Times', 'Fox News', 'Mondoweiss', 'HonestReporting']

    plot_stacked_bar(
        data, 
        series_labels, 
        category_labels=category_labels, 
        show_values=False, 
        value_format="{:.1f}",
        colors=['red', 'orange', 'green'],
        y_label="Quantity (units)"
    )

    plt.show()

def multi_axis():
    from mpl_toolkits.axes_grid1 import host_subplot
    import mpl_toolkits.axisartist as AA
    import matplotlib.pyplot as plt

    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)

    par1 = host.twinx()
    par2 = host.twinx()
    par3 = host.twinx()

    offset = 50
    new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    par2.axis["right"] = new_fixed_axis(loc="right",
                                        axes=par2,
                                        offset=(offset, 0))

    par2.axis["right"].toggle(all=True)

    offset_3 = 100
    new_fixed_axis_3 = par3.get_grid_helper().new_fixed_axis
    par3.axis["right"] = new_fixed_axis_3(loc="right",
                                        axes=par3,
                                        offset=(offset_3, 0))

    par3.axis["right"].toggle(all=True)

    # host.set_xlim(0, 2)
    # host.set_ylim(0, 2)

    host.set_xlabel("News Source")
    host.set_ylabel("NYT")
    par1.set_ylabel("Fox")
    par2.set_ylabel("Mond")
    par3.set_ylabel("HR")

    p1, = host.plot([0, 1, 2], [10, 1, 20], label="NYT")
    p2, = par1.plot([0, 1, 2], [20, 30, 22], label="Fox")
    p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Mond")
    p4, = par3.plot([0, 1, 2], [40, 20, 10], label="HR")

    # par1.set_ylim(0, 4)
    # par2.set_ylim(1, 65)

    host.legend()

    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())
    par2.axis["right"].label.set_color(p3.get_color())
    par3.axis["right"].label.set_color(p4.get_color())

    plt.draw()
    plt.show()

# multi_axis()

data = [
        [len(nyt_neg_df), len(fox_neg_df), len(mond_neg_df), len(honrep_neg_df)],
        [len(nyt_neut_df), len(fox_neut_df), len(mond_neut_df), len(honrep_neut_df)],
        [len(nyt_pos_df), len(fox_pos_df), len(mond_pos_df), len(honrep_pos_df)]
    ]

print(data)