from datetime import timedelta
import threading
import random
import time

from parking_lot import parking_lot, ParkingLot
from parking_types import SpotType
from vehicle import Bike, Car, Truck
from fees import SpotBasedFeeStrategy, VehicleBasedFeeStrategy


def setup_parking_lot():
    parking_lot.levels.clear()

    # Ground Floor
    ground_level = parking_lot.add_level()

    ground_level.add_spot(SpotType.SMALL)
    ground_level.add_spot(SpotType.SMALL)

    ground_level.add_spot(SpotType.MEDIUM)
    ground_level.add_spot(SpotType.MEDIUM)
    ground_level.add_spot(SpotType.MEDIUM)
    ground_level.add_spot(SpotType.MEDIUM)

    # First Floor
    first_level = parking_lot.add_level()

    first_level.add_spot(SpotType.LARGE)
    first_level.add_spot(SpotType.LARGE)
    first_level.add_spot(SpotType.LARGE)

    return parking_lot


def scenario_1_normal_flow(parking_lot: ParkingLot):
    print("\n" + "=" * 50)
    print("SCENARIO 1: NORMAL PARK / UNPARK")
    print("=" * 50)

    bike = Bike("BIKE123")

    ticket = parking_lot.park_vehicle(bike)

    if ticket:
        parking_lot.unpark_vehicle(ticket)


def scenario_2_parking_lot_full(parking_lot: ParkingLot):
    print("\n" + "=" * 50)
    print("SCENARIO 2: SMALL SPOTS FULL")
    print("=" * 50)

    bike1 = Bike("B1")
    bike2 = Bike("B2")
    bike3 = Bike("B3")

    parking_lot.park_vehicle(bike1)
    parking_lot.park_vehicle(bike2)

    ticket = parking_lot.park_vehicle(bike3)

    if ticket is None:
        print("Expected: No small spot available.")


def scenario_3_double_unpark(parking_lot: ParkingLot):
    print("\n" + "=" * 50)
    print("SCENARIO 3: DOUBLE UNPARK")
    print("=" * 50)

    car = Car("CAR123")

    ticket = parking_lot.park_vehicle(car)

    if ticket:
        parking_lot.unpark_vehicle(ticket)

        print("\nAttempting second unpark...\n")

        parking_lot.unpark_vehicle(ticket)


def scenario_4_fee_before_exit(parking_lot: ParkingLot):
    print("\n" + "=" * 50)
    print("SCENARIO 4: CALCULATE FEE BEFORE EXIT")
    print("=" * 50)

    car = Car("CAR456")

    ticket = parking_lot.park_vehicle(car)

    if ticket:
        try:
            fee = parking_lot.fee_manager.calculate_fees(ticket)
            print(f"Fee: {fee}")

        except Exception as e:
            print(f"Expected Error: {e}")


def scenario_5_truck_overflow(parking_lot: ParkingLot):
    print("\n" + "=" * 50)
    print("SCENARIO 5: LARGE SPOTS FULL")
    print("=" * 50)

    truck1 = Truck("T1")
    truck2 = Truck("T2")
    truck3 = Truck("T3")
    truck4 = Truck("T4")

    parking_lot.park_vehicle(truck1)
    parking_lot.park_vehicle(truck2)
    parking_lot.park_vehicle(truck3)

    ticket = parking_lot.park_vehicle(truck4)

    if ticket is None:
        print("Expected: No large spot available.")


def scenario_6_strategy_pattern(parking_lot: ParkingLot):
    print("\n" + "=" * 50)
    print("SCENARIO 6: STRATEGY SWITCHING")
    print("=" * 50)

    car = Car("STRATEGY_CAR")

    ticket = parking_lot.park_vehicle(car)

    if ticket:
        ticket.entry_at -= timedelta(hours=3)
        ticket.mark_exit()

        parking_lot.fee_manager.set_strategy(
            SpotBasedFeeStrategy()
        )

        spot_fee = parking_lot.fee_manager.calculate_fees(ticket)

        parking_lot.fee_manager.set_strategy(
            VehicleBasedFeeStrategy()
        )

        vehicle_fee = parking_lot.fee_manager.calculate_fees(ticket)

        print(f"Spot Based Fee    : {spot_fee}")
        print(f"Vehicle Based Fee : {vehicle_fee}")


def scenario_7_concurrent_parking(parking_lot: ParkingLot):
    print("\n" + "=" * 50)
    print("SCENARIO 7: CONCURRENT PARKING")
    print("=" * 50)

    tickets = []
    tickets_lock = threading.Lock()

    def worker(vehicle):
        ticket = parking_lot.park_vehicle(vehicle)

        if ticket:
            with tickets_lock:
                tickets.append(ticket)

    vehicles = (
        [Bike(f"B{i}") for i in range(5)] +
        [Car(f"C{i}") for i in range(5)] +
        [Truck(f"T{i}") for i in range(5)]
    )

    threads = []

    for vehicle in vehicles:
        thread = threading.Thread(
            target=worker,
            args=(vehicle,)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"\nSuccessfully parked: {len(tickets)}")


def scenario_8_long_duration_billing(parking_lot: ParkingLot):
    print("\n" + "=" * 50)
    print("SCENARIO 8: LONG DURATION BILLING")
    print("=" * 50)

    car = Car("LONGTRIP")

    ticket = parking_lot.park_vehicle(car)

    if ticket:
        ticket.entry_at -= timedelta(hours=5, minutes=20)

        parking_lot.unpark_vehicle(ticket)


def scenario_9_remove_levels(parking_lot: ParkingLot):
    print("\n" + "=" * 50)
    print("SCENARIO 9: REMOVE LEVELS")
    print("=" * 50)

    parking_lot.remove_level()
    parking_lot.remove_level()
    parking_lot.remove_level()
    parking_lot.remove_level()


def scenario_10_mixed_traffic(parking_lot: ParkingLot):
    print("\n" + "=" * 50)
    print("SCENARIO 10: MIXED TRAFFIC")
    print("=" * 50)

    vehicles = [
        Bike("B1"),
        Bike("B2"),
        Car("C1"),
        Car("C2"),
        Truck("T1"),
        Truck("T2"),
    ]

    tickets = []

    for vehicle in vehicles:
        ticket = parking_lot.park_vehicle(vehicle)

        if ticket:
            tickets.append(ticket)

    print(f"\nTotal Parked Vehicles: {len(tickets)}")

    for ticket in tickets:
        parking_lot.unpark_vehicle(ticket)


def scenario_11_concurrent_park_unpark(parking_lot: ParkingLot):
    print("\n" + "=" * 50)
    print("SCENARIO 11: CONCURRENT PARK + UNPARK")
    print("=" * 50)

    parked_tickets = []
    tickets_lock = threading.Lock()

    def park_worker(vehicle):
        ticket = parking_lot.park_vehicle(vehicle)

        if ticket:
            with tickets_lock:
                parked_tickets.append(ticket)

    vehicles = (
        [Bike(f"B{i}") for i in range(2)] +
        [Car(f"C{i}") for i in range(4)] +
        [Truck(f"T{i}") for i in range(2)]
    )

    park_threads = []

    for vehicle in vehicles:
        t = threading.Thread(
            target=park_worker,
            args=(vehicle,)
        )

        park_threads.append(t)
        t.start()

    for t in park_threads:
        t.join()

    print(f"\nInitially parked: {len(parked_tickets)}")

    def unpark_worker(ticket):
        time.sleep(random.uniform(0.1, 1.0))
        parking_lot.unpark_vehicle(ticket)

    unpark_threads = []

    for ticket in parked_tickets:
        t = threading.Thread(
            target=unpark_worker,
            args=(ticket,)
        )

        unpark_threads.append(t)
        t.start()

    for t in unpark_threads:
        t.join()

    print("\nAll vehicles unparked.")


if __name__ == "__main__":

    scenario_1_normal_flow(setup_parking_lot())

    scenario_2_parking_lot_full(setup_parking_lot())

    scenario_3_double_unpark(setup_parking_lot())

    scenario_4_fee_before_exit(setup_parking_lot())

    scenario_5_truck_overflow(setup_parking_lot())

    scenario_6_strategy_pattern(setup_parking_lot())

    scenario_7_concurrent_parking(setup_parking_lot())

    scenario_8_long_duration_billing(setup_parking_lot())

    scenario_9_remove_levels(setup_parking_lot())

    scenario_10_mixed_traffic(setup_parking_lot())

    scenario_11_concurrent_park_unpark(setup_parking_lot())