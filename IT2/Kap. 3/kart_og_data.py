#import osmnx as ox
import folium as fol
# Byenes koordinater
punkter = [
  [59.9139, 10.7522],  # Oslo
  [55.6761, 12.5683],  # København
  [59.3293, 18.0686]   # Stockholm
]
# Beregner snittet av lengdegrader og breddegrader for å finne 
# et punkt midt mellom alle byene.
lengde_sum = 0
bredde_sum = 0
for punkt in punkter:
  lengde_sum += punkt[0]
  bredde_sum += punkt[1]
lengde_snitt = lengde_sum / len(punkter)
bredde_snitt = bredde_sum / len(punkter)
# Lager et kart
m = fol.Map([lengde_snitt, bredde_snitt], zoom_start=6)
# Legger til byene
for punkt in punkter:
  fol.CircleMarker(punkt).add_to(m)
# Lagrer kartet
m.save("skandinavia.html")