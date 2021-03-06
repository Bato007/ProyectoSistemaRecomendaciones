# Autores:
# Martin Amado 19020
# Andrea Amaya 19357
# Brandon Hernández 19376
# 
# Fecha: 6-05-2020
# Nombre: GrafoInicial.py

import networkx as nx

#Param: nombre_artista a recomendar
def generar_grafo(nombre_artista):
    G = nx.DiGraph()

    # agegar nodos (26)
    G.add_node("Ava Max")
    G.add_node("Dua Lipa")
    G.add_node("Melanie Martinez")
    G.add_node("Little Mix")
    G.add_node("Lady Gaga")
    G.add_node("Bebe Rexha")
    G.add_node("Camila Cabello")
    G.add_node("Anne Marie")
    G.add_node("Ariana Grande")
    G.add_node("Halsey")
    G.add_node("Zara Larsson")
    G.add_node("Sabrina Carpenter")
    G.add_node("Demi Lovato")
    G.add_node("Bea Miller")
    G.add_node("Hailee Steinfeld")
    G.add_node("Meghan Trainor")
    G.add_node("Clean Bandit")
    G.add_node("5SOS")
    G.add_node("MGK")
    G.add_node("Jonas Brothers")
    G.add_node("Sam Smith")
    G.add_node("Sia")
    G.add_node("Diplo")
    G.add_node("Zedd")
    G.add_node("Charlotte Lawrence")
    G.add_node("Doja Cat")

    #print ("Nodos: ", G.nodes())

    #Agregar aristas
    G.add_edge("Camila Cabello","5SOS")
    G.add_edge("Camila Cabello","Clean Bandit")
    G.add_edge("Dua Lipa","Anne Marie")
    G.add_edge("Dua Lipa","Camila Cabello")
    G.add_edge("5SOS","Diplo")
    G.add_edge("Halsey","Lady Gaga")
    G.add_edge("Halsey","Dua Lipa")
    G.add_edge("Halsey","Ava Max")
    G.add_edge("Halsey","Sia")
    G.add_edge("Sia","MGK")
    G.add_edge("Sia","Melanie Martinez")
    G.add_edge("Diplo","Halsey")
    G.add_edge("Diplo","Doja Cat")
    G.add_edge("Melanie Martinez","Halsey")
    G.add_edge("Melanie Martinez","Ariana Grande")
    G.add_edge("Demi Lovato","Melanie Martinez")
    G.add_edge("Demi Lovato","Sam Smith")
    G.add_edge("Lady Gaga","Demi Lovato")
    G.add_edge("Lady Gaga","Bea Miller")
    G.add_edge("Lady Gaga","MGK")
    G.add_edge("Lady Gaga","Zedd")
    G.add_edge("Lady Gaga","Anne Marie")
    G.add_edge("Bea Miller","Meghan Trainor")
    G.add_edge("Bea Miller","Little Mix")
    G.add_edge("Ava Max","Bebe Rexha")
    G.add_edge("Zara Larsson","Zedd")
    G.add_edge("Zedd", "Sia")
    G.add_edge("Clean Bandit", "Doja Cat")
    G.add_edge("Clean Bandit", "Ava Max")
    G.add_edge("Little Mix", "Zara Larsson")
    G.add_edge("Little Mix", "Meghan Trainor")
    G.add_edge("Little Mix", "Sabrina Carpenter")
    G.add_edge("Meghan Trainor", "Dua Lipa")
    G.add_edge("Sabrina Carpenter", "Doja Cat")
    G.add_edge("Sabrina Carpenter", "Charlotte Lawrence")
    G.add_edge("Hailee Steinfeld", "Little Mix")
    G.add_edge("Doja Cat", "Lady Gaga")
    G.add_edge("Charlotte Lawrence", "Zara Larsson")
    G.add_edge("Ariana Grande", "Sam Smith")
    G.add_edge("Sam Smith", "Charlotte Lawrence")
    G.add_edge("Bebe Rexha", "Hailee Steinfeld")
    G.add_edge("Bebe Rexha", "Meghan Trainor")
    G.add_edge("Bebe Rexha", "Ariana Grande")
    G.add_edge("Jonas Brothers", "5SOS")
    G.add_edge("Anne Marie", "Jonas Brothers")
    G.add_edge("MGK", "Anne Marie")
    G.add_edge("MGK", "Jonas Brothers")
    G.add_edge("MGK", "5SOS")
    

    #Orden DFS del grafo
    return (list(nx.dfs_preorder_nodes(G,nombre_artista)))

    