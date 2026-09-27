# main.py

from module1 import get_booking
from module2 import ticket_details
from module3 import payment, show_ticket

print("****************************")
print(" TICKET BOOKING SYSTEM ")
print("****************************")

name, phone, ticket, number = get_booking()

if ticket != "None":

    price, available, total, status = ticket_details(ticket, number)

    if status:
        print("\nTicket price:", price)
        print("Available tickets:", available)
        print("Total amount:", total)

        method = payment(total)

        if method != "Unknown":
            show_ticket(name, phone, ticket, number, total, method)

    else:
        print("\nSorry, tickets are not available.")
        print("Available tickets:", available)

else:
    print("\nBooking cancelled.")
