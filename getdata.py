import osmnx as ox
from pathlib import Path
from xml.dom import minidom
import shutil

place = "San Francisco, CA, USA"
# place = "Boston, MA, USA"
# place = "New York, NY, USA"
# place = "Minneapolis, MN, USA"
# place = "Saint Paul, MN, USA"

datapath = f"data/{place}.graphml"
checkExists = Path(datapath)

# if(not checkExists.exists()):
if True:

    # multiGraph = ox.graph.graph_from_place("Minneapolis, MN, USA")
    # multiGraph = ox.graph.graph_from_bbox(45.4013, 44.5396, -92.0915, -94.2256)

    # if city == "Minneapolis":
    #     [north, south, east, west] = [45.0835, 44.8941, -93.1864, -93.3481]

    # if city == "Saint Paul":
    #     [north, south, east, west] = [45.1452, 44.7500, -92.8276, -93.1819]

    # cf = None
    cf = '["highway"~"motorway|' \
        'motorway_link|primary|secondary|tertiary' \
        '"]'
    # cf = '["highway"~"motorway"]'
    # print(cf)

    # multiGraph = ox.graph.graph_from_bbox(north, south, east, west,
    #     network_type="drive",
    #     custom_filter=cf)
    
    multiGraph = ox.graph.graph_from_place(place,
        network_type="drive",
        custom_filter=cf)

    ox.save_graphml(multiGraph, datapath)

shutil.copy(datapath, "data/map.graphml")

G = ox.load_graphml("data/map.graphml")
fig, ax = ox.plot_graph(G)