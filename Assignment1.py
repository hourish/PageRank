from Node import *
import csv
import math

nodes = {} # Map node's name to it's object

def load_graph(path):
    with open(path) as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            first_node = nodes.get(row[0])
            second_node = nodes.get(row[1])
            # Create new node if does not exist
            if first_node == None:
                first_node = Node(row[0])
                nodes[row[0]] = first_node
            else:
                first_node = nodes[row[0]]

            if second_node == None:
                second_node = Node(row[1])
                nodes[row[1]] = second_node
            else:
                second_node = nodes[row[1]]

            # Add one to the out degree of the first node
            first_node.increase_out_degree()

            # The first node point to the second node
            second_node.add_neighbor(first_node)


def calculate_page_rank():
    beta = 0.85
    delta = 0.001
    iterations_limit = 20
    last_iteration = 0

    # Initials values - 1/N
    for node in nodes.values():
        node.setPageRank(1 / nodes.__len__())

    for i in range(iterations_limit):
        # Set new page rank for all nodes
        for node in nodes.values():
            new_pageRank = 0
            for neighbor in node.neighbors_in:
                new_pageRank += beta * (neighbor.pageRank / neighbor.out_degree)
                new_pageRank += (1 - beta) / nodes.__len__()
                last_iteration += math.fabs(new_pageRank - node.pageRank)
            node.setPageRank(new_pageRank)

        # TODO only for check!
        suppose_to_be_1 = 0
        for node in nodes.values():
            suppose_to_be_1 += node.pageRank
        print('suppose to be 1... ' + str(suppose_to_be_1))

        # Check stop conditions
        if last_iteration <= delta:
            break

if __name__== "__main__":
  load_graph('Wikipedia_votes.csv')
  calculate_page_rank()
