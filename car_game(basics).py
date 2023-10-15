# Initialize variables
command = ""
started = False

# Continuously prompt the user for input
while True:
    # Prompt the user for input and convert it to lowercase for easier comparisons
    command = input("> ").lower()

    # Check the user's input and provide appropriate responses
    if command == "help":
        print("""
        start - car started
        stop - car stopped
        quit - end of the game
        """)
    elif command == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started.")
    elif command == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped.")
    elif command == "quit":
        # Exit the loop and end the program
        break
    else:
        print("We don't understand that command.")
