import pandas
import folium

volcano = pandas.read_csv("Volcanoes.txt")

map = folium.Map(location = (40,-120), zoom_start = 6)
vol = folium.FeatureGroup(name = "Volcano")
pop = folium.FeatureGroup(name = "Population")
def color(el):
    if el < 2000:
        return "green"
    elif el < 3000:
        return "orange"
    elif el < 4000:
        return "red"
    else:
        return "purple"

lat = list(volcano['LAT'])
lon = list(volcano["LON"])
elev = list(volcano["ELEV"])

for i,j,k in zip(lat,lon,elev):
        vol.add_child(folium.CircleMarker(location = (i,j),popup = "Elevation: " + str(k) +" Feet", 
        radius = 6,fill_color = color(int(k)), color = 'grey', fill_opacity = 0.8, weight = 2))

pop.add_child(folium.GeoJson(data = open("world.json", 'r', encoding= 'utf-8-sig').read()
, style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 
 else 'orange' if x['properties']['POP2005'] < 50000000 else 'red'} ))


map.add_child(vol)
map.add_child(pop)

map.add_child(folium.LayerControl(position = 'topright', hideSingleBase = True))

map.save("Map2.html")
