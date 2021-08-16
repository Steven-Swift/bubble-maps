{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-latest.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import plotly.express as px\n",
    "import plotly as py\n",
    "import plotly.graph_objs as go\n",
    "import pandas as pd\n",
    "import math\n",
    "import plotly.offline as offline\n",
    "\n",
    "offline.init_notebook_mode(connected=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "starting with plotting a bubble on the newyork city and 0,0 lonititude latitude to understand how scatter geo works\n",
    "\n",
    "\n",
    "with default land color"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "trace = dict (type='scattergeo',\n",
    "              \n",
    "              lon = [0,-74,-25] ,\n",
    "              lat = [0,40.7,20.5],\n",
    "              \n",
    "              marker = dict (size=30),\n",
    "              \n",
    "              mode='markers',\n",
    "    \n",
    ") \n",
    "\n",
    "data=[trace]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "layout = dict(showlegend = False,\n",
    "              \n",
    "              geo = dict(showland = True)\n",
    "             )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "fig=dict(data=data,\n",
    "         layout=layout)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": false
       },
       "data": [
        {
         "lat": [
          0,
          40.7,
          20.5
         ],
         "lon": [
          0,
          -74,
          -25
         ],
         "marker": {
          "size": 30
         },
         "mode": "markers",
         "type": "scattergeo"
        }
       ],
       "layout": {
        "geo": {
         "showland": true
        },
        "showlegend": false,
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"89caca5e-7118-4da9-987c-554ba4f7755c\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"89caca5e-7118-4da9-987c-554ba4f7755c\")) {                    Plotly.newPlot(                        \"89caca5e-7118-4da9-987c-554ba4f7755c\",                        [{\"lat\": [0, 40.7, 20.5], \"lon\": [0, -74, -25], \"marker\": {\"size\": 30}, \"mode\": \"markers\", \"type\": \"scattergeo\"}],                        {\"geo\": {\"showland\": true}, \"showlegend\": false, \"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"pie\": [{\"automargin\": true, \"type\": \"pie\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"autotypenumbers\": \"strict\", \"coloraxis\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('89caca5e-7118-4da9-987c-554ba4f7755c');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "offline.iplot(fig)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Download the Meteorite Landings dataset\n",
    "Dataset location: https://www.kaggle.com/nasa/meteorite-landings\n",
    "\n",
    "This contains a list of over 45,000 meteorite landings from the year 301 until 2013. Includes a handful of predicted landings in the future."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25000000"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data = pd.read_csv('Hyper Cars 2019.csv')\n",
    "data['Cost'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Car Name         object\n",
       "Engine           object\n",
       "Horsepower        int64\n",
       "Transmission      int64\n",
       "Top-speed         int64\n",
       "Cost              int64\n",
       "Latitude        float64\n",
       "Longitude       float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### We restrict our data to meteors which landed in the year 2007\n",
    "We don't wish to plot 45,000 meteor landings on our map"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Obtain the list of latitudes and longitudes\n",
    "These will make up the x and y coordinates of our plot. We have to round up longitudes and latitudes as the points plotted by original values are not accurate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# latitudes = df['Latitude'].round(2)\n",
    "# longitudes = df['Longitude'].round(2)\n",
    "\n",
    "# not rounded\n",
    "latitudes = df['Latitude']\n",
    "longitudes = df['Longitude']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### We set a scaling factor\n",
    "Since the bubbles on our plot will represent the mass of the meteors, they will be rather large by default. For that reason we apply a scaling factor for the marker size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "scale=7500"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Define the trace\n",
    "We set the following attributes:\n",
    "* latitudes and longitudes of the meteor landing sites\n",
    "* the hovertext will contain the name of the meteor\n",
    "* the area of the markers will represent the mass of the meteor with a scaling factor "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "colors =['red', 'blue', 'green', 'orange', 'pink', 'purple', 'yellow', 'grey', 'indigo', 'pink']\n",
    "trace = dict (type='scattergeo',\n",
    "              \n",
    "              lat = latitudes,\n",
    "              lon = longitudes ,     \n",
    "              \n",
    "              text = df['Car Name'],\n",
    "              \n",
    "              \n",
    "              marker = dict(size=df['Cost']/scale, color = colors,\n",
    "                            sizemode = 'area'),\n",
    "                           \n",
    "              \n",
    "              mode='markers'\n",
    "    \n",
    ") \n",
    "\n",
    "data=[trace]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Define the layout\n",
    "Here, we set the color to use to represent the landmass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "layout = dict(title = 'Hyper Cars Based on Manufacturing Location and Price',\n",
    "              showlegend = False,\n",
    "              \n",
    "              geo = dict(showland = True,\n",
    "                         landcolor = '#96f2ff',\n",
    "                         scope = 'europe')\n",
    "             )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "fig=dict(data=data,\n",
    "         layout=layout)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": false
       },
       "data": [
        {
         "lat": [
          51.3168,
          48.5437,
          48.7758,
          51.3168,
          56.2457,
          48.7758,
          44.5263,
          44.6471,
          52.2671,
          48.5437
         ],
         "lon": [
          0.56,
          7.4915,
          9.1829,
          0.56,
          12.8639,
          9.1829,
          10.8667,
          10.9252,
          1.4675,
          7.4915
         ],
         "marker": {
          "color": [
           "red",
           "blue",
           "green",
           "orange",
           "pink",
           "purple",
           "yellow",
           "grey",
           "indigo",
           "pink"
          ],
          "size": [
           3333.3333333333335,
           400,
           353.73333333333335,
           200,
           333.3333333333333,
           120,
           266.6666666666667,
           340,
           426.6666666666667,
           266.6666666666667
          ],
          "sizemode": "area"
         },
         "mode": "markers",
         "text": [
          "McLaren F1",
          "Bugatti Chiron",
          "Mercedes-AMG ONE",
          "McLaren Senna",
          "Koenigseeg Agera",
          "Porsche 918 Spyder",
          "Ferrari LaFerrari",
          "Pagaani Huayra BC",
          "Aston Martin Valkyrie",
          "Bugatti Veyronre"
         ],
         "type": "scattergeo"
        }
       ],
       "layout": {
        "geo": {
         "landcolor": "#96f2ff",
         "scope": "europe",
         "showland": true
        },
        "showlegend": false,
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Hyper Cars Based on Manufacturing Location and Price"
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"5357eeaf-43ca-46d1-84e1-c1aa2b44ff56\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"5357eeaf-43ca-46d1-84e1-c1aa2b44ff56\")) {                    Plotly.newPlot(                        \"5357eeaf-43ca-46d1-84e1-c1aa2b44ff56\",                        [{\"lat\": [51.3168, 48.5437, 48.7758, 51.3168, 56.2457, 48.7758, 44.5263, 44.6471, 52.2671, 48.5437], \"lon\": [0.56, 7.4915, 9.1829, 0.56, 12.8639, 9.1829, 10.8667, 10.9252, 1.4675, 7.4915], \"marker\": {\"color\": [\"red\", \"blue\", \"green\", \"orange\", \"pink\", \"purple\", \"yellow\", \"grey\", \"indigo\", \"pink\"], \"size\": [3333.3333333333335, 400.0, 353.73333333333335, 200.0, 333.3333333333333, 120.0, 266.6666666666667, 340.0, 426.6666666666667, 266.6666666666667], \"sizemode\": \"area\"}, \"mode\": \"markers\", \"text\": [\"McLaren F1\", \"Bugatti Chiron\", \"Mercedes-AMG ONE\", \"McLaren Senna\", \"Koenigseeg Agera\", \"Porsche 918 Spyder\", \"Ferrari LaFerrari\", \"Pagaani Huayra BC\", \"Aston Martin Valkyrie\", \"Bugatti Veyronre\"], \"type\": \"scattergeo\"}],                        {\"geo\": {\"landcolor\": \"#96f2ff\", \"scope\": \"europe\", \"showland\": true}, \"showlegend\": false, \"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"pie\": [{\"automargin\": true, \"type\": \"pie\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"autotypenumbers\": \"strict\", \"coloraxis\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}, \"title\": {\"text\": \"Hyper Cars Based on Manufacturing Location and Price\"}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('5357eeaf-43ca-46d1-84e1-c1aa2b44ff56');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "offline.iplot(fig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Car Name=McLaren F1<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>",
         "hovertext": [
          "McLaren F1"
         ],
         "lat": [
          51.3168
         ],
         "legendgroup": "McLaren F1",
         "lon": [
          0.56
         ],
         "marker": {
          "color": "#636efa",
          "size": [
           25000000
          ],
          "sizemode": "area",
          "sizeref": 62500,
          "symbol": "pentagon-open-dot"
         },
         "mode": "markers",
         "name": "McLaren F1",
         "showlegend": true,
         "type": "scattergeo"
        },
        {
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Car Name=Bugatti Chiron<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>",
         "hovertext": [
          "Bugatti Chiron"
         ],
         "lat": [
          48.5437
         ],
         "legendgroup": "Bugatti Chiron",
         "lon": [
          7.4915
         ],
         "marker": {
          "color": "#EF553B",
          "size": [
           3000000
          ],
          "sizemode": "area",
          "sizeref": 62500,
          "symbol": "pentagon-open-dot"
         },
         "mode": "markers",
         "name": "Bugatti Chiron",
         "showlegend": true,
         "type": "scattergeo"
        },
        {
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Car Name=Mercedes-AMG ONE<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>",
         "hovertext": [
          "Mercedes-AMG ONE"
         ],
         "lat": [
          48.7758
         ],
         "legendgroup": "Mercedes-AMG ONE",
         "lon": [
          9.1829
         ],
         "marker": {
          "color": "#00cc96",
          "size": [
           2653000
          ],
          "sizemode": "area",
          "sizeref": 62500,
          "symbol": "pentagon-open-dot"
         },
         "mode": "markers",
         "name": "Mercedes-AMG ONE",
         "showlegend": true,
         "type": "scattergeo"
        },
        {
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Car Name=McLaren Senna<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>",
         "hovertext": [
          "McLaren Senna"
         ],
         "lat": [
          51.3168
         ],
         "legendgroup": "McLaren Senna",
         "lon": [
          0.56
         ],
         "marker": {
          "color": "#ab63fa",
          "size": [
           1500000
          ],
          "sizemode": "area",
          "sizeref": 62500,
          "symbol": "pentagon-open-dot"
         },
         "mode": "markers",
         "name": "McLaren Senna",
         "showlegend": true,
         "type": "scattergeo"
        },
        {
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Car Name=Koenigseeg Agera<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>",
         "hovertext": [
          "Koenigseeg Agera"
         ],
         "lat": [
          56.2457
         ],
         "legendgroup": "Koenigseeg Agera",
         "lon": [
          12.8639
         ],
         "marker": {
          "color": "#FFA15A",
          "size": [
           2500000
          ],
          "sizemode": "area",
          "sizeref": 62500,
          "symbol": "pentagon-open-dot"
         },
         "mode": "markers",
         "name": "Koenigseeg Agera",
         "showlegend": true,
         "type": "scattergeo"
        },
        {
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Car Name=Porsche 918 Spyder<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>",
         "hovertext": [
          "Porsche 918 Spyder"
         ],
         "lat": [
          48.7758
         ],
         "legendgroup": "Porsche 918 Spyder",
         "lon": [
          9.1829
         ],
         "marker": {
          "color": "#19d3f3",
          "size": [
           900000
          ],
          "sizemode": "area",
          "sizeref": 62500,
          "symbol": "pentagon-open-dot"
         },
         "mode": "markers",
         "name": "Porsche 918 Spyder",
         "showlegend": true,
         "type": "scattergeo"
        },
        {
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Car Name=Ferrari LaFerrari<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>",
         "hovertext": [
          "Ferrari LaFerrari"
         ],
         "lat": [
          44.5263
         ],
         "legendgroup": "Ferrari LaFerrari",
         "lon": [
          10.8667
         ],
         "marker": {
          "color": "#FF6692",
          "size": [
           2000000
          ],
          "sizemode": "area",
          "sizeref": 62500,
          "symbol": "pentagon-open-dot"
         },
         "mode": "markers",
         "name": "Ferrari LaFerrari",
         "showlegend": true,
         "type": "scattergeo"
        },
        {
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Car Name=Pagaani Huayra BC<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>",
         "hovertext": [
          "Pagaani Huayra BC"
         ],
         "lat": [
          44.6471
         ],
         "legendgroup": "Pagaani Huayra BC",
         "lon": [
          10.9252
         ],
         "marker": {
          "color": "#B6E880",
          "size": [
           2550000
          ],
          "sizemode": "area",
          "sizeref": 62500,
          "symbol": "pentagon-open-dot"
         },
         "mode": "markers",
         "name": "Pagaani Huayra BC",
         "showlegend": true,
         "type": "scattergeo"
        },
        {
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Car Name=Aston Martin Valkyrie<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>",
         "hovertext": [
          "Aston Martin Valkyrie"
         ],
         "lat": [
          52.2671
         ],
         "legendgroup": "Aston Martin Valkyrie",
         "lon": [
          1.4675
         ],
         "marker": {
          "color": "#FF97FF",
          "size": [
           3200000
          ],
          "sizemode": "area",
          "sizeref": 62500,
          "symbol": "pentagon-open-dot"
         },
         "mode": "markers",
         "name": "Aston Martin Valkyrie",
         "showlegend": true,
         "type": "scattergeo"
        },
        {
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Car Name=Bugatti Veyronre<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>",
         "hovertext": [
          "Bugatti Veyronre"
         ],
         "lat": [
          48.5437
         ],
         "legendgroup": "Bugatti Veyronre",
         "lon": [
          7.4915
         ],
         "marker": {
          "color": "#FECB52",
          "size": [
           2000000
          ],
          "sizemode": "area",
          "sizeref": 62500,
          "symbol": "pentagon-open-dot"
         },
         "mode": "markers",
         "name": "Bugatti Veyronre",
         "showlegend": true,
         "type": "scattergeo"
        }
       ],
       "layout": {
        "geo": {
         "center": {},
         "domain": {
          "x": [
           0,
           1
          ],
          "y": [
           0,
           1
          ]
         },
         "scope": "europe"
        },
        "hoverlabel": {
         "font": {
          "size": 20
         }
        },
        "legend": {
         "itemsizing": "constant",
         "title": {
          "text": "Car Name"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"8afacbdc-dfa9-4df6-9f36-c1d19f02753c\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"8afacbdc-dfa9-4df6-9f36-c1d19f02753c\")) {                    Plotly.newPlot(                        \"8afacbdc-dfa9-4df6-9f36-c1d19f02753c\",                        [{\"geo\": \"geo\", \"hovertemplate\": \"<b>%{hovertext}</b><br><br>Car Name=McLaren F1<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>\", \"hovertext\": [\"McLaren F1\"], \"lat\": [51.3168], \"legendgroup\": \"McLaren F1\", \"lon\": [0.56], \"marker\": {\"color\": \"#636efa\", \"size\": [25000000], \"sizemode\": \"area\", \"sizeref\": 62500.0, \"symbol\": \"pentagon-open-dot\"}, \"mode\": \"markers\", \"name\": \"McLaren F1\", \"showlegend\": true, \"type\": \"scattergeo\"}, {\"geo\": \"geo\", \"hovertemplate\": \"<b>%{hovertext}</b><br><br>Car Name=Bugatti Chiron<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>\", \"hovertext\": [\"Bugatti Chiron\"], \"lat\": [48.5437], \"legendgroup\": \"Bugatti Chiron\", \"lon\": [7.4915], \"marker\": {\"color\": \"#EF553B\", \"size\": [3000000], \"sizemode\": \"area\", \"sizeref\": 62500.0, \"symbol\": \"pentagon-open-dot\"}, \"mode\": \"markers\", \"name\": \"Bugatti Chiron\", \"showlegend\": true, \"type\": \"scattergeo\"}, {\"geo\": \"geo\", \"hovertemplate\": \"<b>%{hovertext}</b><br><br>Car Name=Mercedes-AMG ONE<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>\", \"hovertext\": [\"Mercedes-AMG ONE\"], \"lat\": [48.7758], \"legendgroup\": \"Mercedes-AMG ONE\", \"lon\": [9.1829], \"marker\": {\"color\": \"#00cc96\", \"size\": [2653000], \"sizemode\": \"area\", \"sizeref\": 62500.0, \"symbol\": \"pentagon-open-dot\"}, \"mode\": \"markers\", \"name\": \"Mercedes-AMG ONE\", \"showlegend\": true, \"type\": \"scattergeo\"}, {\"geo\": \"geo\", \"hovertemplate\": \"<b>%{hovertext}</b><br><br>Car Name=McLaren Senna<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>\", \"hovertext\": [\"McLaren Senna\"], \"lat\": [51.3168], \"legendgroup\": \"McLaren Senna\", \"lon\": [0.56], \"marker\": {\"color\": \"#ab63fa\", \"size\": [1500000], \"sizemode\": \"area\", \"sizeref\": 62500.0, \"symbol\": \"pentagon-open-dot\"}, \"mode\": \"markers\", \"name\": \"McLaren Senna\", \"showlegend\": true, \"type\": \"scattergeo\"}, {\"geo\": \"geo\", \"hovertemplate\": \"<b>%{hovertext}</b><br><br>Car Name=Koenigseeg Agera<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>\", \"hovertext\": [\"Koenigseeg Agera\"], \"lat\": [56.2457], \"legendgroup\": \"Koenigseeg Agera\", \"lon\": [12.8639], \"marker\": {\"color\": \"#FFA15A\", \"size\": [2500000], \"sizemode\": \"area\", \"sizeref\": 62500.0, \"symbol\": \"pentagon-open-dot\"}, \"mode\": \"markers\", \"name\": \"Koenigseeg Agera\", \"showlegend\": true, \"type\": \"scattergeo\"}, {\"geo\": \"geo\", \"hovertemplate\": \"<b>%{hovertext}</b><br><br>Car Name=Porsche 918 Spyder<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>\", \"hovertext\": [\"Porsche 918 Spyder\"], \"lat\": [48.7758], \"legendgroup\": \"Porsche 918 Spyder\", \"lon\": [9.1829], \"marker\": {\"color\": \"#19d3f3\", \"size\": [900000], \"sizemode\": \"area\", \"sizeref\": 62500.0, \"symbol\": \"pentagon-open-dot\"}, \"mode\": \"markers\", \"name\": \"Porsche 918 Spyder\", \"showlegend\": true, \"type\": \"scattergeo\"}, {\"geo\": \"geo\", \"hovertemplate\": \"<b>%{hovertext}</b><br><br>Car Name=Ferrari LaFerrari<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>\", \"hovertext\": [\"Ferrari LaFerrari\"], \"lat\": [44.5263], \"legendgroup\": \"Ferrari LaFerrari\", \"lon\": [10.8667], \"marker\": {\"color\": \"#FF6692\", \"size\": [2000000], \"sizemode\": \"area\", \"sizeref\": 62500.0, \"symbol\": \"pentagon-open-dot\"}, \"mode\": \"markers\", \"name\": \"Ferrari LaFerrari\", \"showlegend\": true, \"type\": \"scattergeo\"}, {\"geo\": \"geo\", \"hovertemplate\": \"<b>%{hovertext}</b><br><br>Car Name=Pagaani Huayra BC<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>\", \"hovertext\": [\"Pagaani Huayra BC\"], \"lat\": [44.6471], \"legendgroup\": \"Pagaani Huayra BC\", \"lon\": [10.9252], \"marker\": {\"color\": \"#B6E880\", \"size\": [2550000], \"sizemode\": \"area\", \"sizeref\": 62500.0, \"symbol\": \"pentagon-open-dot\"}, \"mode\": \"markers\", \"name\": \"Pagaani Huayra BC\", \"showlegend\": true, \"type\": \"scattergeo\"}, {\"geo\": \"geo\", \"hovertemplate\": \"<b>%{hovertext}</b><br><br>Car Name=Aston Martin Valkyrie<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>\", \"hovertext\": [\"Aston Martin Valkyrie\"], \"lat\": [52.2671], \"legendgroup\": \"Aston Martin Valkyrie\", \"lon\": [1.4675], \"marker\": {\"color\": \"#FF97FF\", \"size\": [3200000], \"sizemode\": \"area\", \"sizeref\": 62500.0, \"symbol\": \"pentagon-open-dot\"}, \"mode\": \"markers\", \"name\": \"Aston Martin Valkyrie\", \"showlegend\": true, \"type\": \"scattergeo\"}, {\"geo\": \"geo\", \"hovertemplate\": \"<b>%{hovertext}</b><br><br>Car Name=Bugatti Veyronre<br>Cost=%{marker.size}<br>Latitude=%{lat}<br>Longitude=%{lon}<extra></extra>\", \"hovertext\": [\"Bugatti Veyronre\"], \"lat\": [48.5437], \"legendgroup\": \"Bugatti Veyronre\", \"lon\": [7.4915], \"marker\": {\"color\": \"#FECB52\", \"size\": [2000000], \"sizemode\": \"area\", \"sizeref\": 62500.0, \"symbol\": \"pentagon-open-dot\"}, \"mode\": \"markers\", \"name\": \"Bugatti Veyronre\", \"showlegend\": true, \"type\": \"scattergeo\"}],                        {\"geo\": {\"center\": {}, \"domain\": {\"x\": [0.0, 1.0], \"y\": [0.0, 1.0]}, \"scope\": \"europe\"}, \"hoverlabel\": {\"font\": {\"size\": 20}}, \"legend\": {\"itemsizing\": \"constant\", \"title\": {\"text\": \"Car Name\"}, \"tracegroupgap\": 0}, \"margin\": {\"t\": 60}, \"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"pie\": [{\"automargin\": true, \"type\": \"pie\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"autotypenumbers\": \"strict\", \"coloraxis\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('8afacbdc-dfa9-4df6-9f36-c1d19f02753c');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = px.scatter_geo(df, lat = latitudes,\n",
    "                     lon = longitudes, \n",
    "                     color=\"Car Name\",\n",
    "                     \n",
    "                     hover_name=\"Car Name\", size=df['Cost'],\n",
    "                     scope = 'europe')\n",
    "                     #marker = dict(sizemode = 'area'))\n",
    "\n",
    "fig.update_layout(hoverlabel_font_size=20)\n",
    "\n",
    "fig.update_traces(marker_symbol=\"pentagon-open-dot\", selector=dict(type='scattergeo')) \n",
    "\n",
    "     \n",
    "  \n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "e_data = pd.read_csv('big earthquakes.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1970-06-14T00:00:11.000Z'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "e_data['time'][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "mag7 = e_data[e_data['mag'] >= 7]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "time          object\n",
       "latitude     float64\n",
       "longitude    float64\n",
       "mag          float64\n",
       "place         object\n",
       "type          object\n",
       "dtype: object"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mag7.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "mag_latitudes = mag7['latitude']\n",
    "mag_longitudes = mag7['longitude']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>mag=%{marker.color}<br>latitude=%{lat}<br>longitude=%{lon}<extra></extra>",
         "hovertext": [
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.8,
          7.8,
          7.8,
          7.8,
          7.8,
          7.8,
          7.8,
          7.8,
          7.8,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          8,
          8,
          8,
          8,
          8,
          8,
          8,
          8,
          8.1,
          8.2,
          8.2,
          8.2,
          8.3,
          8.3
         ],
         "lat": [
          -52.028,
          32.053,
          25.977,
          -11.154,
          0.653,
          51.409,
          -63.398,
          -4.33,
          51.396,
          63.952,
          -5.754,
          -5.116,
          -5.912,
          -13.248,
          23.564,
          -20.122,
          13.372,
          -60.823,
          40.641,
          43.024,
          -4.882,
          -12.519,
          44.915,
          40.311,
          40.381,
          24.531,
          3.397,
          7.409,
          16.773,
          -17.098,
          10.204,
          23.247,
          43.53,
          51.744,
          -22.293,
          -17.26,
          16.558,
          -51.225,
          -12.597,
          38.026,
          -30.383,
          -4.843,
          27.793,
          14.066,
          -2.823,
          40.32,
          1.622,
          15.344,
          39.431,
          -14.043,
          -13.987,
          18.404,
          -60.063,
          -24.495,
          -22.767,
          -7.288,
          -24.71,
          -6.526,
          -6.081,
          -30.523,
          45.841,
          -10.97,
          23.613,
          8.87,
          42.453,
          1.156,
          54.567,
          -20.252,
          -13.108,
          41.679,
          -20.878,
          -11.122,
          7.219,
          -22.671,
          36.379,
          -45.277,
          51.934,
          -20.23,
          1.015,
          -20.553,
          -1.278,
          40.4055,
          40.246,
          -2.75,
          10.797,
          1,
          24.185,
          52.487,
          27.236,
          -55.918,
          41.415,
          -11.857,
          23.107,
          -17.76,
          43.318,
          -7.383,
          -38.453,
          -4.603,
          -4.517,
          -59.426,
          42.839,
          -11.132,
          60.642,
          19.066,
          -10.615,
          33.962,
          30.013,
          -29.934,
          13.752,
          27.929,
          36.194,
          8.717,
          55.867,
          -4.843,
          8.185,
          -22.022,
          0.197,
          -1.639,
          -13.966,
          -21.277,
          -20.19,
          -22.037,
          -5.577,
          -17.192,
          -18.771,
          2.305,
          -8.281,
          55.543,
          -6.436,
          -18.318,
          5.358,
          -7.363,
          11.76,
          -19.435,
          53.452,
          -5.982,
          7.239,
          -10.972,
          13.525,
          -37.759,
          12.626,
          52.629,
          18.856,
          27.929,
          -6.903,
          15.978,
          12.614,
          -21.999,
          29.976,
          -32.115,
          6.785,
          -54.476,
          -4.026,
          33.453,
          -25.758,
          -5.154,
          50.486,
          -15.117,
          -14.434,
          -29.082,
          -8.42,
          -12.5,
          -8.031,
          -25.856,
          -30.683,
          -21.89,
          41.117,
          -33.134,
          39.243,
          -24.133,
          -60.665,
          33.683,
          44.117,
          -15.86,
          -34.131,
          -5.599,
          -4.448,
          45.547,
          -21.702,
          0.151,
          -19.022,
          -24.753,
          49.037,
          5.121,
          -15.355,
          -9.094,
          4.554,
          -56.032,
          40.3353333,
          -6.075,
          -22.483,
          7.075,
          14.717,
          -16.62,
          12.059,
          -29.211,
          -5.771,
          16.84,
          28.826,
          45.324,
          -24.061,
          -6.518,
          18.219,
          14.52,
          -59.232,
          52.301,
          46.505,
          52.803,
          22.632,
          7.747,
          39.457,
          39.121,
          36.195,
          18.048,
          13.332,
          -7.481,
          -6.852,
          8.147,
          -4.439,
          -17.94,
          13.477,
          25.149,
          9.919,
          -26.802,
          7.191,
          34.2,
          42.142,
          -6.582,
          42.34,
          43.905,
          51.478,
          33.825,
          15.791,
          51.692,
          -2.839,
          -11.481,
          33.362,
          31.398,
          39.664,
          -31.028,
          22.282,
          33.386,
          -46.675,
          40.462,
          -26.535,
          36.372,
          29.384,
          -0.086,
          -33.207,
          36.19,
          23.901,
          -6.088,
          -58.893,
          -6.266,
          39.837,
          36.957,
          -19.247,
          -15.199,
          16.779,
          -20.69,
          13.402,
          -6.05,
          18.481,
          -14.464,
          17.3,
          15.324,
          39.57,
          45.772,
          -9.89,
          -9.844,
          -9.965,
          44.932,
          -12.41,
          5.167,
          1.795,
          -5.097,
          1.196,
          51.218,
          -9.593,
          55.959,
          56.724,
          -12.265,
          53.113,
          -16.696,
          44.244,
          17.813,
          -48.786,
          -4.883,
          -10.012,
          17.802,
          -24.388,
          -10.366,
          8.337,
          -22.122,
          15.125,
          9.685,
          45.533,
          43.3,
          -18.039,
          -3.184,
          3.752,
          43.233,
          -38.183,
          -7.104,
          19.333,
          38.19,
          16.01,
          1.598,
          -14.96,
          -28.117,
          22.789,
          15.679,
          11.742,
          42.851,
          -23.008,
          -5.799,
          -14.993,
          -12.584,
          -32.601,
          -24.894,
          -16.264,
          56.953,
          1.186,
          -8.48,
          12.982,
          -10.477,
          40.525,
          35.997,
          -6.59,
          6.262,
          -1.679,
          -12.525,
          58.679,
          44.663,
          0.729,
          51.564,
          -7.137,
          -5.524,
          6.405,
          -28.427,
          -33.135,
          18.19,
          51.52,
          -23.34,
          19.055,
          -4.817,
          -52.341,
          -13.841,
          -0.891,
          -11.164,
          43.773
         ],
         "legendgroup": "",
         "lon": [
          -74.07,
          131.782,
          95.34,
          163.377,
          98.711,
          -176.974,
          -61.377,
          102.285,
          -177.318,
          145.965,
          153.868,
          152.282,
          130.603,
          166.407,
          121.539,
          168.949,
          122.787,
          -21.549,
          122.58,
          147.734,
          102.198,
          166.499,
          149.123,
          63.773,
          63.472,
          98.71,
          96.318,
          -78.127,
          122.327,
          -172.264,
          -85.222,
          122.075,
          146.753,
          176.274,
          171.742,
          167.601,
          -98.358,
          160.513,
          165.931,
          20.228,
          -179.339,
          -78.103,
          62.054,
          -91.924,
          118.806,
          63.35,
          126.411,
          120.61,
          75.224,
          166.24,
          166.185,
          -102.973,
          -26.916,
          -70.701,
          -66.205,
          154.371,
          -70.568,
          152.779,
          133.667,
          -178.414,
          26.668,
          -70.776,
          95.901,
          126.48,
          43.673,
          122.957,
          -161.606,
          -176.218,
          -72.187,
          -125.856,
          -178.591,
          165.239,
          126.57,
          -66.543,
          70.868,
          166.927,
          158.647,
          169.789,
          127.733,
          169.361,
          -23.569,
          -126.3028333,
          142.175,
          -77.881,
          -42.254,
          120.45,
          102.543,
          -174.915,
          140.23,
          -2.668,
          143.416,
          166.557,
          121.974,
          -175.066,
          146.442,
          155.575,
          -73.431,
          140.091,
          139.918,
          -20.508,
          78.606,
          162.136,
          -141.593,
          122.096,
          161.284,
          59.726,
          57.794,
          -177.741,
          124.358,
          136.967,
          141.702,
          -83.123,
          161.287,
          151.577,
          -38.794,
          170.95,
          98.027,
          134.911,
          166.516,
          170.102,
          178.86,
          -178.925,
          130.791,
          -72.305,
          -172.415,
          126.76,
          -71.381,
          -156.835,
          146.383,
          168.063,
          31.848,
          120.363,
          121.899,
          169.132,
          169.871,
          -77.094,
          126.645,
          164.181,
          121.067,
          178.752,
          125.297,
          142.827,
          145.218,
          130.175,
          129.151,
          -98.07,
          125.154,
          -65.719,
          68.208,
          179.791,
          126.682,
          -64.499,
          -80.542,
          140.929,
          179.665,
          154.191,
          156.584,
          166.896,
          166.863,
          -175.954,
          154.034,
          -77.786,
          155.538,
          -175.406,
          -177.358,
          169.853,
          -124.253,
          -73.074,
          25.227,
          -175.864,
          -25.451,
          136.894,
          148.192,
          -173.643,
          -71.618,
          151.045,
          143.943,
          26.316,
          -176.616,
          -77.821,
          -69.991,
          -70.433,
          141.847,
          32.145,
          167.464,
          158.442,
          -77.442,
          -25.266,
          -124.2286667,
          147.572,
          -178.413,
          -76.862,
          -92.645,
          167.518,
          125.58,
          -177.589,
          154.347,
          -93.469,
          34.799,
          149.892,
          -177.036,
          154.999,
          -102.756,
          -92.653,
          158.902,
          151.613,
          141.199,
          159.199,
          122.269,
          -77.688,
          73.83,
          44.029,
          1.354,
          -102.084,
          -89.387,
          128.168,
          72.11,
          123.762,
          152.828,
          -172.225,
          124.616,
          95.127,
          -84.808,
          -63.349,
          126.762,
          -116.437,
          73.575,
          130.393,
          132.865,
          147.916,
          -176.847,
          59.809,
          121.63,
          -131.055,
          -77.322,
          166.339,
          140.827,
          100.581,
          118.401,
          -67.767,
          121.512,
          57.434,
          165.707,
          139.102,
          -70.563,
          70.738,
          138.935,
          122.517,
          -71.663,
          70.896,
          121.574,
          147.689,
          158.513,
          149.06,
          142.76,
          49.409,
          168.948,
          -173.529,
          -98.597,
          -178.31,
          120.275,
          152.932,
          -102.996,
          166.601,
          -62,
          -89.101,
          117.978,
          26.761,
          160.348,
          160.822,
          160.731,
          148.439,
          166.381,
          125.124,
          126.519,
          150.967,
          122.787,
          157.829,
          -79.587,
          163.269,
          -135.853,
          -77.795,
          173.497,
          -172.095,
          148.862,
          -101.276,
          164.357,
          153.581,
          160.469,
          -101.647,
          -70.161,
          160.819,
          126.729,
          175.163,
          147.596,
          -83.073,
          151.021,
          143.691,
          -178.413,
          139.722,
          124.221,
          145.785,
          -73.232,
          155.152,
          -155.0015,
          142.028,
          -96.591,
          -79.358,
          -173.085,
          -176.367,
          99.611,
          121.172,
          -87.34,
          139.197,
          169.9,
          154.178,
          -75.675,
          166.676,
          -71.076,
          -175.119,
          -172.467,
          -143.032,
          122.857,
          121.896,
          144.801,
          112.835,
          143.419,
          -17.649,
          155.054,
          124.023,
          136.04,
          165.916,
          -142.786,
          149.3,
          119.931,
          -177.632,
          122.589,
          153.85,
          126.64,
          -177.657,
          -71.871,
          -102.533,
          -174.776,
          -70.294,
          -104.205,
          153.172,
          160.568,
          -67.553,
          136.952,
          118.378,
          147.321
         ],
         "marker": {
          "color": [
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           8,
           8,
           8,
           8,
           8,
           8,
           8,
           8,
           8.1,
           8.2,
           8.2,
           8.2,
           8.3,
           8.3
          ],
          "coloraxis": "coloraxis",
          "size": [
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           8,
           8,
           8,
           8,
           8,
           8,
           8,
           8,
           8.1,
           8.2,
           8.2,
           8.2,
           8.3,
           8.3
          ],
          "sizemode": "area",
          "sizeref": 0.02075,
          "symbol": "star-triangle-down-open"
         },
         "mode": "markers",
         "name": "",
         "showlegend": false,
         "type": "scattergeo"
        }
       ],
       "layout": {
        "coloraxis": {
         "colorbar": {
          "title": {
           "text": "mag"
          }
         },
         "colorscale": [
          [
           0,
           "#0d0887"
          ],
          [
           0.1111111111111111,
           "#46039f"
          ],
          [
           0.2222222222222222,
           "#7201a8"
          ],
          [
           0.3333333333333333,
           "#9c179e"
          ],
          [
           0.4444444444444444,
           "#bd3786"
          ],
          [
           0.5555555555555556,
           "#d8576b"
          ],
          [
           0.6666666666666666,
           "#ed7953"
          ],
          [
           0.7777777777777778,
           "#fb9f3a"
          ],
          [
           0.8888888888888888,
           "#fdca26"
          ],
          [
           1,
           "#f0f921"
          ]
         ]
        },
        "geo": {
         "center": {},
         "domain": {
          "x": [
           0,
           1
          ],
          "y": [
           0,
           1
          ]
         }
        },
        "hoverlabel": {
         "font": {
          "size": 20
         }
        },
        "legend": {
         "itemsizing": "constant",
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"5106e323-d152-4e94-92ac-db14a4319fe6\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"5106e323-d152-4e94-92ac-db14a4319fe6\")) {                    Plotly.newPlot(                        \"5106e323-d152-4e94-92ac-db14a4319fe6\",                        [{\"geo\": \"geo\", \"hovertemplate\": \"<b>%{hovertext}</b><br><br>mag=%{marker.color}<br>latitude=%{lat}<br>longitude=%{lon}<extra></extra>\", \"hovertext\": [7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.1, 8.2, 8.2, 8.2, 8.3, 8.3], \"lat\": [-52.028, 32.053, 25.977, -11.154, 0.653, 51.409, -63.398, -4.33, 51.396, 63.952, -5.754, -5.116, -5.912, -13.248, 23.564, -20.122, 13.372, -60.823, 40.641, 43.024, -4.882, -12.519, 44.915, 40.311, 40.381, 24.531, 3.397, 7.409, 16.773, -17.098, 10.204, 23.247, 43.53, 51.744, -22.293, -17.26, 16.558, -51.225, -12.597, 38.026, -30.383, -4.843, 27.793, 14.066, -2.823, 40.32, 1.622, 15.344, 39.431, -14.043, -13.987, 18.404, -60.063, -24.495, -22.767, -7.288, -24.71, -6.526, -6.081, -30.523, 45.841, -10.97, 23.613, 8.87, 42.453, 1.156, 54.567, -20.252, -13.108, 41.679, -20.878, -11.122, 7.219, -22.671, 36.379, -45.277, 51.934, -20.23, 1.015, -20.553, -1.278, 40.4055, 40.246, -2.75, 10.797, 1.0, 24.185, 52.487, 27.236, -55.918, 41.415, -11.857, 23.107, -17.76, 43.318, -7.383, -38.453, -4.603, -4.517, -59.426, 42.839, -11.132, 60.642, 19.066, -10.615, 33.962, 30.013, -29.934, 13.752, 27.929, 36.194, 8.717, 55.867, -4.843, 8.185, -22.022, 0.197, -1.639, -13.966, -21.277, -20.19, -22.037, -5.577, -17.192, -18.771, 2.305, -8.281, 55.543, -6.436, -18.318, 5.358, -7.363, 11.76, -19.435, 53.452, -5.982, 7.239, -10.972, 13.525, -37.759, 12.626, 52.629, 18.856, 27.929, -6.903, 15.978, 12.614, -21.999, 29.976, -32.115, 6.785, -54.476, -4.026, 33.453, -25.758, -5.154, 50.486, -15.117, -14.434, -29.082, -8.42, -12.5, -8.031, -25.856, -30.683, -21.89, 41.117, -33.134, 39.243, -24.133, -60.665, 33.683, 44.117, -15.86, -34.131, -5.599, -4.448, 45.547, -21.702, 0.151, -19.022, -24.753, 49.037, 5.121, -15.355, -9.094, 4.554, -56.032, 40.3353333, -6.075, -22.483, 7.075, 14.717, -16.62, 12.059, -29.211, -5.771, 16.84, 28.826, 45.324, -24.061, -6.518, 18.219, 14.52, -59.232, 52.301, 46.505, 52.803, 22.632, 7.747, 39.457, 39.121, 36.195, 18.048, 13.332, -7.481, -6.852, 8.147, -4.439, -17.94, 13.477, 25.149, 9.919, -26.802, 7.191, 34.2, 42.142, -6.582, 42.34, 43.905, 51.478, 33.825, 15.791, 51.692, -2.839, -11.481, 33.362, 31.398, 39.664, -31.028, 22.282, 33.386, -46.675, 40.462, -26.535, 36.372, 29.384, -0.086, -33.207, 36.19, 23.901, -6.088, -58.893, -6.266, 39.837, 36.957, -19.247, -15.199, 16.779, -20.69, 13.402, -6.05, 18.481, -14.464, 17.3, 15.324, 39.57, 45.772, -9.89, -9.844, -9.965, 44.932, -12.41, 5.167, 1.795, -5.097, 1.196, 51.218, -9.593, 55.959, 56.724, -12.265, 53.113, -16.696, 44.244, 17.813, -48.786, -4.883, -10.012, 17.802, -24.388, -10.366, 8.337, -22.122, 15.125, 9.685, 45.533, 43.3, -18.039, -3.184, 3.752, 43.233, -38.183, -7.104, 19.333, 38.19, 16.01, 1.598, -14.96, -28.117, 22.789, 15.679, 11.742, 42.851, -23.008, -5.799, -14.993, -12.584, -32.601, -24.894, -16.264, 56.953, 1.186, -8.48, 12.982, -10.477, 40.525, 35.997, -6.59, 6.262, -1.679, -12.525, 58.679, 44.663, 0.729, 51.564, -7.137, -5.524, 6.405, -28.427, -33.135, 18.19, 51.52, -23.34, 19.055, -4.817, -52.341, -13.841, -0.891, -11.164, 43.773], \"legendgroup\": \"\", \"lon\": [-74.07, 131.782, 95.34, 163.377, 98.711, -176.974, -61.377, 102.285, -177.318, 145.965, 153.868, 152.282, 130.603, 166.407, 121.539, 168.949, 122.787, -21.549, 122.58, 147.734, 102.198, 166.499, 149.123, 63.773, 63.472, 98.71, 96.318, -78.127, 122.327, -172.264, -85.222, 122.075, 146.753, 176.274, 171.742, 167.601, -98.358, 160.513, 165.931, 20.228, -179.339, -78.103, 62.054, -91.924, 118.806, 63.35, 126.411, 120.61, 75.224, 166.24, 166.185, -102.973, -26.916, -70.701, -66.205, 154.371, -70.568, 152.779, 133.667, -178.414, 26.668, -70.776, 95.901, 126.48, 43.673, 122.957, -161.606, -176.218, -72.187, -125.856, -178.591, 165.239, 126.57, -66.543, 70.868, 166.927, 158.647, 169.789, 127.733, 169.361, -23.569, -126.3028333, 142.175, -77.881, -42.254, 120.45, 102.543, -174.915, 140.23, -2.668, 143.416, 166.557, 121.974, -175.066, 146.442, 155.575, -73.431, 140.091, 139.918, -20.508, 78.606, 162.136, -141.593, 122.096, 161.284, 59.726, 57.794, -177.741, 124.358, 136.967, 141.702, -83.123, 161.287, 151.577, -38.794, 170.95, 98.027, 134.911, 166.516, 170.102, 178.86, -178.925, 130.791, -72.305, -172.415, 126.76, -71.381, -156.835, 146.383, 168.063, 31.848, 120.363, 121.899, 169.132, 169.871, -77.094, 126.645, 164.181, 121.067, 178.752, 125.297, 142.827, 145.218, 130.175, 129.151, -98.07, 125.154, -65.719, 68.208, 179.791, 126.682, -64.499, -80.542, 140.929, 179.665, 154.191, 156.584, 166.896, 166.863, -175.954, 154.034, -77.786, 155.538, -175.406, -177.358, 169.853, -124.253, -73.074, 25.227, -175.864, -25.451, 136.894, 148.192, -173.643, -71.618, 151.045, 143.943, 26.316, -176.616, -77.821, -69.991, -70.433, 141.847, 32.145, 167.464, 158.442, -77.442, -25.266, -124.2286667, 147.572, -178.413, -76.862, -92.645, 167.518, 125.58, -177.589, 154.347, -93.469, 34.799, 149.892, -177.036, 154.999, -102.756, -92.653, 158.902, 151.613, 141.199, 159.199, 122.269, -77.688, 73.83, 44.029, 1.354, -102.084, -89.387, 128.168, 72.11, 123.762, 152.828, -172.225, 124.616, 95.127, -84.808, -63.349, 126.762, -116.437, 73.575, 130.393, 132.865, 147.916, -176.847, 59.809, 121.63, -131.055, -77.322, 166.339, 140.827, 100.581, 118.401, -67.767, 121.512, 57.434, 165.707, 139.102, -70.563, 70.738, 138.935, 122.517, -71.663, 70.896, 121.574, 147.689, 158.513, 149.06, 142.76, 49.409, 168.948, -173.529, -98.597, -178.31, 120.275, 152.932, -102.996, 166.601, -62.0, -89.101, 117.978, 26.761, 160.348, 160.822, 160.731, 148.439, 166.381, 125.124, 126.519, 150.967, 122.787, 157.829, -79.587, 163.269, -135.853, -77.795, 173.497, -172.095, 148.862, -101.276, 164.357, 153.581, 160.469, -101.647, -70.161, 160.819, 126.729, 175.163, 147.596, -83.073, 151.021, 143.691, -178.413, 139.722, 124.221, 145.785, -73.232, 155.152, -155.0015, 142.028, -96.591, -79.358, -173.085, -176.367, 99.611, 121.172, -87.34, 139.197, 169.9, 154.178, -75.675, 166.676, -71.076, -175.119, -172.467, -143.032, 122.857, 121.896, 144.801, 112.835, 143.419, -17.649, 155.054, 124.023, 136.04, 165.916, -142.786, 149.3, 119.931, -177.632, 122.589, 153.85, 126.64, -177.657, -71.871, -102.533, -174.776, -70.294, -104.205, 153.172, 160.568, -67.553, 136.952, 118.378, 147.321], \"marker\": {\"color\": [7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.1, 8.2, 8.2, 8.2, 8.3, 8.3], \"coloraxis\": \"coloraxis\", \"size\": [7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.1, 8.2, 8.2, 8.2, 8.3, 8.3], \"sizemode\": \"area\", \"sizeref\": 0.02075, \"symbol\": \"star-triangle-down-open\"}, \"mode\": \"markers\", \"name\": \"\", \"showlegend\": false, \"type\": \"scattergeo\"}],                        {\"coloraxis\": {\"colorbar\": {\"title\": {\"text\": \"mag\"}}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"geo\": {\"center\": {}, \"domain\": {\"x\": [0.0, 1.0], \"y\": [0.0, 1.0]}}, \"hoverlabel\": {\"font\": {\"size\": 20}}, \"legend\": {\"itemsizing\": \"constant\", \"tracegroupgap\": 0}, \"margin\": {\"t\": 60}, \"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"pie\": [{\"automargin\": true, \"type\": \"pie\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"autotypenumbers\": \"strict\", \"coloraxis\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('5106e323-d152-4e94-92ac-db14a4319fe6');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "mag_fig = px.scatter_geo(mag7, lat = mag_latitudes,\n",
    "                     lon = mag_longitudes, \n",
    "                     color=\"mag\",\n",
    "                     \n",
    "                     hover_name= \"mag\", \n",
    "                     size=mag7['mag'],)\n",
    "\n",
    "mag_fig.update_layout(hoverlabel_font_size=20)\n",
    "\n",
    "mag_fig.update_traces(marker_symbol=\"star-triangle-down-open\", selector=dict(type='scattergeo')) \n",
    "\n",
    "     \n",
    "  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>mag=%{marker.color}<br>latitude=%{lat}<br>longitude=%{lon}<extra></extra>",
         "hovertext": [
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.1,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.3,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.4,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.5,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.7,
          7.8,
          7.8,
          7.8,
          7.8,
          7.8,
          7.8,
          7.8,
          7.8,
          7.8,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          8,
          8,
          8,
          8,
          8,
          8,
          8,
          8,
          8.1,
          8.2,
          8.2,
          8.2,
          8.3,
          8.3
         ],
         "lat": [
          -52.028,
          32.053,
          25.977,
          -11.154,
          0.653,
          51.409,
          -63.398,
          -4.33,
          51.396,
          63.952,
          -5.754,
          -5.116,
          -5.912,
          -13.248,
          23.564,
          -20.122,
          13.372,
          -60.823,
          40.641,
          43.024,
          -4.882,
          -12.519,
          44.915,
          40.311,
          40.381,
          24.531,
          3.397,
          7.409,
          16.773,
          -17.098,
          10.204,
          23.247,
          43.53,
          51.744,
          -22.293,
          -17.26,
          16.558,
          -51.225,
          -12.597,
          38.026,
          -30.383,
          -4.843,
          27.793,
          14.066,
          -2.823,
          40.32,
          1.622,
          15.344,
          39.431,
          -14.043,
          -13.987,
          18.404,
          -60.063,
          -24.495,
          -22.767,
          -7.288,
          -24.71,
          -6.526,
          -6.081,
          -30.523,
          45.841,
          -10.97,
          23.613,
          8.87,
          42.453,
          1.156,
          54.567,
          -20.252,
          -13.108,
          41.679,
          -20.878,
          -11.122,
          7.219,
          -22.671,
          36.379,
          -45.277,
          51.934,
          -20.23,
          1.015,
          -20.553,
          -1.278,
          40.4055,
          40.246,
          -2.75,
          10.797,
          1,
          24.185,
          52.487,
          27.236,
          -55.918,
          41.415,
          -11.857,
          23.107,
          -17.76,
          43.318,
          -7.383,
          -38.453,
          -4.603,
          -4.517,
          -59.426,
          42.839,
          -11.132,
          60.642,
          19.066,
          -10.615,
          33.962,
          30.013,
          -29.934,
          13.752,
          27.929,
          36.194,
          8.717,
          55.867,
          -4.843,
          8.185,
          -22.022,
          0.197,
          -1.639,
          -13.966,
          -21.277,
          -20.19,
          -22.037,
          -5.577,
          -17.192,
          -18.771,
          2.305,
          -8.281,
          55.543,
          -6.436,
          -18.318,
          5.358,
          -7.363,
          11.76,
          -19.435,
          53.452,
          -5.982,
          7.239,
          -10.972,
          13.525,
          -37.759,
          12.626,
          52.629,
          18.856,
          27.929,
          -6.903,
          15.978,
          12.614,
          -21.999,
          29.976,
          -32.115,
          6.785,
          -54.476,
          -4.026,
          33.453,
          -25.758,
          -5.154,
          50.486,
          -15.117,
          -14.434,
          -29.082,
          -8.42,
          -12.5,
          -8.031,
          -25.856,
          -30.683,
          -21.89,
          41.117,
          -33.134,
          39.243,
          -24.133,
          -60.665,
          33.683,
          44.117,
          -15.86,
          -34.131,
          -5.599,
          -4.448,
          45.547,
          -21.702,
          0.151,
          -19.022,
          -24.753,
          49.037,
          5.121,
          -15.355,
          -9.094,
          4.554,
          -56.032,
          40.3353333,
          -6.075,
          -22.483,
          7.075,
          14.717,
          -16.62,
          12.059,
          -29.211,
          -5.771,
          16.84,
          28.826,
          45.324,
          -24.061,
          -6.518,
          18.219,
          14.52,
          -59.232,
          52.301,
          46.505,
          52.803,
          22.632,
          7.747,
          39.457,
          39.121,
          36.195,
          18.048,
          13.332,
          -7.481,
          -6.852,
          8.147,
          -4.439,
          -17.94,
          13.477,
          25.149,
          9.919,
          -26.802,
          7.191,
          34.2,
          42.142,
          -6.582,
          42.34,
          43.905,
          51.478,
          33.825,
          15.791,
          51.692,
          -2.839,
          -11.481,
          33.362,
          31.398,
          39.664,
          -31.028,
          22.282,
          33.386,
          -46.675,
          40.462,
          -26.535,
          36.372,
          29.384,
          -0.086,
          -33.207,
          36.19,
          23.901,
          -6.088,
          -58.893,
          -6.266,
          39.837,
          36.957,
          -19.247,
          -15.199,
          16.779,
          -20.69,
          13.402,
          -6.05,
          18.481,
          -14.464,
          17.3,
          15.324,
          39.57,
          45.772,
          -9.89,
          -9.844,
          -9.965,
          44.932,
          -12.41,
          5.167,
          1.795,
          -5.097,
          1.196,
          51.218,
          -9.593,
          55.959,
          56.724,
          -12.265,
          53.113,
          -16.696,
          44.244,
          17.813,
          -48.786,
          -4.883,
          -10.012,
          17.802,
          -24.388,
          -10.366,
          8.337,
          -22.122,
          15.125,
          9.685,
          45.533,
          43.3,
          -18.039,
          -3.184,
          3.752,
          43.233,
          -38.183,
          -7.104,
          19.333,
          38.19,
          16.01,
          1.598,
          -14.96,
          -28.117,
          22.789,
          15.679,
          11.742,
          42.851,
          -23.008,
          -5.799,
          -14.993,
          -12.584,
          -32.601,
          -24.894,
          -16.264,
          56.953,
          1.186,
          -8.48,
          12.982,
          -10.477,
          40.525,
          35.997,
          -6.59,
          6.262,
          -1.679,
          -12.525,
          58.679,
          44.663,
          0.729,
          51.564,
          -7.137,
          -5.524,
          6.405,
          -28.427,
          -33.135,
          18.19,
          51.52,
          -23.34,
          19.055,
          -4.817,
          -52.341,
          -13.841,
          -0.891,
          -11.164,
          43.773
         ],
         "legendgroup": "",
         "lon": [
          -74.07,
          131.782,
          95.34,
          163.377,
          98.711,
          -176.974,
          -61.377,
          102.285,
          -177.318,
          145.965,
          153.868,
          152.282,
          130.603,
          166.407,
          121.539,
          168.949,
          122.787,
          -21.549,
          122.58,
          147.734,
          102.198,
          166.499,
          149.123,
          63.773,
          63.472,
          98.71,
          96.318,
          -78.127,
          122.327,
          -172.264,
          -85.222,
          122.075,
          146.753,
          176.274,
          171.742,
          167.601,
          -98.358,
          160.513,
          165.931,
          20.228,
          -179.339,
          -78.103,
          62.054,
          -91.924,
          118.806,
          63.35,
          126.411,
          120.61,
          75.224,
          166.24,
          166.185,
          -102.973,
          -26.916,
          -70.701,
          -66.205,
          154.371,
          -70.568,
          152.779,
          133.667,
          -178.414,
          26.668,
          -70.776,
          95.901,
          126.48,
          43.673,
          122.957,
          -161.606,
          -176.218,
          -72.187,
          -125.856,
          -178.591,
          165.239,
          126.57,
          -66.543,
          70.868,
          166.927,
          158.647,
          169.789,
          127.733,
          169.361,
          -23.569,
          -126.3028333,
          142.175,
          -77.881,
          -42.254,
          120.45,
          102.543,
          -174.915,
          140.23,
          -2.668,
          143.416,
          166.557,
          121.974,
          -175.066,
          146.442,
          155.575,
          -73.431,
          140.091,
          139.918,
          -20.508,
          78.606,
          162.136,
          -141.593,
          122.096,
          161.284,
          59.726,
          57.794,
          -177.741,
          124.358,
          136.967,
          141.702,
          -83.123,
          161.287,
          151.577,
          -38.794,
          170.95,
          98.027,
          134.911,
          166.516,
          170.102,
          178.86,
          -178.925,
          130.791,
          -72.305,
          -172.415,
          126.76,
          -71.381,
          -156.835,
          146.383,
          168.063,
          31.848,
          120.363,
          121.899,
          169.132,
          169.871,
          -77.094,
          126.645,
          164.181,
          121.067,
          178.752,
          125.297,
          142.827,
          145.218,
          130.175,
          129.151,
          -98.07,
          125.154,
          -65.719,
          68.208,
          179.791,
          126.682,
          -64.499,
          -80.542,
          140.929,
          179.665,
          154.191,
          156.584,
          166.896,
          166.863,
          -175.954,
          154.034,
          -77.786,
          155.538,
          -175.406,
          -177.358,
          169.853,
          -124.253,
          -73.074,
          25.227,
          -175.864,
          -25.451,
          136.894,
          148.192,
          -173.643,
          -71.618,
          151.045,
          143.943,
          26.316,
          -176.616,
          -77.821,
          -69.991,
          -70.433,
          141.847,
          32.145,
          167.464,
          158.442,
          -77.442,
          -25.266,
          -124.2286667,
          147.572,
          -178.413,
          -76.862,
          -92.645,
          167.518,
          125.58,
          -177.589,
          154.347,
          -93.469,
          34.799,
          149.892,
          -177.036,
          154.999,
          -102.756,
          -92.653,
          158.902,
          151.613,
          141.199,
          159.199,
          122.269,
          -77.688,
          73.83,
          44.029,
          1.354,
          -102.084,
          -89.387,
          128.168,
          72.11,
          123.762,
          152.828,
          -172.225,
          124.616,
          95.127,
          -84.808,
          -63.349,
          126.762,
          -116.437,
          73.575,
          130.393,
          132.865,
          147.916,
          -176.847,
          59.809,
          121.63,
          -131.055,
          -77.322,
          166.339,
          140.827,
          100.581,
          118.401,
          -67.767,
          121.512,
          57.434,
          165.707,
          139.102,
          -70.563,
          70.738,
          138.935,
          122.517,
          -71.663,
          70.896,
          121.574,
          147.689,
          158.513,
          149.06,
          142.76,
          49.409,
          168.948,
          -173.529,
          -98.597,
          -178.31,
          120.275,
          152.932,
          -102.996,
          166.601,
          -62,
          -89.101,
          117.978,
          26.761,
          160.348,
          160.822,
          160.731,
          148.439,
          166.381,
          125.124,
          126.519,
          150.967,
          122.787,
          157.829,
          -79.587,
          163.269,
          -135.853,
          -77.795,
          173.497,
          -172.095,
          148.862,
          -101.276,
          164.357,
          153.581,
          160.469,
          -101.647,
          -70.161,
          160.819,
          126.729,
          175.163,
          147.596,
          -83.073,
          151.021,
          143.691,
          -178.413,
          139.722,
          124.221,
          145.785,
          -73.232,
          155.152,
          -155.0015,
          142.028,
          -96.591,
          -79.358,
          -173.085,
          -176.367,
          99.611,
          121.172,
          -87.34,
          139.197,
          169.9,
          154.178,
          -75.675,
          166.676,
          -71.076,
          -175.119,
          -172.467,
          -143.032,
          122.857,
          121.896,
          144.801,
          112.835,
          143.419,
          -17.649,
          155.054,
          124.023,
          136.04,
          165.916,
          -142.786,
          149.3,
          119.931,
          -177.632,
          122.589,
          153.85,
          126.64,
          -177.657,
          -71.871,
          -102.533,
          -174.776,
          -70.294,
          -104.205,
          153.172,
          160.568,
          -67.553,
          136.952,
          118.378,
          147.321
         ],
         "marker": {
          "color": [
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           8,
           8,
           8,
           8,
           8,
           8,
           8,
           8,
           8.1,
           8.2,
           8.2,
           8.2,
           8.3,
           8.3
          ],
          "coloraxis": "coloraxis",
          "size": [
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.1,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.2,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.3,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.4,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.5,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.6,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.7,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.8,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           7.9,
           8,
           8,
           8,
           8,
           8,
           8,
           8,
           8,
           8.1,
           8.2,
           8.2,
           8.2,
           8.3,
           8.3
          ],
          "sizemode": "area",
          "sizeref": 0.02075,
          "symbol": "star-triangle-down-open"
         },
         "mode": "markers",
         "name": "",
         "showlegend": false,
         "type": "scattergeo"
        }
       ],
       "layout": {
        "coloraxis": {
         "colorbar": {
          "title": {
           "text": "mag"
          }
         },
         "colorscale": [
          [
           0,
           "#0d0887"
          ],
          [
           0.1111111111111111,
           "#46039f"
          ],
          [
           0.2222222222222222,
           "#7201a8"
          ],
          [
           0.3333333333333333,
           "#9c179e"
          ],
          [
           0.4444444444444444,
           "#bd3786"
          ],
          [
           0.5555555555555556,
           "#d8576b"
          ],
          [
           0.6666666666666666,
           "#ed7953"
          ],
          [
           0.7777777777777778,
           "#fb9f3a"
          ],
          [
           0.8888888888888888,
           "#fdca26"
          ],
          [
           1,
           "#f0f921"
          ]
         ]
        },
        "geo": {
         "center": {},
         "domain": {
          "x": [
           0,
           1
          ],
          "y": [
           0,
           1
          ]
         }
        },
        "hoverlabel": {
         "font": {
          "size": 20
         }
        },
        "legend": {
         "itemsizing": "constant",
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        }
       }
      },
      "text/html": [
       "<div>                            <div id=\"af009a6e-69dd-4981-9a03-b429b53ab75f\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"af009a6e-69dd-4981-9a03-b429b53ab75f\")) {                    Plotly.newPlot(                        \"af009a6e-69dd-4981-9a03-b429b53ab75f\",                        [{\"geo\": \"geo\", \"hovertemplate\": \"<b>%{hovertext}</b><br><br>mag=%{marker.color}<br>latitude=%{lat}<br>longitude=%{lon}<extra></extra>\", \"hovertext\": [7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.1, 8.2, 8.2, 8.2, 8.3, 8.3], \"lat\": [-52.028, 32.053, 25.977, -11.154, 0.653, 51.409, -63.398, -4.33, 51.396, 63.952, -5.754, -5.116, -5.912, -13.248, 23.564, -20.122, 13.372, -60.823, 40.641, 43.024, -4.882, -12.519, 44.915, 40.311, 40.381, 24.531, 3.397, 7.409, 16.773, -17.098, 10.204, 23.247, 43.53, 51.744, -22.293, -17.26, 16.558, -51.225, -12.597, 38.026, -30.383, -4.843, 27.793, 14.066, -2.823, 40.32, 1.622, 15.344, 39.431, -14.043, -13.987, 18.404, -60.063, -24.495, -22.767, -7.288, -24.71, -6.526, -6.081, -30.523, 45.841, -10.97, 23.613, 8.87, 42.453, 1.156, 54.567, -20.252, -13.108, 41.679, -20.878, -11.122, 7.219, -22.671, 36.379, -45.277, 51.934, -20.23, 1.015, -20.553, -1.278, 40.4055, 40.246, -2.75, 10.797, 1.0, 24.185, 52.487, 27.236, -55.918, 41.415, -11.857, 23.107, -17.76, 43.318, -7.383, -38.453, -4.603, -4.517, -59.426, 42.839, -11.132, 60.642, 19.066, -10.615, 33.962, 30.013, -29.934, 13.752, 27.929, 36.194, 8.717, 55.867, -4.843, 8.185, -22.022, 0.197, -1.639, -13.966, -21.277, -20.19, -22.037, -5.577, -17.192, -18.771, 2.305, -8.281, 55.543, -6.436, -18.318, 5.358, -7.363, 11.76, -19.435, 53.452, -5.982, 7.239, -10.972, 13.525, -37.759, 12.626, 52.629, 18.856, 27.929, -6.903, 15.978, 12.614, -21.999, 29.976, -32.115, 6.785, -54.476, -4.026, 33.453, -25.758, -5.154, 50.486, -15.117, -14.434, -29.082, -8.42, -12.5, -8.031, -25.856, -30.683, -21.89, 41.117, -33.134, 39.243, -24.133, -60.665, 33.683, 44.117, -15.86, -34.131, -5.599, -4.448, 45.547, -21.702, 0.151, -19.022, -24.753, 49.037, 5.121, -15.355, -9.094, 4.554, -56.032, 40.3353333, -6.075, -22.483, 7.075, 14.717, -16.62, 12.059, -29.211, -5.771, 16.84, 28.826, 45.324, -24.061, -6.518, 18.219, 14.52, -59.232, 52.301, 46.505, 52.803, 22.632, 7.747, 39.457, 39.121, 36.195, 18.048, 13.332, -7.481, -6.852, 8.147, -4.439, -17.94, 13.477, 25.149, 9.919, -26.802, 7.191, 34.2, 42.142, -6.582, 42.34, 43.905, 51.478, 33.825, 15.791, 51.692, -2.839, -11.481, 33.362, 31.398, 39.664, -31.028, 22.282, 33.386, -46.675, 40.462, -26.535, 36.372, 29.384, -0.086, -33.207, 36.19, 23.901, -6.088, -58.893, -6.266, 39.837, 36.957, -19.247, -15.199, 16.779, -20.69, 13.402, -6.05, 18.481, -14.464, 17.3, 15.324, 39.57, 45.772, -9.89, -9.844, -9.965, 44.932, -12.41, 5.167, 1.795, -5.097, 1.196, 51.218, -9.593, 55.959, 56.724, -12.265, 53.113, -16.696, 44.244, 17.813, -48.786, -4.883, -10.012, 17.802, -24.388, -10.366, 8.337, -22.122, 15.125, 9.685, 45.533, 43.3, -18.039, -3.184, 3.752, 43.233, -38.183, -7.104, 19.333, 38.19, 16.01, 1.598, -14.96, -28.117, 22.789, 15.679, 11.742, 42.851, -23.008, -5.799, -14.993, -12.584, -32.601, -24.894, -16.264, 56.953, 1.186, -8.48, 12.982, -10.477, 40.525, 35.997, -6.59, 6.262, -1.679, -12.525, 58.679, 44.663, 0.729, 51.564, -7.137, -5.524, 6.405, -28.427, -33.135, 18.19, 51.52, -23.34, 19.055, -4.817, -52.341, -13.841, -0.891, -11.164, 43.773], \"legendgroup\": \"\", \"lon\": [-74.07, 131.782, 95.34, 163.377, 98.711, -176.974, -61.377, 102.285, -177.318, 145.965, 153.868, 152.282, 130.603, 166.407, 121.539, 168.949, 122.787, -21.549, 122.58, 147.734, 102.198, 166.499, 149.123, 63.773, 63.472, 98.71, 96.318, -78.127, 122.327, -172.264, -85.222, 122.075, 146.753, 176.274, 171.742, 167.601, -98.358, 160.513, 165.931, 20.228, -179.339, -78.103, 62.054, -91.924, 118.806, 63.35, 126.411, 120.61, 75.224, 166.24, 166.185, -102.973, -26.916, -70.701, -66.205, 154.371, -70.568, 152.779, 133.667, -178.414, 26.668, -70.776, 95.901, 126.48, 43.673, 122.957, -161.606, -176.218, -72.187, -125.856, -178.591, 165.239, 126.57, -66.543, 70.868, 166.927, 158.647, 169.789, 127.733, 169.361, -23.569, -126.3028333, 142.175, -77.881, -42.254, 120.45, 102.543, -174.915, 140.23, -2.668, 143.416, 166.557, 121.974, -175.066, 146.442, 155.575, -73.431, 140.091, 139.918, -20.508, 78.606, 162.136, -141.593, 122.096, 161.284, 59.726, 57.794, -177.741, 124.358, 136.967, 141.702, -83.123, 161.287, 151.577, -38.794, 170.95, 98.027, 134.911, 166.516, 170.102, 178.86, -178.925, 130.791, -72.305, -172.415, 126.76, -71.381, -156.835, 146.383, 168.063, 31.848, 120.363, 121.899, 169.132, 169.871, -77.094, 126.645, 164.181, 121.067, 178.752, 125.297, 142.827, 145.218, 130.175, 129.151, -98.07, 125.154, -65.719, 68.208, 179.791, 126.682, -64.499, -80.542, 140.929, 179.665, 154.191, 156.584, 166.896, 166.863, -175.954, 154.034, -77.786, 155.538, -175.406, -177.358, 169.853, -124.253, -73.074, 25.227, -175.864, -25.451, 136.894, 148.192, -173.643, -71.618, 151.045, 143.943, 26.316, -176.616, -77.821, -69.991, -70.433, 141.847, 32.145, 167.464, 158.442, -77.442, -25.266, -124.2286667, 147.572, -178.413, -76.862, -92.645, 167.518, 125.58, -177.589, 154.347, -93.469, 34.799, 149.892, -177.036, 154.999, -102.756, -92.653, 158.902, 151.613, 141.199, 159.199, 122.269, -77.688, 73.83, 44.029, 1.354, -102.084, -89.387, 128.168, 72.11, 123.762, 152.828, -172.225, 124.616, 95.127, -84.808, -63.349, 126.762, -116.437, 73.575, 130.393, 132.865, 147.916, -176.847, 59.809, 121.63, -131.055, -77.322, 166.339, 140.827, 100.581, 118.401, -67.767, 121.512, 57.434, 165.707, 139.102, -70.563, 70.738, 138.935, 122.517, -71.663, 70.896, 121.574, 147.689, 158.513, 149.06, 142.76, 49.409, 168.948, -173.529, -98.597, -178.31, 120.275, 152.932, -102.996, 166.601, -62.0, -89.101, 117.978, 26.761, 160.348, 160.822, 160.731, 148.439, 166.381, 125.124, 126.519, 150.967, 122.787, 157.829, -79.587, 163.269, -135.853, -77.795, 173.497, -172.095, 148.862, -101.276, 164.357, 153.581, 160.469, -101.647, -70.161, 160.819, 126.729, 175.163, 147.596, -83.073, 151.021, 143.691, -178.413, 139.722, 124.221, 145.785, -73.232, 155.152, -155.0015, 142.028, -96.591, -79.358, -173.085, -176.367, 99.611, 121.172, -87.34, 139.197, 169.9, 154.178, -75.675, 166.676, -71.076, -175.119, -172.467, -143.032, 122.857, 121.896, 144.801, 112.835, 143.419, -17.649, 155.054, 124.023, 136.04, 165.916, -142.786, 149.3, 119.931, -177.632, 122.589, 153.85, 126.64, -177.657, -71.871, -102.533, -174.776, -70.294, -104.205, 153.172, 160.568, -67.553, 136.952, 118.378, 147.321], \"marker\": {\"color\": [7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.1, 8.2, 8.2, 8.2, 8.3, 8.3], \"coloraxis\": \"coloraxis\", \"size\": [7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.1, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.3, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.7, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.8, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 7.9, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.1, 8.2, 8.2, 8.2, 8.3, 8.3], \"sizemode\": \"area\", \"sizeref\": 0.02075, \"symbol\": \"star-triangle-down-open\"}, \"mode\": \"markers\", \"name\": \"\", \"showlegend\": false, \"type\": \"scattergeo\"}],                        {\"coloraxis\": {\"colorbar\": {\"title\": {\"text\": \"mag\"}}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"geo\": {\"center\": {}, \"domain\": {\"x\": [0.0, 1.0], \"y\": [0.0, 1.0]}}, \"hoverlabel\": {\"font\": {\"size\": 20}}, \"legend\": {\"itemsizing\": \"constant\", \"tracegroupgap\": 0}, \"margin\": {\"t\": 60}, \"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"pie\": [{\"automargin\": true, \"type\": \"pie\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"autotypenumbers\": \"strict\", \"coloraxis\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('af009a6e-69dd-4981-9a03-b429b53ab75f');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "mag_fig.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
