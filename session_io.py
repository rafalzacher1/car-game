# Session and console I/O helpers (prompts, append-only log).

# ANYTHING is a variable that is changed in the actual program
# it has no dependency. It's used to pass on arguments

import datetime


# Request input, this is mandatory
# The prompt parameter is the text to display in the input statement
def ask_for_string(ANYTHING):
    value = ""                              # Local variable
    while len(value) == 0:                  # Mandatory input
        value = input(ANYTHING).strip()     # No leading or trailing spaces
        if len(value) > 0:
            return value


# Ask the user to input a numeric integer
def ask_for_whole_number(ANYTHING):
    val = ""                            # Local variable
    intresult = None
    while len(val) == 0:                # Mandatory input
        val = input(ANYTHING).strip()     # No leading or trailing spaces
        if val.isdigit():               # Check only numeric digits entered
            intresult = int(val)        # Type conversion to integer
            return intresult            # Returns the value to the function
        else:
            print("That did not work, try a whole number")
            val = ""


# Open the log file
def open_log_file(ANYTHING, mode):
    return open(ANYTHING, mode)


# Closes the file and commit changes to disk
def close_log_file(ANYTHING):
    ANYTHING.close()


# Write data to file buffer
def write_log_date(ANYTHING, data):
    today_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    ANYTHING.write(today_date + ": " + str(data) + "\n")


# Welcome message for the user
def welcome(ANYTHING):
    print("Welcome back", ANYTHING)
