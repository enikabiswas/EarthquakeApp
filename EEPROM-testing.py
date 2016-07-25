import RPi.GPIO as GPIO
import time, re
GPIO.setmode(GPIO.BCM) #Use chip numbering scheme; 

#CE, WE, OE pins (pull down to activate each mode): This communicates the pi with the GPIO pins 
GPIO.setup (2, GPIO.OUT, pull_up_down = GPIO.PUD_UP) #CE; The number is the pin of the CE unique to each EEPROM
GPIO.setup (3, GPIO.OUT, pull_up_down = GPIO.PUD_UP) #OE; The number is the pin of the OE unique to each EEPROM
GPIO.setup (4, GPIO.OUT, pull_up_down = GPIO.PUD_UP) #WE; The number is the pin of the WE unique to each EEPROM 

#Set the chip in standby mode: Gives a high signal to the setup CE, WE, and OE pins to turn it off  
GPIO.output(2,1) #CE - high
GPIO.output(3,1) #OE - high
GPIO.output(4,1) #WE - high

#Address pins set for output (A15, A16, A17 connected to ground): Sets up the GPIO outputs of the pi (depends on how the GPIO outputs have been configured)
GPIO.setup (10, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A0
GPIO.setup (9,  GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A1
GPIO.setup (11, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A2
GPIO.setup (25, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A3
GPIO.setup (8,  GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A4
GPIO.setup (7,  GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A5
GPIO.setup (5,  GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A6
GPIO.setup (6,  GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A7
GPIO.setup (12, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A8
GPIO.setup (13, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A9
GPIO.setup (19, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A10
GPIO.setup (26, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A11
GPIO.setup (16, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A12
GPIO.setup (20, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A13
GPIO.setup (21, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN) #A14

#Data pins set for input (pull down for zeroes): Sets up the GPIO inputs of the pi 
GPIO.setup (14, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D0
GPIO.setup (15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D1
GPIO.setup (18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D2
GPIO.setup (17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D3
GPIO.setup (27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D4
GPIO.setup (22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D5
GPIO.setup (23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D6
GPIO.setup (24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #D7

i=0 #You enter the memory address of the EEPROM in a 15 bit format
try:
    while (i==0):
        A=[]
        A=raw_input("Type memory address to read (15 bits): ")

        if not re.match("^[0-1]*$", A) or (len(A) != 15):
            print "Error! Only 1 and 0 allowed. Please type 15 bits."

        else:
            i=1
            A=map(int, A) #Converts the strings to an integer 
except KeyboardInterrupt:
    print "Keyboard Interrupt.\nPerforming GPIO cleanup."
    GPIO.cleanup()

#Set address bus: Gives either the 1 or 0 (high/low) points of array A to the output pins of the pi
GPIO.output(10,A[0])    #A0
GPIO.output(9,A[1])     #A1
GPIO.output(11,A[2])    #A2
GPIO.output(25,A[3])    #A3
GPIO.output(8,A[4])     #A4
GPIO.output(7,A[5])     #A5
GPIO.output(5,A[6])     #A6
GPIO.output(6,A[7])     #A7
GPIO.output(12,A[8])    #A8
GPIO.output(13,A[9])    #A9
GPIO.output(19,A[10])   #A10
GPIO.output(26,A[11])   #A11
GPIO.output(16,A[12])   #A12
GPIO.output(20,A[13])   #A13
GPIO.output(21,A[14])   #A14

#Operation Loop; Reading capabilities is on
try:
    print "Turning on the chip and setting it to output mode."
    GPIO.output(3,0) #OE - low - enable output
    GPIO.output(2,0) #CE - low - turn on the chip
    time.sleep(0.1)
    print "Reading the address."

    #set data variables; the Pi will take the readings from the eeprom and the pi will read it   
    D0= GPIO.input(14)
    D1= GPIO.input(15)
    D2= GPIO.input(18)
    D3= GPIO.input(17)
    D4= GPIO.input(27)
    D5= GPIO.input(22)
    D6= GPIO.input(23)
    D7= GPIO.input(24)

    print str(D0)+" "+str(D1)+" "+str(D2)+" "+str(D3)+" "+str(D4)+" "+str(D5)+" "+str(D6)+" "+str(D7)
    GPIO.output(2,1) #CE - high - standby mode
    GPIO.output(3,1) #OE - high - disable output
    GPIO.cleanup()

except KeyboardInterrupt:
    print "Keyboard Interrupt.\nPerforming GPIO cleanup."
    GPIO.cleanup()
