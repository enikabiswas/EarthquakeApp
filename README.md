# EarthquakeApp
Earthquake app for predicting earthquakes, notifying people and gathering information about these events

# Backend 
- Database/server:
    - Current system uses a virtual server with an Influx database and this current system seems to work efficiently
     - A possible alternative to this method would be to use Amazon AWS: https://aws.amazon.com/
       - I have created a virtual private cloud with a public and private subnet including PostgreSQL virtual database. The maximum amount of gigabytes that this cloud can hold is 20 GB, but this number can be increased if money is paid
    - The main benefit of using a cloud service like AWS is that the sensor data can be more easily accessed by anyone around the world
  
- Sensor optimization 
    - Current system uses a raspberry pi model b with the HMR2300 magnetometer. However, there has been issues with signal dropping every other second. 
        - Data sheet for HMR2300:
        https://aerospace.honeywell.com/~/media/aerospace/files/datasheet/smartdigitalmagnetometerhmr2300_ds.pdf
        - Schematic that shows how data is being collected by the raspberry pi: https://www.dropbox.com/s/58sekts03p6gpva/Screenshot%202016-08-01%2013.00.37.png?dl=0
    - Things that still need to be done to diagnose the signal dropping:
        - Hardware diagnosis: Hook up the magnetometer-raspberry pi system to an oscillascope and see what kind of signal is produced
             - Most likely if it it is a straight line, then there is an issue with the communication between the pi and the sensor; in which case, the connection must be further secured by means of soddering or the serial communication between the RS232 port of the HMR2300 and the TTL conversion of the pi should be further looked into by conducting an experiment with the HMR2300 and a different serial communication such as RS485, which is better at handling excess noise. Here is a link that goes deeper into the serial communication: http://www.farnell.com/datasheets/46088.pdf
             - Most likely if it is some kind of a sine wave with gaps, then the magnetometer is probably faulty, and a software diagnosis will need to be done to see numerically what kind of data the magnetometer is picking up. 
        - Software dignosis: I have written a piece of code called EEPROM.py (within this branch) that can be used to test each memory address of an external EEPROM. This code will need to be tested with the magnetometer-raspberry pi system we currenly have in Alaska to see if we can get the numerical data of each memory address in the magnemtometer
