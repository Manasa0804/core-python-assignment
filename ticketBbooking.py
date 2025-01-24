def manage_seats(total_seats, booked_seats, book_seat=None, cancel_seat=None):
    if book_seat and book_seat not in booked_seats:
        booked_seats.append(book_seat)
    elif book_seat in booked_seats:
        print(f"Seat {book_seat} is already booked.")

    if cancel_seat and cancel_seat in booked_seats:
        booked_seats.remove(cancel_seat)
    elif cancel_seat and cancel_seat not in booked_seats:
        print(f"Seat {cancel_seat} is not booked.")

    a = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
    return a


total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5

available_seats = manage_seats(total_seats, booked_seats, book_seat, cancel_seat)
print(f"Available seats: {available_seats}")