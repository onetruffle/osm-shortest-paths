import osmnx as ox
from pathlib import Path
from xml.dom import minidom

datapath = "data/map.graphml"
checkExists = Path(datapath)
if(not checkExists.exists()):
    multiGraph = ox.graph.graph_from_place("Minneapolis, MN, USA")
    # multiGraph = ox.graph.graph_from_bbox(45.4013, 44.5396, -92.0915, -94.2256)
    ox.save_graphml(multiGraph, datapath)