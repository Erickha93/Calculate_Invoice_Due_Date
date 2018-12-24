#!/usr/bin/env python3

from datetime import datetime, timedelta

# get from the user to format the date out
def get_invoice_date():
    invoice_date_str = input("Enter the invoice date (MM/DD/YY): ")    
    invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%y")
    return invoice_date


# calculate over time due day
def get_calculate_overdue(days_overdue):
    if days_overdue > 0:    # day is greater than zero is over due
            print("This invoice is", days_overdue, "day(s) overdue.")
    else:
        # the day is not meet on the due date
        days_due = days_overdue * -1  # convert date negative to positive number
        print("This invoice is due in", days_due, "day(s).")
    print()


def main():
    print("The Invoice Due Date program")
    print()

    while True:
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)    # timedelta used for count for 30 days
        current_date = datetime.today()         # get the current date
        days_overdue = (current_date - due_date).days   # current date - due date

        # display results
        print("Invoice Date: " + invoice_date.strftime("%B %d, %Y"))
        print("Due Date:     " + due_date.strftime("%B %d, %Y"))    # current date plus in 30 days
        print("Current Date: " + current_date.strftime("%B %d, %Y"))    # current date

        # function for calculation over time for due day
        calculate_overdue = get_calculate_overdue(days_overdue)

        # ask if user wants to continue
        result = input("Continue? (y/n): ")
        print()
        if result.lower() != "y":
            print("Bye!")
            break      

if __name__ == "__main__":
    main()
