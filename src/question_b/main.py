#add import

from question_b import get_stock_list, write_to_file

def main():

    file_name = 'stock_file.dat'
    write_to_file(file_name)
   

    while True:
        print("\nMenu:")
        print("1-Display stock purchase history")
        print("2-Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            stock_list = get_stock_list()
            print("\nStock Report")
            print(f"{'Company':<15} {'Symbol'}")
            for stock in stock_list:
                print(f"{stock.get_company_name():<15} {stock.get_symbol()}")
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


main() 