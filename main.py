import flightradar24
flight_id = 'TK1' # Turkish Airlines' Istanbul - New York flight
fr = flightradar24.Api()
flight = fr.get_flight(flight_id)
