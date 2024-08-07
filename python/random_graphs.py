# This python script will produce random mentis graphs for given n and m

import random

FILE_PATH = "../data/metis_graphs/auto_generated_graphs/"


def random_graph(n, m):
    text = (
        "% Random generated graph with "
        + str(n)
        + " vertices and "
        + str(m)
        + " edges. \n"
    )
    text += str(n) + " " + str(m)

    adjacency_matrix = [[0 for x in range(n)] for y in range(n)]

    for _ in range(m):
        set = False
        while not set:
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)

            if adjacency_matrix[u][v] == 0:
                # we assume undirected graphs with self loops
                adjacency_matrix[u][v] = 1
                adjacency_matrix[v][u] = 1
                set = True

    for i in range(n):
        text += "\n"
        first = True
        for j in range(n):
            if adjacency_matrix[i][j] == 1:
                if first:
                    text += str(j + 1)
                    first = False
                else:
                    text += " " + str(j)

    return text


# a function that exports the generated graphs into files
def text_to_file(text, file_name):
    with open(file_name, "w") as f:
        f.write(text)


# A function generating a random graph for fixed n and m
def generate_graph_for_fixed_n_and_m(n, m):
    text = random_graph(n, m)
    filename = "randgraph_" + str(n) + "_" + str(m) + ".graph"
    text_to_file(text, FILE_PATH + filename)


# A function calculating all graphs
def generate_graphs():
    max_exponent = 14

    for i in range(2, max_exponent + 1):
        print("generating graph with " + str(2**i) + " vertices")
        # graph with 2^i vertices and random number of edges between 2^i and 2^(2i)

        generate_graph_for_fixed_n_and_m(
            2**i, random.randint(2**i, (2**i) * (2**i - 1) * (1 / 2))
        )


if __name__ == "__main__":
    generate_graphs()
