from Node import *
import csv
import math

nodes = {} # Map node's name to it's object

def load_graph(path):
    '''Read csv file from the given path and update the data structures'''
    with open(path, encoding='utf-8-sig') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows: # Each row is a list of source and destination nodes
            # Create new nodes if do not exist
            first_node = create_node(row[0]) if nodes.get(row[0]) == None else nodes[row[0]]
            second_node = create_node(row[1]) if nodes.get(row[1]) == None else nodes[row[1]]

            # Add one to the out degree of the first node
            first_node.increase_out_degree()

            # The first node point to the second node
            second_node.add_neighbor(first_node)


def create_node(name):
    ''' Create new node from the given name, add to 'nodes' and return it'''
    node = Node(name)
    nodes[name] = node
    return node


def calculate_page_rank(beta = 0.85, delta = 0.001):
    '''Calculate the page rank values for all the nodes given the parameters: beta, delta'''
    iterations_limit = 20

    # Initials values - 1/N
    for node in nodes.values():
        node.setPageRank(1 / nodes.__len__())

    # Update until reach iterations_limit or last_iteration <= delta
    for i in range(iterations_limit):
        last_iteration = 0
        new_pageRanks = []
        s = 0
        # Set new page rank for all nodes
        for node in nodes.values():
            r_prime = 0
            for neighbor in node.neighbors_in:
                r_prime += beta * (neighbor.pageRank / neighbor.out_degree)
            s += r_prime
            new_pageRanks.append(r_prime) # only r_prime without (1-s)/n

        # After the calculation of s, add to the page rank values (1-s)/n
        for new, old in zip(new_pageRanks, nodes.values()):
            new_pageRank = new + ((1 - s) / nodes.__len__())
            old.setPageRank(new_pageRank)
            last_iteration += math.fabs(new_pageRank - old.pageRank)

        # Check stop conditions
        if last_iteration <= delta:
            break

def get_PageRank(node_name):
    '''Return the page rank value of the given node_name'''
    if nodes[node_name] == None:
        return '-1'
    return nodes[node_name].pageRank


def Get_top_nodes(n):
    '''Return a list of tuples of n nodes with the highest page rank value'''
    sortedLst = sorted(nodes.items(), key = lambda item : item[1].pageRank,reverse= True)
    result = [] # Map node_name to its page rank value
    for element in sortedLst[:n]:
        result.append(tuple((element[0], element[1].pageRank)))
    return result

def get_all_PageRank():
    '''Return a list of tuples of the nodes sorted by their page rank value of high to low'''
    sortedLst = sorted(nodes.items(), key = lambda item : item[1].pageRank,reverse= True)
    result = []
    for element in sortedLst:
        result.append(tuple((element[0], element[1].pageRank)))
    return result
