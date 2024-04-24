import socket 
# functiont to convert incoming data to uppercase
def convert_to_uppercase(data):
  return data.decode().upper().encode()

  #create a socket object 
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  #get local machine name 
  host = socket.gethostname()
  
  #set port number 
  port = int(input("Enter Port Number:"))

  #bind socket to to a public host, and a port
  serversocket.bind((host, port))

  #become a server socket 
  serversocket.listen(1)
  print("server started on {}:{}".format(host, port))

  while True:
    #establish a connection
    clientsocket, addr = serversocket.accept()
    print("got a connection from {}".fromat(str(addr)))

    while True:
      #receive data from the client
      data = clientsocket.recv(1024)

      #convert data to uppercase
      modified_data = convert_to_uppercase(data)

      #send modified data back to the client
      clientsocket.send(modified_data)

      #if client sends "QUIT" close the connection
      if data.decode() == "QUIT":
        clientsocket.close()
        break
