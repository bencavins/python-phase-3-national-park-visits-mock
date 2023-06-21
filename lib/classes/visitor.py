class Visitor:

    def __init__(self, name):
        self.name = name
        self.trips = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception('invalid name')
    
    def get_parks(self):
        result = []
        for trip in self.trips:
            if trip.park not in result: # <- this will make the parks unique (not required)
                result.add(trip.park)
        return result
        # return [trip.park for trip in self.trips]
    
    def create_trip(self, park, start, end):
        from classes.trip import Trip
        return Trip(park, start, end, visitor=self)
    
    def __repr__(self) -> str:
        return f"<Visitor {self.name}>"