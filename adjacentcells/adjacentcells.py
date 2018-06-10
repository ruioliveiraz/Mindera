import argparse
import json
import sys
import os


class adjacent_cells():
    def __init__(self, input):
        self.values = self.read_matrix(input)
        self.grid_len_x = len(self.values[0])
        self.grid_len_y = len(self.values)
        self.groups_of_nodes = []
        self.visited_nodes = []


    def read_matrix(self, input):
        """
        Method that opens the file that contains the 2D Matrix of cells.
        """
        with open(input) as f:
            values = json.load(f)
        cells = []
        for value in values:
            cells.append(value)
        return cells


    def find_adjacent_cells(self):
        """
        Method that iterates over all the cells in the matrix with value equal to one and for each one of them
        finds the corresponding adjacent cells.
        :return: list of adjacent cells
        """
        for y in range(self.grid_len_y):
            for x in range(self.grid_len_x):
                self.find_cells(y, x)
                if len(self.groups_of_nodes) > 1:
                    print(sorted(self.groups_of_nodes))
                self.groups_of_nodes = []


    def find_cells(self, y_coord,  x_coord):
        """
        Method that recursively finds all the adjacent cells of a given a cell.
        The next cell to find is made according to the position of the given cell.
        :param y_coord: y coordinate of the cell (grid line)
        :param x_coord: x coordinate of the cell (grid column)
        """
        if [y_coord, x_coord] not in self.visited_nodes and self.values[y_coord][x_coord]:
            self.groups_of_nodes.append([y_coord, x_coord])  #list of adjacent cells
            self.visited_nodes.append([y_coord,x_coord])  #list of cells that have already been visited

            if x_coord == 0:
                self.find_cells(y_coord, x_coord + 1) #find right adjacent cells

            if x_coord == self.grid_len_x-1:
                self.find_cells(y_coord, x_coord - 1) #find left adjacent cells

            if y_coord == 0:
                self.find_cells(y_coord + 1, x_coord) #find up adjacent cells

            if y_coord == self.grid_len_y-1:
                self.find_cells(y_coord - 1, x_coord)  #find down adjacent cells

            if 0 < y_coord < self.grid_len_y - 1:  # find up and down adjacent cells
                self.find_cells(y_coord + 1, x_coord)
                self.find_cells(y_coord - 1, x_coord)

            if 0 < x_coord < self.grid_len_x - 1:  # find left and right adjacent cells
                self.find_cells(y_coord, x_coord + 1)
                self.find_cells(y_coord, x_coord - 1)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    args = parser.parse_args()
    if args.input is None:
        print('Missing input filename')
    else:
        input = sys.argv[2]
        if os.path.exists(input):
            ad = adjacent_cells(input)
            ad.find_adjacent_cells()
        else:
            print('File does not exist!')
