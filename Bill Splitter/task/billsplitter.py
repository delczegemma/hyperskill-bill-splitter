import random

def guest_num():
    try:
        return int(input("Enter the number of friends joining (including you):"))
    except ValueError:
        return 0

def guest_list(num):
    print("Enter the name of every friend (including you), each on a new line:")
    guests = {}
    while len(guests) < num:
        name = input()
        if name in guests:
            print(f"{name} is already on the list, please enter a different name")
        else:
            guests[name] = 0
    return guests

def get_the_bill():
    while True:
        try:
            bill = float(input("Enter the total bill value:"))
        except ValueError:
            print("Please enter a number:")
            continue
        if bill <= 0:
            print("Please enter a positive number:")
            continue
        return bill

def bill_split(bill, people):
    people_in_debt = { debt: round(bill / len(people), 2) for debt in people}
    return people_in_debt

def ask_lucky(guests):
    command = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:').lower()
    if command == 'yes':
        return random.choice(list(guests.keys()))
    return None

def redistribute(lucky, bill, guests):
    debt = round(bill / (len(guests)-1), 2)
    return { name: 0 if name == lucky else debt for name in guests }

def main():
    num_of_guests = guest_num()
    if num_of_guests <= 0:
        print("No one is joining for the party")
    else:
        guests = guest_list(num_of_guests)
        bill = get_the_bill()
        guests = bill_split(bill, guests)
        if len(guests) > 1:
            lucky = ask_lucky(guests)
            if lucky is None:
                print("No one is going to be lucky")
            else:
                print(f"{lucky} is the lucky one!")
                guests = redistribute(lucky, bill, guests)
        print(guests)


main()