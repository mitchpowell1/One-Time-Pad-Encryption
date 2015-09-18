__author__ = 'Mitchell Powell'
__date__ = 'April 26, 2015'
__course__ = 'CSC 344'
import sys #allows program to process command line arguments

### The Read_Key function reads a key in plaintext format and converts it into binary to
### pad the message text
def Read(KeyFile):
    Keyf = open(KeyFile)
    Key = str(Keyf.read())
    Keyf.close()
    bin_key = ''
    for char in Key:
        bin_key += '{0:08b}'.format(ord(char)) ##Ensures that 8 bits are stored instead of just significant bits.
    return(bin_key)

### Write_Cyph function takes a Source string and writes it to a file "NewFile"
def Write_Cyph(Source, NewFile):
    New = open(NewFile,'w')
    New.write(Source)
    New.close()

### Encrypt function takes two strings of bits and performs an XOR function, outputting the result as a string of bits
def Encrypt(Key_Bin,Mess_Bin):
    Cypher = ''
    for index in range(len(Mess_Bin)):
        Cypher += str(int(Mess_Bin[index])^int(Key_Bin[index]))
    Char_Cypher = ''
    for byte in range(0,(len(Cypher)/8)):
        Char_Cypher += chr(int(Cypher[(8*byte):(8*byte)+8],2)) #Interprets a byte at a time and then
    return(Char_Cypher)                                        #Returns the result as a character string


##Main function reads in the Key and Message files, saves them as a variable called "CypherText"
##and then writes those to a file called "NewFile"
def Main(Key, Message, NewFile):
    CypherText = Encrypt(Read(Key),Read(Message))
    Write_Cyph(CypherText, NewFile)

##Passes command line arguments through to the Main function when it is called.
Main(sys.argv[1],sys.argv[2],sys.argv[3])
##Note: sys.argv takes the arguments from the command line and stores them as a list. The first item on this list
##is the name of the program (OTpad.py) followed by the actual arguments.