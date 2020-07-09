import numpy as np
import itertools

def ranks_dict(poset):
    """
    Return a dictionary `r_dict` with rank keys (in descending order, from supremum,
    i.e. `h.vertices()[0]`, to infimum, `h.vertices()[-1]`) and lists of indices of
    the vertices at that level, to be displayed from left to right, suitable to be
    passed as the `heights` argument to `poset.plot`.
    """
    h = poset.hasse_diagram()
    ranks = [poset.rank_function()(z) for z in h.vertices()]
    rank_set = set(ranks) # Note that this sorts the ranks ascending (reversed later)
    r_indices = [[i for i, r in enumerate(ranks) if r == s] for s in rank_set]
    r_dict = dict(reversed(list(zip(rank_set, r_indices))))
    return r_dict

def poset_rel_coords(level_sizes, w_scale):
    max_len = np.max(level_sizes)
    unit_w = (1.0 * w_scale) / (max_len - 1)
    max_x = np.multiply(unit_w, np.subtract(level_sizes, 1))
    x_start = (w_scale - max_x)/2
    max_x += x_start
    # Round these as linspace gives weird floating point errors
    xx = [np.round(np.linspace(f, m, s), 3).tolist() for f,m,s in zip(x_start, max_x, level_sizes)]
    yy = np.round(np.linspace(0, 1, len(level_sizes)), 3).tolist()
    yy = list(map(lambda y: [y], yy))
    coords = [list(map(list, itertools.product(*v))) for v in zip(xx, yy)]
    return coords

def hasse_coords(poset, return_dict=True, key_by_vertex_index=False, scale_w=True):
    """
    poset should be a poset class such as `posets.IntegerPartitions(n)` for some `n`

    If `return_dict` is False:
    Returns a list of level lists. Each level list is a list of node tuples
    (the first/last are the singleton lists of the supremum/infimum).
    Each node tuple is a 2-tuple of the vertex index and a coordinate tuple.
    Each coordinate tuple is a 2-tuple of `(x,y)` coordinates.

    If `return_dict` is True and `key_by_vertex_index` is True:
    Returns a dictionary whose keys are integers in `range(len(h.vertices()))`,
    the values at each key are the `(x,y)` tuple, by default scaled from `[0.0, 1.0]`.

    If `return_dict` is True and `key_by_vertex_index` is False:
    Returns a dictionary whose keys are `h.vertices()` (to match `DiGraph.layout()`),
    the values at each key are the `(x,y)` tuple, by default scaled from `[0.0, 1.0]`.

    If `scale_w` is True, the (w:h) aspect ratio will be scaled to the poset's ratio
    of width:height i.e. the length ratio of the maximum antichain to maximum chain.
    """
    h = poset.hasse_diagram()
    r_dict = ranks_dict(poset)
    level_sizes = list(map(len, r_dict.values()))
    wh_aspect_ratio = 1 # 1:1 width:height aspect ratio
    if scale_w:
        # Do not check chain and antichain max. lengths, fails above n=7 or so
        ph = len(level_sizes)
        pw = max(level_sizes)
        wh_aspect_ratio = pw / ph
    poset_coords = poset_rel_coords(level_sizes, wh_aspect_ratio)
    vi_coords = list(map(lambda z: list(zip(*z)), list(zip(r_dict.values(), poset_coords))))
    node_coords = [[(h.vertices()[c[0]], c[1]) for c in l] for l in vi_coords]
    if not return_dict:
        return vi_coords
    if key_by_vertex_index:
        # return a dict whose keys are the index of the vertex in `h.vertices()`
        return dict(list(itertools.chain.from_iterable(vi_coords)))
    else:
        # return a dict whose keys are the vertex tuples themselves
        return dict(list(itertools.chain.from_iterable(node_coords)))

# Deprecated: Sage posets implement a method `rank_function`, use `rank_dicts` instead
def partition_len_level_dicts(vertices):
    """
    Return a dictionary `v_dict` with length keys and lists of indices of the
    vertices at that level, to be displayed from left to right,
    suitable to be passed as the `heights` argument to `poset.plot`.
    """
    v_dict = {}
    for vi, v in enumerate(vertices):
        v_len = len(v)
        v_dict.setdefault(v_len, [])
        v_dict.get(v_len).append(vi)
    return v_dict
