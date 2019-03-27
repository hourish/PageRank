class Node:

    def __init__(self, name):
        self.id = int(name)
        self.neighbors_in = []
        self.out_degree = 0

    def setPageRank(self, pageRank):
        self.pageRank = pageRank

    def add_neighbor(self, neighbor):
        self.neighbors_in.append(neighbor)

    def increase_out_degree(self):
        self.out_degree += 1