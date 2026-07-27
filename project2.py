total = 0

def main():
    global total
    while True:
        expense = input("Enter an expense (or type 'quit' to stop): ")

        if expense == "quit":
            break

        try:
            expense = int(expense)
            total += expense
        except ValueError:
            print("Invalid Data")

    print(f"FINAL TOTAL: {total}")

if __name__ == "__main__":
    main()