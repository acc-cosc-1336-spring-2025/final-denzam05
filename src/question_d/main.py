#add import

import question_d

def main ():

    print ("DNA Substring Finder")

    while True:

        dna_string1 = input("Please enter the primary DNA sequence between 8 to 16): ")

        while not question_d.validate_dna_string1 (dna_string1):
            print ("Invalid input. Please enter a DNA sequence between 8 and 16 characters: ")
            dna_string1 = input("Please re-enter the primary DNA sequence between 8 to 16): ")

        dna_string2 = input("Please enter the secondary DNA sequence exactly 4 characters: ")

        while not question_d.validate_dna_string2 (dna_string2):
            print ("Invalid input. Please enter a DNA sequence exactly 4 characters long: ")
            dna_string1 = input("Please re-enter the secondary DNA sequence with exactly 4 characters): ")

        results = question_d.get_most_likely_ancestor_consensus (dna_string1, dna_string2)

        if results:
            print ("Substring found at positions: ", *results)
        else:
            print ("DNA substring not found") 

        cont = input("Would you like to search again? (y/n): ").strip().lower()
        if cont != 'y':
            print("Exiting...")
            break

main ()