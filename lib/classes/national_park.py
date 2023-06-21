class NationalPark:
    def __init__(self, name):
        self.name = name
        self.trips = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    def get_visitors(self):
        result = []
        for trip in self.trips:
            result.append(trip.visitor)
        return result

    def total_visits(self):
        return len(self.trips)
    
    def best_visitor(self):
        results = {}
        for trip in self.trips:
            # if trip.visitor.name not in results:
            #     results[trip.visitor.name] = 1
            # else:
            #     results[trip.visitor.name] += 1
            results[trip.visitor.name] = results.get(trip.visitor.name, 0) + 1
            # results.setdefault(trip.visitor.name, results.get(trip.visitor.name, 0) + 1)
        return results
    
    def __repr__(self) -> str:
        return f"<Park {self.name}>"
