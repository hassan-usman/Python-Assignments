command = ""
started = False
while True:
    command = str(input("< "))
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car is started")
    elif command == "stop":
        if not  started:
            print("Car is already stopped")
        else:
            started = False
            print ("Car is stopped")
    elif command == "help":
        print("""
start - To start the car        
stop - To stop the car
quit - To close the game                
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand")

































































































