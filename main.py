import flightradar24
import json
# import pandas as pd

flight_id = 'HD12' 
fr = flightradar24.Api()
flight = fr.get_flight(flight_id)

print(json.dumps(flight, indent=2))
