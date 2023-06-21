#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    park1 = NationalPark('yellostone')
    park2 = NationalPark('tetons')

    visitor1 = Visitor('joe')
    visitor2 = Visitor('jane')

    trip1 = Trip(visitor1, park1, '01/01/23', '01/07/23')

    ipdb.set_trace()
