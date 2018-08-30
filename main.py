from matplotlib import pyplot as plt
import csv

'''
Ryan Farr
rlf238

CS 5785 HW0

Citations:
Python CSV Docs: https://docs.python.org/3.7/library/csv.html
matplotlib Docs: https://matplotlib.org/contents.html

Data format: sepal length(cm), sepal width(cm), petal length (cm), petal width (cm), class
'''


def read_data():
    filename = 'iris.data'
    data = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            converted_row = [float(row[0]), float(
                row[1]), float(row[2]), float(row[3]), row[4]]
            data.append(converted_row)
    return data


def plot_data(data):
    create_plot(data, 0, 1, 'Sepal Length (cm)',
                'Sepal Width (cm)', 'Sepal Width vs. Sepal Length', 1)
    create_plot(data, 0, 2, 'Sepal Length (cm)',
                'Petal Length (cm)', 'Petal Length vs. Sepal Length', 2)
    create_plot(data, 0, 3, 'Sepal Length (cm)',
                'Petal Width (cm)', 'Petal Width vs. Sepal Length', 3)
    create_plot(data, 1, 2, 'Sepal Width (cm)',
                'Petal Length (cm)', 'Petal Length vs. Sepal Width', 4)
    create_plot(data, 1, 3, 'Sepal Width (cm)',
                'Petal Width (cm)', 'Petal Width vs. Sepal Width', 5)
    create_plot(data, 2, 3, 'Petal Length (cm)',
                'Petal Width (cm)', 'Petal Width vs. Petal Length', 6)


def create_plot(data, x_index, y_index, x_label, y_label, plot_label, plot_num):
    # get the x axis, y axis, and colors
    xs = [d[x_index] for d in data]
    ys = [d[y_index] for d in data]
    cols = []
    for row in data:
        if row[4] == 'Iris-setosa':
            cols.append('r')
        elif row[4] == 'Iris-versicolor':
            cols.append('g')
        elif row[4] == 'Iris-virginica':
            cols.append('b')

    # create the scatter plot
    plt.scatter(xs, ys, c=cols)

    # put in labels and save
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(plot_label)
    plt.savefig(plot_label + ".png")
    plt.show()


if __name__ == '__main__':
    data = read_data()
    plot_data(data)
