import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
    ('AB', 'DB'),
    ('AB', 'EB'),
    ('AC', 'DB'),
    ('AC', 'DC'),
    ('AC', 'EB'),
    ('AC', 'EC'),
    ('AE', 'CE'),
    ('AE', 'DE'),
    ('AE', 'EB'),
    ('AE', 'EC'),
    ('CE', 'DB'),
    ('CE', 'DC'),
    ('CE', 'DE'),
    ('DB', 'EB'),
    ('DB', 'EC'),
    ('DC', 'EC'),
]
G.add_edges_from(edges)

plt.figure()
nx.draw(G, with_labels=True, font_color='white')
plt.title('Graph showing incompatible turns')
plt.show()
plt.savefig("graph1.png")

color_map = nx.coloring.greedy_color(G)
colors = [color_map[node] for node in G.nodes()]

plt.figure()
nx.draw(G, with_labels=True, node_color=colors, font_color='white')
plt.title('Colored graph')
plt.show()
plt.savefig("colored_graph.png")