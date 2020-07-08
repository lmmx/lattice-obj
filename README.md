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

### Overview

- Generate integer composition posets in SAGE,
  - as JSON specification (via Sage: `posets.IntegerCompositions.hasse_diagram`)
  - as HTML (via Sage's integration with D3.js: `hasse_diagram.show(method="js")`)
  - as SVG (via D3.js, manually copying the HTML D3 generates into SVG files from the browser DOM
    with 'Inspect element')
- Generate SVG that matches the above Sage-generated SVG
  - Bypass manual copying-SVG-from-the-DOM, producing SVG from a Hasse diagram specification
- Generate an ODP slide drawing that matches the imported SVG
  - Bypass manual SVG import, allowing automated creation of ODP presentations which can be
    arranged freely to explore the integer compositions

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

- There is far too much whitespace around the margins of the diagram.
- There is an unnecessary `<rect fill="white">`
- The marker end has 'overlap' but this is invisible due to the circle at the end of the marker:
  - `<marker><path>` attribute `d` = `M0,-2L4,0L0,2`
    - The 2nd and 4th parts of the comma-separated value array are non-zero.
    - The 2nd and the 4th scale the anti-clockwise and the clockwise side of the marker respectively,
      and the 2nd also modifies the `L` value which is the 'end' (L = `lineto` i.e. end/destination,
      M = `moveto` i.e. start/origin which stays set to `0` i.e. the same as the `L` value of the
      path the marker is 'marking')
      - (i.e. the clockwise side is the west side if the marker is directed southward,
         or simply the right hand side with respect to the end direction)
      - See [W3schools](https://www.w3schools.com/graphics/svg_path.asp) and
        [Mozilla Tutorial](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths)
        for reference on the `path` element in SVG.
- The marker end `fill` colour is black by default, setting it to `fill="rgb(100,100,100)"` prevents
  it from matching the text, meaning the text labels become unreadable where they overlap the marker.

This gives a 'recipe' for editing the SVG output then: remove the `rect` tag and add a `fill` attribute
to the `marker`⇒`path` tag in the `defs` tag.

We can also generate an SVG from scratch using this template.

I removed parts of the partition diagram of the integer 4 (not a Young's lattice as I said, but I'm
abbreviating it y4 for brevity):

- `y4_min.html` has grey-coloured markers (arrows), 1 node (the supremum), and the 3 paths from it
  - The SVG element is the only child of the `html`⇒`body` tag, its source is `y4_min_pretty.svg`
- `y4_four_nodes.html` has grey-coloured markers (arrows), 4 nodes, and the 3 paths that link them
  - The SVG element is the only child of the `html`⇒`body` tag, its source is `y4_four_nodes_pretty.svg`

Similarly for compositions of the integer 5

![](y5.png)

Here I decided to change the size of the markers, as they were being shown as way too big when
rendered by Inkscape (but not by Firefox, but still I wanted to avoid it), and I also noticed that
when D3 renders them it gives them partial opacity, so I created a CSS style node underneath the
`<svg>` tag. The result looks much neater, and overlaps are subtly shown by the darker shading.

- The files involved here are `y5_small_markers.png` generated from `y5_small_markers.svg` and
  viewable as a webpage as `y5_small_markers.html`

![](y5_small_markers.png)

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

If we add the flag `--ids`, only the penultimate node (`marker`) has an id
(`#directed`), but if we use the flag `--props` we see various properties:

```STDOUT
svg | width=1334 height=735 pointer-events=all 
└─ g | 
   └─ g | transform=translate(47.8483... 
      ├─ rect | x=-10000 y=-10000 width=20000 height=20000 fill=white 
      ├─ path | class=link directed marker-end=url(#directed) style=stroke: rgb(170, ... d=M666.376991707682... 
      ├─ path | class=link directed marker-end=url(#directed) style=stroke: rgb(170, ... d=M666.376991707682... 
      ├─ path | class=link directed marker-end=url(#directed) style=stroke: rgb(170, ... d=M666.376991707682... 
      ├─ path | class=link directed marker-end=url(#directed) style=stroke: rgb(170, ... d=M810.389868041940... 
      ├─ path | class=link directed marker-end=url(#directed) style=stroke: rgb(170, ... d=M810.389868041940... 
      ├─ path | class=link directed marker-end=url(#directed) style=stroke: rgb(170, ... d=M520.898644950828... 
      ├─ path | class=link directed marker-end=url(#directed) style=stroke: rgb(170, ... d=M520.898644950828... 
      ├─ path | class=link directed marker-end=url(#directed) style=stroke: rgb(170, ... d=M664.892233574425... 
      ├─ path | class=link directed marker-end=url(#directed) style=stroke: rgb(170, ... d=M668.581599973266... 
      ├─ path | class=link directed marker-end=url(#directed) style=stroke: rgb(170, ... d=M668.581599973266... 
      ├─ path | class=link directed marker-end=url(#directed) style=stroke: rgb(170, ... d=M812.524124993109... 
      ├─ path | class=link directed marker-end=url(#directed) style=stroke: rgb(170, ... d=M523.077534533065... 
      ├─ circle | class=node r=7 style=fill: rgb(31, 119... cx=666.3769917076821 cy=134.73103756664625 
      │  └─ title | 
      ├─ circle | class=node r=7 style=fill: rgb(31, 119... cx=810.3898680419409 cy=269.7125742360677 
      │  └─ title | 
      ├─ circle | class=node r=7 style=fill: rgb(31, 119... cx=520.8986449508284 cy=268.1542229405705 
      │  └─ title | 
      ├─ circle | class=node r=7 style=fill: rgb(31, 119... cx=664.892233574425 cy=403.5621268126448 
      │  └─ title | 
      ├─ circle | class=node r=7 style=fill: rgb(31, 119... cx=668.5815999732662 cy=331.4188556805278 
      │  └─ title | 
      ├─ circle | class=node r=7 style=fill: rgb(31, 119... cx=812.5241249931095 cy=466.8549120446366 
      │  └─ title | 
      ├─ circle | class=node r=7 style=fill: rgb(31, 119... cx=523.0775345330653 cy=465.28423876421226 
      │  └─ title | 
      ├─ circle | class=node r=7 style=fill: rgb(31, 119... cx=667.0884150720784 cy=600.2903513213034 
      │  └─ title | 
      ├─ text | vertical-align=middle x=673.3769917076821 y=134.73103756664625 
      ├─ text | vertical-align=middle x=817.3898680419409 y=269.7125742360677 
      ├─ text | vertical-align=middle x=527.8986449508284 y=268.1542229405705 
      ├─ text | vertical-align=middle x=671.892233574425 y=403.5621268126448 
      ├─ text | vertical-align=middle x=675.5815999732662 y=331.4188556805278 
      ├─ text | vertical-align=middle x=819.5241249931095 y=466.8549120446366 
      ├─ text | vertical-align=middle x=530.0775345330653 y=465.28423876421226 
      ├─ text | vertical-align=middle x=674.0884150720784 y=600.2903513213034 
      └─ defs | 
         └─ marker | viewBox=0 -2 4 4 refX=6 refY=0 markerWidth=4 markerHeight=4 preserveAspectRatio=false orient=auto 
            └─ path | d=M0,-2L4,0L0,2
```

Essentially this is what we need: there are paths (the properties of which `svgi` has cropped, unhelpfully), so
we can use Python's `BeautifulSoup` (version 4 is `bs4`) to "prettify" it (pretty print) to file:

```sh
python -c "from bs4 import BeautifulSoup as bs; soup=bs(open('y4.svg')); h=soup.prettify(); print(h, file=open('y4_pretty.svg', 'w'))"
```

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

Pretty print the content XML for the edited ODP (as a new file, [`y4_manually-grouped-content.xml`](y4_manually-grouped-content.xml).

- This was the file where the SVG was imported and then its components were grouped hierarchically from the supremum downward,
  with the outbound arcs from a given node (i.e. from a given composition) 'grouped' with that node.
  - After all nodes have been grouped to their outbound arcs, the entire set of nodes and arcs is grouped
  - ...then the entire set of nodes/arcs is grouped with the labels (I think

```py
from xml.dom.minidom import parse
p = parse("y4_edited_odp_extracted/content.xml")
print(p.toprettyxml(), file=open("y4_manually-grouped_content.xml", "w"))
```

As a one liner that can be reused:

```sh
python -c "from xml.dom.minidom import parse; print(parse('y4_coloured_odp_extracted/content.xml').toprettyxml(), file=open('y4_manually-coloured_content.xml', 'w'))"
```

Examining this XML, it can be seen that:

- Everything except the `<office:body>` node is generic and can be ignored (as mere 'container')
  - Briefly, they are: document content specification; scripts (i.e. macros: none); font face declarations; text styles; list bullet styles
- The `<office:body>` has a single child node, which is `<office:presentation>` (as this is a presentation file).
- The `<office:presentation>` has 2 child nodes:
  - A `<draw:page>` node
  - A `<presentation:settings>` node
- Presumably there would be multiple `<draw:page>` nodes if there were multiple slides.
- The `<draw:page>` has 2 noteworthy attributes:
  - `draw:master-page-name="Default" meaning it uses the default 'master' template
  - `draw:name="page1"` meaning its title is "page1" (presumably this is parsed to become "Slide 1" but also to allow object-oriented constructions
    such as "Duplicate of Slide 1" when duplicated, etc.

### Editing the ODP file

We have viewed the ODP file archive's contents, and can edit the unzipped archive, but if we just zip it again it'll be considered corrupt and
will not be read by LibreOffice Impress unless we use particular flags (due to a
[change](https://ask.libreoffice.org/en/question/185777/libreoffice-60-unzip-zip-open-document-file/) in LibreOffice around 2019):

> When (re)zipping an ODF document you must ensure that the mimetype file is
> the very first file in the archive and not compressed, it must be plain text.
> If that is not the case (compressed file or different position in the zip
> directory) then it is not a valid ODF file.
>
> To achieve that, easiest is to freshen the existing zip with the modified
> file(s) instead of creating a new zip, i.e. use the `-f` option, for example
> `zip -f /path/to/filename.ods content.xml`
>
> When creating a new zip, add and store only the mimetype file first using the
> `-0` (numeric zero, not letter O) option. Then add other files using the `-u` option.

In other words, don't compress the mimetype as it needs to be readable as plain text,
but rather than supplying each file to compress with the `-f` flag after passing in
`-0 mimetype`, just 'freshen' the existing file you originally decompressed,
since it already contains a `content.xml` so you can just update that in the
compressed archive to be the modified version you just edited.

I tried this and it didn't work, then I went back and noticed this answer
had been corrected further down the discussion:

> The `zip -f ./decompresslib/X.odt ./decompresslib/content.xml` is wrong,
> content.xml must be without path, otherwise there's noting to refresh (and
> adding the file would be wrong). So either the zip command be invoked in its
> (`content.xml`) actual directory `decompresslib/` and omitting the directory, or
> the -j junk directory names option be used, so `zip -f -j ./decompresslib/X.odt ./decompresslib/content.xml`
> (be careful you don't use that with other files that actually need a correct directory prefix).

> The non-matching CRC does not harm, it will be corrected with freshening the zip.

In other words (ignore the name "decompresslib"), if you freshen a zip archive but are not
running the command from (i.e. the working directory) the directory of the extracted file,
then it won't freshen the file, but it also won't tell you it didn't. So instead, this
response suggests to use the `-j` ("junk") option to `zip`,

```
-j
--junk-paths
      Store just the name of a saved file (junk the path),  and  do  not  store
      directory  names.  By  default, zip will store the full path (relative to
      the current directory).
```

I think what this means is, if you try to freshen the file `content.xml` but do so
by calling it from the parent directory `my_cool_dir`, then you won't freshen the `.odp` zip
archive 'subfile' (think of the archive as like a little file system) at `myfile.odp/content.xml`
but at `myfile.odp/my_cool_dir/content.xml`, which didn't exist, so since `freshen` will not
add new files to an archive, it won't do anything, and this is why nothing changed when
`zip -f` was run without `-j`.

The second part of the response warns against using `-j` if the directory path is needed,
in other words if you're storing something in a subdirectory of the archive, but here
`content.xml` is in the 'top-level' of the archive so it doesn't matter, so we can use `-j`
and "junk the path".
