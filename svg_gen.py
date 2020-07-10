from demo_json import example_json, example_json_nonsquare
from bs4 import BeautifulSoup as BS
import numpy as np
from scipy.sparse import coo_matrix as coo
from math import ceil, sqrt
import sys

def svg_from_json_demo(json=example_json_nonsquare, pprint=True, printer=sys.stdout):
    """
    Demo of the SVG generation with pre-obtained JSON, imported
    from `demo_json.py` module and generated by IntegerCompositions
    with `n=6` (`example_json_nonsquare`) and `n=4` (`example_json`).
    """
    return svg_from_json(json=json, pprint=pprint, printer=printer)

def svg_from_json(json, scale=800, pprint=False, printer=sys.stdout):
    """
    Process `pos`, `nodes`, and `links` entries in JSON from
    `sage.graphs.graph_plot_js.gen_html_code` into an SVG.

    Print the result to STDOUT if `pprint` is True, or to any
    other output give as `printer` (e.g. `sys.stderr` or a file).
    """
    svg = BS("", "html.parser")
    scale = scale
    pos = np.array(json.get("pos"))
    span = pos.max(axis=0) - pos.min(axis=0)
    aspect_ratio = np.divide(*span) # wide if AR > 1, narrow if AR < 1
    h, w = 2 * scale / span
    shift = (np.array([w, h]) - scale * span) / 2
    shift_downscale = (2.5, 1) # Reduce the x (left) shift to account for RHS label
    shift_loss = shift - (shift / shift_downscale)
    shift /= shift_downscale
    # Account for the trimmed left shift (avoid "spare width" on RHS)
    w, h = (w, h) - shift_loss
    circ_radius = 7
    svg_tag = svg.new_tag("svg", attrs={
        "width": w,
        "height": h,
        "pointer-events": "all"
    })
    svg.append(svg_tag)
    g1 = svg.new_tag("g") # One 'top-level' group
    svg.svg.insert(0, g1)
    bg = svg.new_tag("rect", attrs={
        "opacity": 0,
        "x": 0,
        "y": 0,
        "width": w,
        "height": h
    })
    g1.append(bg)

    node_names = [v.get("name") for v in json.get("nodes")]
    sources = [e.get("source") for e in json.get("links")]
    targets = [e.get("target") for e in json.get("links")]
    arcs = np.array([sources, targets]).T
    scaled_positions = scale * (pos - pos.min(axis=0)) + shift
    scaled_arc_positions = scale * (pos - pos.min(axis=0))[arcs] + shift
    arc_style = "stroke: rgb(170, 170, 170); stroke-width: 4px;"
    arc_style += " stroke-opacity: .6; opacity: .6;"
    for ((src_x, src_y), (to_x, to_y)) in scaled_arc_positions:
        arc_path = svg.new_tag("path", attrs={
            "class": "link directed",
            "marker-end": "url(#directed)",
            "style": arc_style,
            "d": f"M{src_x},{src_y}L{to_x},{to_y}"
        })
        g1.append(arc_path)
    node_style = "fill: rgb(31, 119, 180); stroke: #fff; stroke-width: 1.5px;"
    node_labels = BS("", "html.parser")
    for vi, (cx, cy) in enumerate(scaled_positions):
        circ = svg.new_tag("circle", attrs={
            "class": "node",
            "r": circ_radius,
            "style": node_style,
            "cx": cx,
            "cy": cy
        })
        node_title = svg.new_tag("title")
        node_name = node_names[vi]
        node_title.append(node_name) # set node name as title tag text (shown on hover)
        circ.append(node_title)
        g1.append(circ)
        # Accumulate an array of text tags (the labels) to add after the circles
        node_label = node_labels.new_tag("text", attrs={
            "vertical-align": "middle",
            "x": cx + circ_radius,
            "y": cy
        })
        node_label.append(node_name)
        node_labels.append(node_label)
    g1.append(node_labels) # Add all label text tags at once after the circles
    defs = svg.new_tag("defs")
    vb_bl_x, vb_bl_y = (0, -2) # viewBox bottom-left corner relative (x,y) coordinates
    vb_width = vb_height = 4
    marker_tag = svg.new_tag("marker", attrs={
        "id": "directed",
        "viewBox": f"{vb_bl_x} {vb_bl_y} {vb_width} {vb_height}",
        "refX": ceil(2*sqrt(circ_radius)), # Math.ceil(2*Math.sqrt(graph.vertex_size))
        "refY": 0,
        "markerWidth": vb_width,
        "markerHeight": vb_height,
        "preserveAspectRatio": "none",
        "orient": "auto",
        "style": "fill: #bbb;"
    })
    tri_pts = [(0, -2), (4, 0), (0, 2)] # 3 endpoints of a triangle ==> "M0,-2L4,0L0,2"
    d_str = "".join([s + ','.join(map(repr, tri_pts[i])) for i, s in enumerate("MLL")])
    marker_path = svg.new_tag("path", attrs={"d": d_str})
    marker_tag.append(marker_path)
    defs.append(marker_tag)
    g1.append(defs)
    if pprint:
        print(svg.prettify(), file=printer)
    return svg
