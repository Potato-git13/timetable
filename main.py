#!/bin/python
import re
import os
import random

timetable = []


def print_timetable():
    # Output the items from the timetable list and properly format them
    try:
        print("")
        for item in timetable:
            print(f"{item[0]}\t{item[1]}\t:\t{item[2]}")
        print("")
    except IndexError:
        print("ERROR - One of your items doesn't include all of the required arguments\n"
        "or there are too many of them. Please remove the illegal item\n"
        "Type -h if you do not know how to remove an item\n")


def final_timetable():
    output = ""
    longest = 0
    length = 0
    out = ""
    # Get the longest string in the timetable list and put its len in longest
    for item in timetable:
        out = f"{item[0]}\t{item[1]}\t:\t{item[2]}"
        length = len(out)
        if length > longest:
            longest = length
    # Make the timetable upper cover and lower cover by calculating it based on the longest string
    cover = " _"
    lower = " \\"
    for i in range(longest):
        cover = cover + "_"
        lower = lower + "_"
    cover = cover + "___" * 3
    lower = lower + "___" * 3
    
    # Save the result to output
    cover = cover + "__\n"
    lower = lower + "_/\n"
    output = output + cover

    # Convert the items in timetable list to fit in the final timetable
    for item in timetable:
        out = f"{item[0]}\t{item[1]}\t:\t{item[2]}"
        while len(out) != longest:
            out = out + " "
        out = "| " + out + " |\n"
        output = output + out

    output = output + lower
    # Return the final string to be writen on the screen/writen to a file
    return output


print("Type '-h' for help")

while True:
    print_timetable()
    # Get the input and execute the command user entered
    command = input("> ")

    if command.startswith("add "):
        command = re.sub("add ", "", command)
        input_array = command.split(", ")
        timetable.append(input_array)

    elif command.startswith("rm "):
        command = re.sub("rm ", "", command)
        try:
            command = int(command) - 1
            del timetable[command]
        except ValueError:
            print("ERROR - Your input was not a number")
        except IndexError:
            print("ERROR - Index out of range")

    elif command == "exit":
        exit(0)

    elif command == "-h":
        print("To add an item type 'add ITEMNAME, TIMEFROM, TIMETO'")
        print("To remove an item type 'rm ITEM_INDEX_NUMBER' (starts with 1)")
        print("To exit type 'exit'")
        print("To print the final timetable type 'final-timetable'")

    elif command == "final-timetable":
        save = input("Do you want your timetable to be writen to a file?(y/n) ").lower()
        if save == "y":
            # Create a dir and a file to write the final timetable in
            try:
                os.mkdir("timetables")
            except FileExistsError:
                pass
            while True:
                try:
                    f = open("timetables/timetable-" + str(random.randint(0, 999)), "x")
                    break
                except FileExistsError:
                    pass

            write_timetable = final_timetable()
            print(write_timetable)
            f.write(write_timetable)
            print("Timetable saved to a file in the timetables directory")
        else:
            print(final_timetable())
