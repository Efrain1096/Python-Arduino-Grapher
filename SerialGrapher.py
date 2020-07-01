import csv
# import tkinter
import datetime
import os
import statistics
import sys
import time

import matplotlib.pyplot as plt
# import matplotlib.animation as animation
import numpy as np
import serial  # importing the serialpy library to communicate through serial

data_values = []  # list to save the data values for plotting
time_stamps = []  # Time stamps list for plotting


# local_time = time.strftime("%Y-%b-%d_%H:%M:%S", time.localtime())#This saves the date and time to name the text log file created to archive the values
local_time = datetime.datetime.now()


def graph_record_data_txt(port_name, baud_rate, name_of_file, data_type):
    port = port_name
    baud = baud_rate
    arduino = serial.Serial(port, baud)  # Initialize/open the serial port with the name of the arduino port and the baud rate

    while arduino.isOpen():  # If the port of the device we want is open

        print(arduino.name + ' is open...')
        log_file = open(str(name_of_file) + "_" + str(data_type) + ".txt", "w+")  # Names the file as the local time and date
        i = 0  # Used for counting and index positioning

        while arduino.isOpen():
            k = arduino.readline()  # Reading data from the serial object
            y = float(
                k)  # By default, the readline reads in stuff as a string. So, I have decided to convert it into float numbers

            data_values.append(y)  # Add each incoming value to the end of the list
            time_stamps.append(time.strftime("%H:%M:%S", time.localtime()))  # Every loop save a time stamp for x-axis

            log_file.write(time_stamps[i] + "," + str(data_values[i]))  # Write the incoming values to a text file.
            log_file.write('\n')  # Separate each entry onto it's own line
            log_file.flush()  # Flush the internal buffer of the object

            print("At time: " + str(time_stamps[i]))

            print("Value: " + str(
                data_values[i]))  # Print out values to interpreter to display values as they are graphed

            print("Average: " + str(statistics.mean(data_values)))

            print('\n')

            plt.xticks(rotation=90)  # Rotate the x axis to minimize overlapping values
            plt.plot(time_stamps, data_values, linestyle='-', marker='o', color='b')

            plt.ylabel(str(data_type))  # y-axis
            plt.xlabel("Time")  # x-axis
            i = i + 1

            plt.pause(0.50)  # Pause for 1 second


def graph_data_csv():  # Incomplete function for CSV plotting
    port = "COM13"
    baud = 9600
    arduino = serial.Serial(port, baud)  # Initialize/open the serial port with the name of the arduino port and the baud rate

    while arduino.isOpen():  # If the port of the device we want is open
        print(arduino.name + ' is open...')
        log_file = open(str(local_time) + " Height values" + '.csv', "w+")  # Names the file as the local time and date
        i = 0

        while arduino.isOpen():
            print(2)


def list_txt_files(): # Works on Windows. Linux, not so much....
    path = os.getcwd() # Gets the absolute path of the current working directory
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

    for f in files:
        print(f)

def graph_read_data_txt(file_to_read):  # Read data from a specially formatted text file
    data_read = open(str(file_to_read) + ".txt",
                     'r').read()  # Append the file extension to end of name to retrive desired file of data values
    data_file = data_read.split('\n')
    t_values = []  # Save the read time stamp values
    y_values = []  # Save the read data values
    i = 0
    for each_line in data_file:
        if len(each_line) >= 1:  # If the line is more than 0 characters essentially

            t, y = each_line.split(',')
            t_values.append(str(t))
            y_values.append(float(y))
            plt.ylabel("Data")  # y-axis
            plt.xlabel("Time)")  # x-axis
            plt.xticks(rotation=90)  # Rotate the x axis to minimize overlapping values
            plt.plot(t_values, y_values, linestyle='-', marker='o', color='g')
            print(y_values[i])
            print("At second:  ")
            print(i)
            print("Avg: ")
            print(statistics.mean(y_values))  # Average of read values
            print('\n')
            i = i + 1
            plt.pause(0.01)

    print("Finished reading: " + file_to_read + ", on " + str(local_time))
    print(" Data read from a time interval of: " + str(i) + " seconds")
    plt.show()
##############################################################################################################################
print('\n')
print("Welcome to the serial graphing program!")
choice = input(
    "Enter 1 to graph from serial\nEnter 2 to graph from a text file\nEnter 3 to list text files\nEnter 'about' to know about this program: ")
print('\n')

if choice == '1':
    port = input("Enter port name: ")
    baud = input("Enter baud rate: ")
    file_name = input("Enter desired name for file: ")
    data_type = input("What kind of data?: ")
    # type_of_file = input("Which kind of file?(txt): ")
    graph_record_data_txt(port, baud, file_name, data_type)

if choice == '2':
    file_name = input("Enter name of file to graph: ")
    graph_read_data_txt(file_name)

if choice == '3': # Work in progress feature.
    #file_ext = input("Enter file extension(.txt): ")
    # directory = input("Enter name of directory to list files: ")
    # list_txt_files(directory, file_ext)
    list_txt_files()
'''
if choice == "about":
    words = []
    data_read = open("About_Graph_From_Serial" + ".txt",
                     'r').read()  # Append the file extension to end of name to retrive desired file of data values
    data_file = data_read.split('\n')
    i = 0
    print("\n")
    for each_line in data_file:
        if len(each_line) >= 1:
            print(each_line)
            print("\n")
'''

