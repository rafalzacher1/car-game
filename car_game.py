# Car Game: entry point (text menu, pygame loop, logging).

import pygame
import time

import gen_maze
import help_text
import session_io as library


log_file_name = "session_log.txt"                                   # Append-only operator session log
factory_layout = "factory_map.csv"                                  # Factory / maze layout (CSV)
file_object = library.open_log_file(log_file_name, "a")             # Open the file in append mode
print()
help_text.welcome_autonomous_vehicle()                                   # Prints a greeting message and information about the program
print()
operator_name = library.ask_for_string("Please enter your name: ")  # Request operator's name (mandatory)


def main():
    library.welcome(operator_name)                      # Prints a greeting message with the user's name
    library.write_log_date(file_object, operator_name)  # Record operator's name in a log file
    print()
    print("Please make a selection")
    print()
    selection = 0                                                       # Sets the variable to 0
    while not selection == 5:                                           # Creates a loop for help
        # List of help that user can get
        print("Enter 1 for basic instruction")
        print("Enter 2 for technical information")
        print("Enter 3 for expert information")
        print("Enter 4 for context help")
        print("Enter 5 to start")
        print("Enter 6 to stop")
        print()
        selection = library.ask_for_whole_number("Enter selection: ")   # Asks the user for a number
        print()
        # User selects a number to get the help required
        if selection == 1:
            help_text.novice_help()
        if selection == 2:
            help_text.intermediate_help()
        if selection == 3:
            help_text.expert_help()
        if selection == 4:
            help_text.context_help()
        if selection == 5:
            start_run()
        if selection == 6:
            break
    library.write_log_date(file_object, "End.")         # Write the operator's name in the log file
    library.close_log_file(file_object)                 # Close the log file


def start_run():
    print("Starting...")
    car = gen_maze.Car()
    gen_maze.main(factory_layout, car)
    car.filedata = gen_maze.filedata                         # Pass the factory map to the car
    library.write_log_date(file_object, factory_layout)     # Record the factory layout being used

    # First the outward journey
    car.Finished = False
    while not car.Finished:
        direction = "?"     # Tells the car which direction to go
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                library.write_log_date(file_object, "Terminate by operator.")
                return

            # Key commands for the car
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w] or pressed[pygame.K_UP]: direction = "U"
            if pressed[pygame.K_s] or pressed[pygame.K_DOWN]: direction = "D"
            if pressed[pygame.K_a] or pressed[pygame.K_LEFT]: direction = "L"
            if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]: direction = "R"
            # Update for help
            if pressed[pygame.K_i]: direction = "I"

            # Validates the key commands
            if direction in ['U', 'D', 'L', 'R']:
                car_direction = car.move(direction)
                if not car_direction:
                    print("Stop crashing the car!!")

                # Record the station IDs when the car drives on them
                station_id = int(car.get_trackinfo())
                if station_id > 3:
                    print("This is the station ID", station_id)
                    library.write_log_date(file_object, "Station: " + str(station_id))

            gen_maze.render(car)     # Renders the map to update any movements

    # Return journey
    print("Returning now!!")
    print()
    direction = ""
    return_route = ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D']    # Return journey
    car.Finished = False
    for direction in return_route:
        print(direction)
        car_direction = car.move(direction)
        if not car_direction:
            print("Crashed again!!")
        gen_maze.render(car)
        time.sleep(1)


main()
