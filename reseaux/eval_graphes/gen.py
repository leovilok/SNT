#!/usr/bin/env python

import networkx as nx
from networkx.algorithms.distance_measures import *
import matplotlib.pyplot as plt
from random import *

from sys import argv
from io import open

def random_simple_connected_graph(nodes, num_edges):
    g = nx.Graph()

    # random spanning tree
    for i in range(1,len(nodes)):
        g.add_edge(nodes[i], choice(nodes[:i]))

    # additionnal edges
    g.add_edges_from(choices(list(nx.non_edges(g)), k=num_edges-len(nodes)))

    return g

def draw_graph_file(id, g):
    plt.clf()

    pos = nx.nx_agraph.graphviz_layout(g, prog="neato")
    nx.draw(g, pos=pos, with_labels=True, font_size=36, node_size=2500, node_color="white", edge_color="black", width=2, linewidths=2)
    #nx.draw_kamada_kawai(g, with_labels=True, font_size=36, node_size=2500, node_color="white", edge_color="black", width=2, linewidths=2)

    ax = plt.gca()
    ax.collections[0].set_edgecolor("#000000")

    ax.margins(0.20)

    #plt.text(-0.5,-1,"Diamètre : __ Rayon : __ Centre(s) : __________", va="top", ha="left")
    #plt.show()
    #plt.axis("off")
    fname = ID+"g"+id+".png"
    plt.savefig(fname)
    return fname

def printboth(s, end='\n'):
    print(s, file=out, end=end)
    print(s, file=outcorr, end=end)

if len(argv)>1:
    ID = argv[1]
else:
    ID="0"

print(ID)

out = open(ID+".md", 'w')
outcorr = open(ID+"-corr.md", 'w')

printboth("""

# Évaluation sur les graphes

Nom :

Prénom :

Classe :
""")

printboth("*(version générée N°%s)*"%ID)

# Exercice 1

nodes = ['Alice', 'Bob', 'Céline', 'Damien', 'Élodie']

g = random_simple_connected_graph(nodes, 7)

printboth("""
**Exercice 1** : Dessinez le graphe correspondant aux relations sociales suivantes :
""")

for edge in g.edges():
    printboth("- **{}** est ami{} avec **{}**".format(edge[0], 'e' if edge[0][-1]=='e' else '', edge[1]))

print("""
\\

\\ 

\\ 

\\ 
""",file=out)

fname = draw_graph_file("ex1", g)

print("![](%s){ width=50%%}"%fname, file=outcorr)

# Exercice 2

printboth("""
**Exercice 2** : Dans le graphe ci-dessous :
""")

g = random_simple_connected_graph("DEFGH", 8)
g.add_edge("A", choice("DFG"))
g.add_edge("B", choice("EH"))
g.add_edge("C", choice("DEFGH"))

printboth("- Donnez un chemin entre **A** et **B** : ", end="")

print("_______________", file=out)
print(nx.shortest_path(g, 'A', 'B'), file=outcorr)

printboth("- Quelle est la distance entre **A** et **C** (en nombre d'arêtes) ? ", end="")
print("___", file=out)
print(nx.shortest_path_length(g, 'A', 'C'), file=outcorr)

printboth("- Quelle est la distance entre **B** et **C** (en nombre d'arêtes) ? ", end="")
print("___", file=out)
print(nx.shortest_path_length(g, 'B', 'C'), file=outcorr)

fname = draw_graph_file("ex2", g)

print("\n![](%s){ width=70%% }"%fname, file=out)

print("\n![](%s){ width=50%% }"%fname, file=outcorr)

# Exercice 3
printboth("""
**Exercice 3 (verso)** : Trouvez les diamètres, rayons, et centres des graphes suivants.
\pagebreak
""")

alpha = list("ABCDEFGHIJKLMNOP")

glist = []

nodes = alpha[:5]

shuffle(nodes)

glist.append(random_simple_connected_graph(nodes, 5))
glist.append(random_simple_connected_graph(nodes, 7))

nodes = alpha[:6]
shuffle(nodes)

glist.append(random_simple_connected_graph(nodes, 8))
glist.append(random_simple_connected_graph(nodes, 10))

nodes = alpha[:7]
shuffle(nodes)

glist.append(random_simple_connected_graph(nodes, 11))
glist.append(random_simple_connected_graph(nodes, 12))

fname=""

for i in range(6):
    oldfname = fname
    fname = draw_graph_file(str(i), glist[i])

    if i%2==1:
        printboth("| ![](%s) | ![](%s) |"%(oldfname, fname))
        printboth("|---|---|")
        print("| Diamètre : ___ \\ \\ \\ Rayon : ___ Centre(s) : _____________ ", file=out, end="")
        print("| Diamètre : ___ \\ \\ \\ Rayon : ___ Centre(s) : _____________ ", file=out, end="|\n")
        print("| Diamètre :", diameter(glist[i-1]),"Rayon :", radius(glist[i-1]), "Centres :", sorted(center(glist[i-1])), file=outcorr, end=" ")
        print("| Diamètre :", diameter(glist[i]),"Rayon :", radius(glist[i]), "Centres :", sorted(center(glist[i])), file=outcorr, end=" |\n")
        
#    end = "" if i%2==0 else "|\n"
#    printboth("| ![](%s)"%fname, end=end)
#    print("| Diamètre : ___ Rayon : ___ Centre(s) : __________ ", file=out, end=end)
#    print("| Diamètre : 1 Rayon : 1 Centre(s) : A,B,C ", file=outcorr, end=end)
        printboth("")

    
    

