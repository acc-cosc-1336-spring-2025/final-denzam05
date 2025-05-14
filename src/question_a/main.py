#add import
import question_a

def main():
    while True:
        print("\nMenu:")
        print("1 - Display multiplication table")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            table = question_a.create_multiplication_table()
            question_a.display_multiplication_table(table)
        elif choice == "2":
            print("Exiting!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

main()