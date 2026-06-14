from datetime import datetime, timedelta

from movie_booking_system import system
from movie import Movie
from seat import SeatType


def main():

    # Add cities
    system.add_city("Delhi")
    system.add_city("Mumbai")

    # Get city
    delhi = system.get_city("Delhi")

    # Add theatres
    delhi.add_theatre("CP")
    delhi.add_theatre("Dwarka")

    # Get theatres
    cp_theatre = delhi.list_theatres()[0]

    # Add screens
    cp_theatre.add_screen()
    cp_theatre.add_screen()

    # Get screen
    screen1 = cp_theatre.list_screens()[0]

    # Create movies
    interstellar = Movie(
        "Interstellar",
        timedelta(hours=2, minutes=49),
        "Sci-Fi"
    )

    oppenheimer = Movie(
        "Oppenheimer",
        timedelta(hours=3),
        "Drama"
    )

    # Add shows
    screen1.add_show(
        interstellar,
        datetime(2026, 6, 14, 18, 0)
    )

    screen1.add_show(
        oppenheimer,
        datetime(2026, 6, 14, 21, 30)
    )

    # Get show
    interstellar_show = screen1.list_shows()[0]

    # Add seats
    for _ in range(5):
        interstellar_show.add_seat(SeatType.REGULAR)

    for _ in range(3):
        interstellar_show.add_seat(SeatType.PREMIUM)

    print("\n========== SEARCH SHOWS ==========")

    shows = system.search_shows(
        city="Delhi",
        movie_name="Interstellar"
    )

    for show in shows:
        print(
            f"Show ID: {show.id}, "
            f"Movie: {show.movie.name}, "
            f"Start Time: {show.start_time}, "
            f"End Time: {show.end_time}"
        )

    selected_show = shows[0]

    print("\n========== AVAILABLE SEATS ==========")

    available_seats = system.find_seats(selected_show)

    for seat in available_seats:
        print(
            f"Seat Number: {seat.id}, "
            f"Type: {seat.type.name}"
        )

    print("\n========== BOOKING SEATS ==========")

    booked_seats = system.book_seats(
        selected_show,
        [1, 2, 6]
    )

    for seat in booked_seats:
        print(
            f"Booked Seat: {seat.id}, "
            f"Type: {seat.type.name}"
        )

    print("\n========== AVAILABLE SEATS AFTER BOOKING ==========")

    available_seats = system.find_seats(selected_show)

    for seat in available_seats:
        print(
            f"Seat Number: {seat.id}, "
            f"Type: {seat.type.name}"
        )


if __name__ == "__main__":
    main()