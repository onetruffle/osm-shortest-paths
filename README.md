# osm-shortest-paths

Install the following python modules.
1. osmnx
2. flask
3. flask-cors

Either specify the location or the bounding box in `getdata.py`, then run it.
Also change the bounding box boundaries and center in `osmmap.html` accordingly.

Run `flaskAPI.py`, then open `osmmap.html` in a web browser.

Inside the bounding box: \
1st click - source \
2nd click - destination \
3rd click - anywhere (to get the shortest path)