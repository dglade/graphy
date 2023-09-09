from graphene import ObjectType, String, Int, Float, Date, Time, DateTime, Boolean, List, Field, Schema

from .model import get_positions

class VehicleDetail(ObjectType):
    id = String()
    label = String()
    license_place = String()


class Position(ObjectType):
    bearing = Int()
    latitude = Float()
    longitude = Float()
    odometer = Float()
    speed = Int()


class Trip(ObjectType):
    direction_id = String()
    route_id = String()
    schedule_relationship = Int()
    start_date = Date()
    start_time = Time()
    trip_id = String()


class TimeStamp(ObjectType):
    high = Int()
    low = DateTime()
    unsigned = Boolean()

class Vehicle(ObjectType):
    congestion_level = String()
    current_status = Int()
    current_stop_sequence = String()
    occupancy_status = String()
    position = Field(Position)
    stop_id = Int()
    timestamp = Field(TimeStamp)
    trip = Field(Trip)
    vehicle_detail = Field(VehicleDetail)

        
class Query(ObjectType):
    all_vehicles = List(Vehicle)

    def resolve_all_vehicles(parent, info):
        # We can easily optimize query count in the resolve method
        all_positions = get_positions()
        return [position['vehicle'] for position in all_positions]

schema = Schema(query=Query)


