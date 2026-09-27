 #module3.py

def payment(total):
    print("\n Payment Details")
    print("Total amount Tickets :", total)

    print("1. Cash Payment")
    print("2. Online payment (UPI)")
    print("3. Card Payment")

    choice = int(input("Select payment method:"))

    if choice == 1:
        method = "Cash Payment."
    elif choice == 2:
        method = "Online payment (UPI)."
    elif choice == 3:
        method = "Card Payment."
    else:
        method = "Unknown Payment Method."

    if method != "Unknown Payment Method.":
        print("Payment successful." )
        return method
    else:
        print("Invalid payment method.")
        return method


def show_ticket(name, phone, ticket, number, total, method):
    print("\n===========================")
    print("       TICKET CONFIRMATION")
    print("=============================")
    print("Name:", name)
    print("Phone:", phone)
    print("Ticket Type:", ticket)
    print("Number of Tickets:", number)
    print("Total Amount Tickets :", total)
    print("Payment Method:", method)
    print("Status of Tickets: Confirmed")
    print("=============================")
