def main():
    print("Welcome To The Circuit Identifier")
    print("Please Answer the Following Questions and choose the best number according to your observation")
    
    def get_user_choice(prompt, options):
        while True:
            try:
                choice = int(input(prompt))
                if choice in options:
                    return choice
                else:
                    print(f"Invalid choice. Please choose {options}.")
            except ValueError:
                print("Please enter a valid number.")
    
    # Question 1
    print("A. How are the components connected?")
    print("1) End-to-end nodes via straight path")
    print("2) Across common points, providing multiple paths")
    user_choice1 = get_user_choice("Enter your choice (1 or 2): ", [1, 2])
    
    # Question 2
    print("B. Does the current have only one path to flow through all components?")
    print("1) Yes, only one path")
    print("2) No, multiple paths")
    user_choice2 = get_user_choice("Enter your choice (1 or 2): ", [1, 2])
    
    # Question 3
    print("C. If one component fails, does the entire circuit stop functioning?")
    print("1) Yes, the entire circuit stops")
    print("2) No, other paths still function")
    user_choice3 = get_user_choice("Enter your choice (1 or 2): ", [1, 2])
    
    # Analyzing and interpreting the user's input
    if user_choice1 == 1 and user_choice2 == 1 and user_choice3 == 1:
        circuit_type = "Series Circuit"
    elif user_choice1 == 2 and user_choice2 == 2 and user_choice3 == 2:
        circuit_type = "Parallel Circuit"
    else:
        circuit_type = "undetermined based on your choices. Please observe circuits properly."
    
    # Printing User Output based on given choices
    print(f"\nThe circuit is a {circuit_type}.")
    print("Thank you for using the Circuit Identifier. Have a great day!")

# Call the main function to run the program
if __name__ == "__main__":
    main()
