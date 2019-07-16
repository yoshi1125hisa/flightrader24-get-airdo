import flightradar24

flight_id = 'HD12' 
fr = flightradar24.Api()
flight = fr.get_flight(flight_id)

print(fr)
print(flight)
