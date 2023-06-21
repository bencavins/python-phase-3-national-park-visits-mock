from classes.national_park import NationalPark

class Trip:
    def __init__(self, visitor, park, start_date, end_date):
        # make visitor/park accesible from Trip obj
        self.visitor = visitor
        self.park = park
        self.start_date = start_date
        self.end_date = end_date

        # make Trip obj accesible from visitor/park objs
        self.visitor.trips.append(self)
        self.park.trips.append(self)
    
    @property
    def park(self):
        return self._park
    
    @park.setter
    def park(self, new_park):
        if isinstance(new_park, NationalPark):
            self._park = new_park
        else:
            raise Exception('invalid park')

    
    def __repr__(self) -> str:
        return f'<Trip {self.park.name} {self.visitor.name}>'
