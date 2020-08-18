import folium

map = folium.Map(location=[39.59, 66.97])

map.add_child(folium.Marker(location=[39.5, 66.9], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(folium.LayerControl())

map.save("Map1.html")
