from json import loads

example_json_nonsquare = loads("""{
    "nodes": [
        {"name": "[6]", "group": "0"},
        {"name": "[5, 1]", "group": "0"},
        {"name": "[4, 2]", "group": "0"},
        {"name": "[4, 1, 1]", "group": "0"},
        {"name": "[3, 3]", "group": "0"},
        {"name": "[3, 2, 1]", "group": "0"},
        {"name": "[3, 1, 2]", "group": "0"},
        {"name": "[3, 1, 1, 1]", "group": "0"},
        {"name": "[2, 4]", "group": "0"},
        {"name": "[2, 3, 1]", "group": "0"},
        {"name": "[2, 2, 2]", "group": "0"},
        {"name": "[2, 2, 1, 1]", "group": "0"},
        {"name": "[2, 1, 3]", "group": "0"},
        {"name": "[2, 1, 2, 1]", "group": "0"},
        {"name": "[2, 1, 1, 2]", "group": "0"},
        {"name": "[2, 1, 1, 1, 1]", "group": "0"},
        {"name": "[1, 5]", "group": "0"},
        {"name": "[1, 4, 1]", "group": "0"},
        {"name": "[1, 3, 2]", "group": "0"},
        {"name": "[1, 3, 1, 1]", "group": "0"},
        {"name": "[1, 2, 3]", "group": "0"},
        {"name": "[1, 2, 2, 1]", "group": "0"},
        {"name": "[1, 2, 1, 2]", "group": "0"},
        {"name": "[1, 2, 1, 1, 1]", "group": "0"},
        {"name": "[1, 1, 4]", "group": "0"},
        {"name": "[1, 1, 3, 1]", "group": "0"},
        {"name": "[1, 1, 2, 2]", "group": "0"},
        {"name": "[1, 1, 2, 1, 1]", "group": "0"},
        {"name": "[1, 1, 1, 3]", "group": "0"},
        {"name": "[1, 1, 1, 2, 1]", "group": "0"},
        {"name": "[1, 1, 1, 1, 2]", "group": "0"},
        {"name": "[1, 1, 1, 1, 1, 1]", "group": "0"}
    ],
    "links": [
        {"source": 0, "target": 16, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 0, "target": 1, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 0, "target": 2, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 0, "target": 4, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 0, "target": 8, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 1, "target": 17, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 1, "target": 3, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 1, "target": 5, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 1, "target": 9, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 2, "target": 18, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 2, "target": 3, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 2, "target": 6, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 2, "target": 10, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 3, "target": 19, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 3, "target": 7, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 3, "target": 11, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 4, "target": 20, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 4, "target": 5, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 4, "target": 6, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 4, "target": 12, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 5, "target": 21, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 5, "target": 7, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 5, "target": 13, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 6, "target": 22, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 6, "target": 7, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 6, "target": 14, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 7, "target": 23, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 7, "target": 15, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 8, "target": 24, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 8, "target": 9, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 8, "target": 10, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 8, "target": 12, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 9, "target": 25, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 9, "target": 11, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 9, "target": 13, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 10, "target": 26, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 10, "target": 11, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 10, "target": 14, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 11, "target": 27, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 11, "target": 15, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 12, "target": 28, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 12, "target": 13, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 12, "target": 14, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 13, "target": 29, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 13, "target": 15, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 14, "target": 30, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 14, "target": 15, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 15, "target": 31, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 16, "target": 17, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 16, "target": 18, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 16, "target": 20, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 16, "target": 24, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 17, "target": 19, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 17, "target": 21, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 17, "target": 25, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 18, "target": 19, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 18, "target": 22, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 18, "target": 26, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 19, "target": 23, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 19, "target": 27, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 20, "target": 21, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 20, "target": 22, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 20, "target": 28, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 21, "target": 23, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 21, "target": 29, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 22, "target": 23, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 22, "target": 30, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 23, "target": 31, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 24, "target": 25, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 24, "target": 26, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 24, "target": 28, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 25, "target": 27, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 25, "target": 29, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 26, "target": 27, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 26, "target": 30, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 27, "target": 31, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 28, "target": 29, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 28, "target": 30, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 29, "target": 31, "strength": 0, "color": "#aaa", "curve": 0, "name": ""},
        {"source": 30, "target": 31, "strength": 0, "color": "#aaa", "curve": 0, "name": ""}
    ],
    "loops": [],
    "pos": [
        [0.833, -1.0], [1.204, -0.8], [1.019, -0.8], [1.667, -0.6], [0.833, -0.8],
        [1.481, -0.6], [1.296, -0.6], [1.667, -0.4], [0.648, -0.8], [1.111, -0.6],
        [0.926, -0.6], [1.481, -0.4], [0.741, -0.6], [1.296, -0.4], [1.111, -0.4],
        [1.204, -0.2], [0.463, -0.8], [0.556, -0.6], [0.37, -0.6], [0.926, -0.4],
        [0.185, -0.6], [0.741, -0.4], [0.556, -0.4], [1.019, -0.2], [0.0, -0.6],
        [0.37, -0.4], [0.185, -0.4], [0.833, -0.2], [0.0, -0.4], [0.648, -0.2],
        [0.463, -0.2], [0.833, -0.0]
    ],
    "directed": true,
    "charge": 0,
    "link_distance": 200,
    "link_strength": 0,
    "gravity": 0.0,
    "vertex_labels": true,
    "edge_labels": false,
    "vertex_size": 7,
    "edge_thickness": 4
}
""")

example_json = loads("""{
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
  "pos": [
    [0.5, -1.0], [1.0, -0.667], [0.5, -0.667], [1.0, -0.333],
    [0.0, -0.667], [0.5, -0.333], [0.0, -0.333], [0.5, -0.0]
  ],
  "directed": true,
  "charge": -120,
  "link_distance": 200,
  "link_strength": 2,
  "gravity": 0.04,
  "vertex_labels": true,
  "edge_labels": false,
  "vertex_size": 7,
  "edge_thickness": 4
}""")
