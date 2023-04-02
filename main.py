import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 6,
    "C": 4,
    "D": 8
}

symbol_value = {
    "A": 6,
    "B": 3,
    "C": 4,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings , winning_lines

def slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #copy of list : to copy a list use [:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


# input how much you want to deposit function
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than $0")
        else:
            print("Please enter a valid Number!")

    return amount

# function for picking num of lines to bet on
def get_num_of_lines():
    while True:
        lines = input("enter a number of lines to bet on (1 - {})? ".format(MAX_LINES))
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a Valid Number of lines")
        else:
            print("Please enter a valid Number!")

    return lines

#function for picking how much you would like to bet for each line
def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between ${} - ${}".format(MIN_BET, MAX_BET))
        else:
            print("Please enter a valid Number!")

    return amount

def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("you dont have enough money deposited to make this bet, current balance is ${}".format(balance))
        else:
            break
    print("You are betting ${bet} on {lines} lines, Total is ${total_bet}".format(bet=bet, lines=lines, total_bet=total_bet))

    slots = slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while balance > 0:
        print(f"Current balance is: ${balance}")
        answer = input("press enter to spin! (Press Q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    while balance == 0:
        ans = input("You are out of money! press Y to deposit more, or press Q to quit: ")
        if ans == "y":
            main()
        if ans == "q":
            break
        

main()
