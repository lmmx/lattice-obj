from hasse import hasse_coords
from sage.all import posets
from sage.all import sage as sg

def integer_composition_graph(n):
    p = posets.IntegerCompositions(n)
    DG = sg.graphs.digraph.DiGraph
    GG = sg.graphs.generic_graph.GenericGraph
    h = p.hasse_diagram()
    h_repositioned = DG(h, pos=hasse_coords(p))
    GG.show(h_repositioned, method="js", link_distance=200)
    return h_repositioned
