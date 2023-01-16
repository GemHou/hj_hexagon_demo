import random
import math
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def in_hexagon(self):
        x = self.x
        y = self.y
        if y >= -sqrt(3) * x + sqrt(3) or y >= sqrt(3) * x + sqrt(3) or y <= -sqrt(3) * x - sqrt(3) or y <= sqrt(
                3) * x - sqrt(3) or y > sqrt(3) / 2 or y < -sqrt(3)/2:
            return False
        else:
            return True

    def plot(self, color="gx"):
        """
        if self.in_hexagon():
            plt.plot([self.x], [self.y], "gx")
        else:
            plt.plot([self.x], [self.y], "rx")
        """
        plt.plot([self.x], [self.y], color)


class Line:
    def __init__(self, k, b, x_range=None):
        self.k = k
        self.b = b
        self.x_range = x_range

    def plot(self, color="b"):
        if self.x_range is not None:
            x_list = self.x_range
        else:
            x_list = [-1, 1]
        y_list = [self.k*x_list[0]+self.b, self.k*x_list[1]+self.b]
        plt.plot(x_list, y_list, color)

    def intersection(self, new_line):
        solution_x = (new_line.b - self.b) / (self.k - new_line.k)
        if new_line.x_range is not None and (solution_x < new_line.x_range[0] or solution_x > new_line.x_range[1]):
            return None
        else:
            solution_y = self.k * solution_x + self.b
            return Node(solution_x, solution_y)

    def hexagon_length(self, hexagon_line_list):
        node_list = []
        for tmp_line in hexagon_line_list:
            tmp_node = self.intersection(tmp_line)
            if tmp_node is not None:
                tmp_node.plot(color="k+")
                node_list.append(tmp_node)
        assert len(node_list) == 2
        x1 = node_list[0].x
        y1 = node_list[0].y
        x2 = node_list[1].x
        y2 = node_list[1].y
        length = sqrt((x1 - x2)**2 + (y1 - y2)**2)
        return length


def main():
    line0 = Line(-sqrt(3), sqrt(3), x_range=[0.5, 1])
    line1 = Line(0, sqrt(3)/2, x_range=[-0.5, 0.5])
    line2 = Line(sqrt(3), sqrt(3), x_range=[-1, -0.5])
    line3 = Line(-sqrt(3), -sqrt(3), x_range=[-1, -0.5])
    line4 = Line(0, -sqrt(3)/2, x_range=[-0.5, 0.5])
    line5 = Line(sqrt(3), -sqrt(3), x_range=[0.5, 1])

    hexagon_line_list = [line0, line1, line2, line3, line4, line5]

    for tmp_line in hexagon_line_list:
        tmp_line.plot()

    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])
    # plt.show()

    length_list = []

    i = 0
    # for i in range(10):
    while True:
        x = random.random() * 2 - 1  # -1~1
        # print("x: ", x)
        y = random.random() * sqrt(3) - sqrt(3) / 2  # -sqrt(3)~sqrt(3)
        # print("y: ", y)
        node = Node(x, y)
        if node.in_hexagon():
            i += 1
            # print("node.x: ", node.x)
            # print("node.y: ", node.y)
            node.plot()

            theta = random.random() * 2 * math.pi - math.pi  # -pi~pi
            k = math.tan(theta)
            b = node.y - node.x * k
            tmp_line = Line(k, b)
            tmp_line.plot(color="g")

            length = tmp_line.hexagon_length(hexagon_line_list)
            assert length < 2
            assert length > 0
            length_list.append(length)
        if i % 1000 == 1:
            print("np.mean(length_list): ", np.mean(length_list))
    # plt.show()


if __name__ == '__main__':
    main()
