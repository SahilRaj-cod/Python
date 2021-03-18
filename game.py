command = ""
while command  != "quit":
        command = input("> ").lower()
        if command == "start":
            print("The Car is Start ! Its Moving")

        elif command == "stop":
            print("The Car is Stopped Now ")

        elif command == "help":
            print("""Commands :
1 Start (To start the car)
2 Stop (To stop the car)
3 Quit (To Quit  the Game)""")
        else:
            print("Sorry I Don't understand")    

         