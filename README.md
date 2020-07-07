# lattice-obj

Generating ODP presentations (PowerPoint PPT equivalent for Linux) to show a lattice of
integer compositions created by Sage.

“Young's lattice of integer compositions” is a bit of a misnomer, it's actually an
analogue of Young's lattice, Richard Stanley wrote about it [here](http://www-math.mit.edu/~rstan/papers/composet.pdf)
and calls it the "composition poset" (or 'composet')

**However** the poset output by Sage for the integer compositions is _not_ this poset.

In the poset output by Sage's `posets.IntegerCompositions` there are only links between
sets with equal sum (though not necessarily), while in Stanley's "composition poset"
there are no links between sets of equal sum (e.g. 4 and 31)

## Analysis code

### Generate poset JSON in Sage

Generate a D3.js HTML file with the Young's lattice of partitions of the integer 4

```py
x = posets.IntegerCompositions(4)
h = x.hasse_diagram()
h.show(method="js",link_distance=200)
```

I then manually copied the HTML node `<svg>` and put it in the file `y4.svg`,
since it turns out the output of the Python method involved here is just

- Specifically:
  [`sage/graphs/graph_plot_js.py`](https://github.com/sagemath/sage/blob/master/src/sage/graphs/graph_plot_js.py)
  has a function which replaces a comment line in a HTML file
  - `~/miniconda/envs/sage/share/sage/ext/graphs/graph_plot_js.html` is where the HTML file is for me
- It replaces this comment with a JSON encoded dictionary

```py
string = JSONEncoder().encode({"nodes": nodes,
			   "links": edges,
			   "loops": loops,
			   "pos": pos,
			   "directed": G.is_directed(),
			   "charge": int(charge),
			   "link_distance": int(link_distance),
			   "link_strength": int(link_strength),
			   "gravity": float(gravity),
			   "vertex_labels": bool(vertex_labels),
			   "edge_labels": bool(edge_labels),
			   "vertex_size": int(vertex_size),
			   "edge_thickness": int(edge_thickness)})
```

which looks like this:

```json
{"nodes": [{"name": "[4]", "group": "0"}, {"name": "[3, 1]", "group": "0"}, {"name": "[2, 2]", "group": "0"}, {"name": "[2, 1, 1]", "group": "0"}, {"name": "[1, 3]", "group": "0"}, {"name": "[1, 2, 1]", "group": "0"}, {"name": "[1, 1, 2]", "group": "0"}, {"name": "[1, 1, 1, 1]", "group": "0"}], "links": [{"source": 0, "target": 1, "strength": 0, "color": "#aaa", "curve": 0, "name": ""}, {"source": 0, "target": 2, "strength": 0, "color": "#aaa", "curve": 0, "name": ""}, {"source": 0, "target": 4, "strength": 0, "color": "#aaa", "curve": 0, "name": ""}, {"source": 1, "target": 3, "strength": 0, "color": "#aaa", "curve": 0, "name": ""}, {"source": 1, "target": 5, "strength": 0, "color": "#aaa", "curve": 0, "name": ""}, {"source": 2, "target": 3, "strength": 0, "color": "#aaa", "curve": 0, "name": ""}, {"source": 2, "target": 6, "strength": 0, "color": "#aaa", "curve": 0, "name": ""}, {"source": 3, "target": 7, "strength": 0, "color": "#aaa", "curve": 0, "name": ""}, {"source": 4, "target": 5, "strength": 0, "color": "#aaa", "curve": 0, "name": ""}, {"source": 4, "target": 6, "strength": 0, "color": "#aaa", "curve": 0, "name": ""}, {"source": 5, "target": 7, "strength": 0, "color": "#aaa", "curve": 0, "name": ""}, {"source": 6, "target": 7, "strength": 0, "color": "#aaa", "curve": 0, "name": ""}], "loops": [], "pos": [], "directed": true, "charge": -120, "link_distance": 200, "link_strength": 2, "gravity": 0.04, "vertex_labels": true, "edge_labels": false, "vertex_size": 7, "edge_thickness": 4}
```

...which `jq` formats as:

```json
{
  "nodes": [
    {
      "name": "[4]",
      "group": "0"
    },
    {
      "name": "[3, 1]",
      "group": "0"
    },
    {
      "name": "[2, 2]",
      "group": "0"
    },
    {
      "name": "[2, 1, 1]",
      "group": "0"
    },
    {
      "name": "[1, 3]",
      "group": "0"
    },
    {
      "name": "[1, 2, 1]",
      "group": "0"
    },
    {
      "name": "[1, 1, 2]",
      "group": "0"
    },
    {
      "name": "[1, 1, 1, 1]",
      "group": "0"
    }
  ],
  "links": [
    {
      "source": 0,
      "target": 1,
      "strength": 0,
      "color": "#aaa",
      "curve": 0,
      "name": ""
    },
    {
      "source": 0,
      "target": 2,
      "strength": 0,
      "color": "#aaa",
      "curve": 0,
      "name": ""
    },
    {
      "source": 0,
      "target": 4,
      "strength": 0,
      "color": "#aaa",
      "curve": 0,
      "name": ""
    },
    {
      "source": 1,
      "target": 3,
      "strength": 0,
      "color": "#aaa",
      "curve": 0,
      "name": ""
    },
    {
      "source": 1,
      "target": 5,
      "strength": 0,
      "color": "#aaa",
      "curve": 0,
      "name": ""
    },
    {
      "source": 2,
      "target": 3,
      "strength": 0,
      "color": "#aaa",
      "curve": 0,
      "name": ""
    },
    {
      "source": 2,
      "target": 6,
      "strength": 0,
      "color": "#aaa",
      "curve": 0,
      "name": ""
    },
    {
      "source": 3,
      "target": 7,
      "strength": 0,
      "color": "#aaa",
      "curve": 0,
      "name": ""
    },
    {
      "source": 4,
      "target": 5,
      "strength": 0,
      "color": "#aaa",
      "curve": 0,
      "name": ""
    },
    {
      "source": 4,
      "target": 6,
      "strength": 0,
      "color": "#aaa",
      "curve": 0,
      "name": ""
    },
    {
      "source": 5,
      "target": 7,
      "strength": 0,
      "color": "#aaa",
      "curve": 0,
      "name": ""
    },
    {
      "source": 6,
      "target": 7,
      "strength": 0,
      "color": "#aaa",
      "curve": 0,
      "name": ""
    }
  ],
  "loops": [],
  "pos": [],
  "directed": true,
  "charge": -120,
  "link_distance": 200,
  "link_strength": 2,
  "gravity": 0.04,
  "vertex_labels": true,
  "edge_labels": false,
  "vertex_size": 7,
  "edge_thickness": 4
}
```

...the keys of which `jq -r keys[]` gives as:

```STDOUT
charge
directed
edge_labels
edge_thickness
gravity
link_distance
link_strength
links
loops
nodes
pos
vertex_labels
vertex_size
```

The SVG this was turned into by D3.js is [here](y4.svg) (GitHub says it's invalid and won't display
it but Firefox displays it and Inkscape parses it), and can be converted to a PNG for embedding
below by the command `inkscape -z -w 1024 y4.svg -e y4.png`

![](y4.png)

The first thing to notice is that the dimensions should be optimised: there is far too much
whitespace around the margins of the diagram.

### View SVG tree with svgi

The `npm`-packaged `nodejs` tool `svgi` will similarly print the tree of the SVG file generated from
this JSON specification by the D3.js script, by running `svgi -t y4.svg`:

```STDOUT
svg
└─ g
   └─ g
      ├─ rect
      ├─ path
      ├─ path
      ├─ path
      ├─ path
      ├─ path
      ├─ path
      ├─ path
      ├─ path
      ├─ path
      ├─ path
      ├─ path
      ├─ path
      ├─ circle
      │  └─ title
      ├─ circle
      │  └─ title
      ├─ circle
      │  └─ title
      ├─ circle
      │  └─ title
      ├─ circle
      │  └─ title
      ├─ circle
      │  └─ title
      ├─ circle
      │  └─ title
      ├─ circle
      │  └─ title
      ├─ text
      ├─ text
      ├─ text
      ├─ text
      ├─ text
      ├─ text
      ├─ text
      ├─ text
      └─ defs
         └─ marker
            └─ path
```

The challenge now is to figure out how the JSON determines the SVG...

### Viewing the ODP file

Unzip the ODP file into a [newly created] directory `y4_odp_extracted`:

```sh
unzip y4_lattice_sage-d3-generated.odp -d y4_odp_extracted/
```

Inspect the drawing groups:

```sh
cd y4_odp_extracted/
cat content.xml  | xq '. [] . "office:body"[] . "draw:page" .  "draw:g" . "draw:g"[] . "draw:g"[]'
```
