import folium
import pandas as pd

# Create map object
m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

# Load data
data = pd.DataFrame({
    'Latitude': [45.52, 45.52, 45.53], 
    'Longitude': [-122.68, -122.69, -122.68],
    'Location': ['Store 1', 'Store 2', 'Store 3']
})

# Add markers to map
for _, row in data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Location']).add_to(m)

# Save map
m.save('map.html')