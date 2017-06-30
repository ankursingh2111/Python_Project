import folium, pandas

map=folium.Map(location=[38.18,-99.09],zoom_start=6, tiles="Mapbox Bright")
fg=folium.FeatureGroup(name="My Map")
dfw=pandas.read_csv("Volcanoes.txt")
lat=list(dfw["LAT"])
lon=list(dfw["LON"])
elev=list(dfw["ELEV"])

def colorcoding(ele):
    if ele<1000:
        return "green"
    elif 100<=ele<2000:
        return "orange"
    else:
        return "red"

for la, lo, el in zip(lat,lon,elev):
    #fg.add_child(folium.Marker(location=[la,lo], popup=str(el)+" m", icon=folium.Icon(color=colorcoding(el))))
    fg.add_child(folium.CircleMarker(location=[la,lo], radius=4, popup=str(el)+" m",color=colorcoding(el)))
fg.add_child(folium.GeoJson(data=open("world.json","r", encoding="utf-8-sig"), style_function=lambda x:{'fillColor':"yellow" if x['properties']['POP2005']<1000000
else "orange" if 1000000<=x['properties']['POP2005']<2000000 else "red"}))
map.add_child(fg)
map.save("Map1.html")
