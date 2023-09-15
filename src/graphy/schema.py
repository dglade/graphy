from graphene import ObjectType, String, Int, Float, Date, Time, DateTime, Boolean, List, Field, Schema

from .model import get_positions, get_trip_updates

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


class Trip(ObjectType):
    trip_id = String()
    route_id = String()
    # direction_id = 
    start_time = String()
    start_date = String()
    schedule_relationship = Int()

class TripUpdate(ObjectType):
    trip = Field(Trip)
    vehicle = Field(VehicleDetail)


class Query(ObjectType):
    all_vehicles = List(Vehicle)
    all_trip_updates = List(TripUpdate)

    def resolve_all_vehicles(parent, info):
        all_positions = get_positions()
        return [position['vehicle'] for position in all_positions]

    def resolve_all_trip_updates(parent, info):
        all_trip_updates = get_trip_updates()
        return [{'trip': trip_update['trip_update']['trip'], 'vehicle': trip_update['trip_update']['vehicle']} for trip_update in all_trip_updates]

schema = Schema(query=Query)


# {'id': '1', 'is_deleted': False, 'trip_update': {'trip': {'trip_id': 'MD-W_MW2254_V2_C', 'route_id': 'MD-W', 'direction_id': None, 'start_time': '21:22:00', 'start_date': '20230913', 'schedule_relationship': 0}, 'vehicle': {'id': '8587', 'label': '2254', 'license_plate': None}, 'stop_time_update': [{'stop_sequence': 6, 'stop_id': 'HANOVERP', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T02:41:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T02:41:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}, {'stop_sequence': 7, 'stop_id': 'SCHAUM', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T02:45:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T02:45:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}, {'stop_sequence': 8, 'stop_id': 'ROSELLE', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T02:50:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T02:50:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}, {'stop_sequence': 9, 'stop_id': 'MEDINAH', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T02:52:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T02:52:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}, {'stop_sequence': 10, 'stop_id': 'ITASCA', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T02:56:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T02:56:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}, {'stop_sequence': 11, 'stop_id': 'WOODDALE', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T03:00:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T03:00:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}, {'stop_sequence': 12, 'stop_id': 'BENSENVIL', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T03:04:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T03:04:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}, {'stop_sequence': 15, 'stop_id': 'FRANKLIN', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T03:11:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T03:11:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}, {'stop_sequence': 17, 'stop_id': 'RIVERGROVE', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T03:14:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T03:14:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}, {'stop_sequence': 18, 'stop_id': 'ELMWOODPK', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T03:17:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T03:17:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}, {'stop_sequence': 19, 'stop_id': 'MONTCLARE', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T03:19:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T03:19:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}, {'stop_sequence': 21, 'stop_id': 'GALEWOOD', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T03:21:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T03:21:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}, {'stop_sequence': 25, 'stop_id': 'WESTERNAVE', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T03:32:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T03:32:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}, {'stop_sequence': 28, 'stop_id': 'CUS', 'arrival': {'delay': 0, 'time': {'low': '2023-09-14T03:45:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'departure': {'delay': 0, 'time': {'low': '2023-09-14T03:45:54.000Z', 'high': 0, 'unsigned': False}, 'uncertainty': 0}, 'schedule_relationship': 0}], 'timestamp': {'low': '2023-09-14T02:39:15.000Z', 'high': 0, 'unsigned': True}, 'delay': None, 'position': {'id': '106', 'is_deleted': False, 'trip_update': None, 'vehicle': {'trip': {'trip_id': 'MD-W_MW2254_V2_C', 'route_id': 'MD-W', 'direction_id': None, 'start_time': '21:22:00', 'start_date': '20230913', 'schedule_relationship': 0}, 'vehicle': {'id': '8587', 'label': '2254', 'license_plate': None}, 'position': {'latitude': 41.99205017089844, 'longitude': -88.18218994140625, 'bearing': 99, 'odometer': None, 'speed': None}, 'current_stop_sequence': None, 'stop_id': None, 'current_status': 2, 'timestamp': {'low': '2023-09-14T02:38:52.000Z', 'high': 0, 'unsigned': True}, 'congestion_level': None, 'occupancy_status': None}, 'alert': None}}, 'vehicle': None, 'alert': None}
 