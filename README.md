# Ticket Booking System

A simple **Ticket Booking System of Pyhton Program.**. This is the application that allows the users to view the available their 'tickets of trains,buses,movies,','booking of tickets', 'view of bookings', and 'cancelation of booking tickets bookings'.

## Features

- View  available tickets
- You can book one or more tickets
- Enter customer name and phone number manadatory
- Automatically calculate the total price
- Generate a unique booking ID
- View all active bookings
- You can Cancel bookings
- Restore ticket availability after cancellation
- Simple menu-driven interface

## Ticket Types

| Ticket Type | Price |
|---|---:|
| Movie Ticket | ₹180 |
| Bus Ticket | ₹150 |
| Train Ticket | ₹750 |
| Concert Ticket | ₹750 |

## Requirements

- Python 3.x
- No external libraries are required.

## Project Structure

```text
Ticket-Booking-System/
├── ticket_booking.py
├── statement.md
└── README.md
```

## How to Run

Check that Python is installed:

```bash
python --version
```

Run the program:

```bash
python ticket_booking.py
```

## Menu

```text
======================================
       TICKET BOOKING SYSTEM
======================================
1. View Available Tickets
2. Book Ticket
3. View Bookings
4. Cancel Ticket
5. Exit
======================================
Enter your choice:
```

## Booking Process

1. Select **Book Ticket**.
2. Enter the Ticket ID.
3. Enter the number of tickets.
4. Enter the customer name.
5. Enter the phone number.
6. The system calculates the total amount.
7. A unique Booking ID is generated.

## Example

```text
Enter Ticket ID: 2
Enter number of tickets: 2
Enter passenger/customer name: Rahul
Enter phone number: 9876543210

========== BOOKING SUCCESSFUL ==========
Booking ID : 1001
Customer   : Rahul
Ticket     : Bus Ticket
Quantity   : 2
Total      : ₹ 300
```

## Technologies Used

- **Language:** Python
- **Interface:** Command Line.
- **Data Storage:** Python Lists and Dictionaries

## Limitations

- Booking data is stored only during program execution.
- Data is lost when the program is closed.
- There is no user authentication.
- There is no permanent database.

## Future Enhancements

- Add MySQL or SQLite database support.
- Add user registration and login.
- Add a graphical user interface (GUI).
- Add online payment integration.
- Add email/SMS booking confirmation.
- Add date and time selection.
- Add seat selection.
- Add booking history.
- Add an administrator panel.

## License

 This project of "Ticket Booking System Python Project." is been made for educational purpose so, their is no need for license for it and it is in properly manner written the code in it.
