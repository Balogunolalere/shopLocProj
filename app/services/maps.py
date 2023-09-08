import folium
from app.models.shop import Shop
from app.database import crud


def generate_map(shops: list[Shop]):

  map = folium.Map(location=[6.6018, 3.3515], zoom_start=13)

  shops = [shop for shop in crud.get_shops()]

  for shop in shops:
    folium.Marker(
      [shop['latitude'], shop['longitude']],
      popup=shop['name'],  
      icon=folium.Icon(color='blue', icon='store')
    ).add_to(map)

  return map._repr_html_()

def generate_map_page(map_html):
  page = f"""
  <html>
    <head>
      <title>Shops Map</title> 
    </head>
    <body>
      {map_html}
    </body>
  </html>
  """
  return page