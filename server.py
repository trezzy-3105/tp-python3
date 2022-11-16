from socket import *

HOST = '127.0.0.1'   # or 127.0.0.1 or localhost
PORT = 3600
ADDR = (HOST,PORT)
BUFFER = 4096

#create a socket (SRV)
#see python docs for socket for more info

srv = socket(AF_INET,SOCKSTREAM)

#bind socket to address
srv.bind((ADDR))	#double parens create a tuple with one object
srv.listen(5) # maximum queued connections is 5

conn,addr = srv.accept() #accepts the connection
print ('...connected!')
conn.send('TEST')

conn.close()
