Author: Efrain Migel Vasques Jr

Program Description: A graphing program written in Python 3 to receive values from Serial through Python for graphing and recording to later read. A data logging tool basically, useful to test and otherwise monitor sensors and particular values sent through from an Arduino microcontroller. Uses the serialpy library to easily grab sent values through serial. It currently can only read and write to .txt files. The specific formatting will be found in an example text file in this repository named "Test_data_large". It is limited to graphing one stream of float values at any given time. In a future date I will add the capability to graph multiple inputs and plot each one separately. 

It's usage is pretty simple:


**However, there are a few things to do first, in order to get the Python script working properly and install the needed modules. I highly recommend using Linux. Windows, after much trial and error trying to get it to work, is more of a hassle.**


Modules needed: PIP, Matplotlib, and serialPy

Installing PIP if not installed previously: sudo apt-get install python3-pip python-dev

Installing Matplotlib: sudo apt-get install python3-matplotlib

Installing serialPy: sudo apt-get install -y python3-serial


1. Make sure Arduino is connected, know which port it's connected to. Depends if the environment is Windows or Linux.
2. Run the Arduino code and print to serial the desired data.
3. Run the SerialGrapher.py and choose the first option.
4. When prompted, enter the appropiate port (ex. "COM7"), baud rate (ex. 9600), name, and type of data to label the y-axis.
5. If everything has been entered correctly, a matplotlib window should appear graphing and plotting the incoming data.

