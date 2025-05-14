#add import

import question_c

def main():

    while True:
        print("Stock Menu:")
        print("1 - Display Stock Purchase History")
        print("2 - Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            question_c.stock_purchase_history()

        elif choice == '2':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, or 2")

main()