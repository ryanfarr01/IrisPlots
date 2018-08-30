from matplotlib import pyplot as plt
import numpy as np
import csv

'''
Ryan Farr
rlf238

CS 5785 HW0

Citations
---------
Python CSV Docs: https://docs.python.org/3.7/library/csv.html
matplotlib Docs: https://matplotlib.org/contents.html

Data format
-----------
<sepal length(cm), sepal width(cm), petal length (cm), petal width (cm), class>
'''


def read_data():
    """ read_data function

    Reads the CSV data stored in 'iris.data' and returns it as an Nxp
    matrix, where N is the number of samples and p is the number of features
    as well as a list of labels.

    Returns
    -------
    Tuple (Nxp Matrix, list)
    """
    filename = 'iris.data'
    features = []
    labels = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            converted_row = [float(row[0]), float(row[1]),
                             float(row[2]), float(row[3])]
            features.append(np.array(converted_row))
            labels.append(row[4])
    return (np.array(features), labels)


def plot_data(data):
    """ plot_data function

    Creates the six iris data plots.

    Arguments
    ---------
    data : (Nxp Matrix, list)
        The iris data.
    """
    create_plot(data, 0, 1, 'Sepal Length (cm)',
                'Sepal Width (cm)', 'Sepal Width vs. Sepal Length')
    create_plot(data, 0, 2, 'Sepal Length (cm)',
                'Petal Length (cm)', 'Petal Length vs. Sepal Length')
    create_plot(data, 0, 3, 'Sepal Length (cm)',
                'Petal Width (cm)', 'Petal Width vs. Sepal Length')
    create_plot(data, 1, 2, 'Sepal Width (cm)',
                'Petal Length (cm)', 'Petal Length vs. Sepal Width')
    create_plot(data, 1, 3, 'Sepal Width (cm)',
                'Petal Width (cm)', 'Petal Width vs. Sepal Width')
    create_plot(data, 2, 3, 'Petal Length (cm)',
                'Petal Width (cm)', 'Petal Width vs. Petal Length')


def create_plot(data, x_index, y_index, x_label, y_label, plot_label):
    """ create_plot

    Creates and saves a single plot.

    Arguments
    ---------
    data : (Nxp Matrix, list)
        The iris data.
    x_index : int
        The column index for the x-axis.
    y_index : int
        The column index for the y-axis.
    x_label : str
        Description of the x-axis.
    y_label : str
        Description of the y-axis.
    plot_label : str
        Title of the plot and filename for the saved image.
    """
    # get the x axis, y axis, and colors
    features = data[0]
    labels = data[1]
    cols = []
    for row in labels:
        if row == 'Iris-setosa':
            cols.append('r')
        elif row == 'Iris-versicolor':
            cols.append('g')
        else:
            cols.append('b')

    # create the scatter plot
    plt.scatter(features[:, x_index], features[:, y_index], c=cols)

    # put in labels and save
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(plot_label)
    plt.savefig(plot_label + ".png")


if __name__ == '__main__':
    data = read_data()
    plot_data(data)
