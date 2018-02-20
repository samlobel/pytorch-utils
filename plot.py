import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class MultiGraphPlotter(object):
    def __init__(self, basedir, extension=".jpg"):
        self.basedir = basedir
        self.graph_dict = {}
        self.extension = extension


    def add_point(self, graph_name=None, value=None, bin_name=None):
        if None in [graph_name, value, bin_name]:
            raise Exception("Argument not provided to add point in MultiGraphPlotter")

        if graph_name not in self.graph_dict:
            self.graph_dict[graph_name] = MultiLinePlotter(graph_name, self.extension)

        self.graph_dict[graph_name].add_point(value=value, bin_name=bin_name)

    def graph_all(self):
        for name, plotter in self.graph_dict.items():
            plotter.graph_points(location=os.path.join(self.basedir, name))

class MultiLinePlotter(object):
    def __init__(self, location, extension=".jpg"):
        super().__init__()
        self.location = location
        self.point_tracker = collections.defaultdict(list)
        self.extension = extension


    def add_point(self, value=None, bin_name=None):
        if None in [value, bin_name]:
            raise Exception("Argument not provided to add_point in MultiLinePlotter")
        self.point_tracker[bin_name].append(value)

    def graph_points(self, location=None):
        location = location or self.location
        _make_dir(location)
        plt.clf()

        for key, vals in self.point_tracker.items():
            x_vals, y_vals = zip(*enumerate(vals))
            line = plt.plot(x_vals, y_vals, label=key)

        plt.legend()
        true_loc = location.replace(' ', '_') + self.extension
        plt.savefig(true_loc)
