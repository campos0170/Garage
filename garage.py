class parkingGarage():

    def __init__(self,ticket,parkingSpaces,currentTicket):

        """

        ATTRIBUTES:
        
        - ticket, is an integer
        - parkingSpaces, is a list
        - currentTicket, is a dictionary


        """

        self.ticket = ticket
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):

        if len(self.parkingSpaces)<1: # parking space

            print("Sorry, the Garage is full!")

        else:
            self.currentTicket[self.ticket]=False
            self.ticket+=1
            self.parkingSpaces.pop()

    def payForParking(self):
        amount = input("Hello and welcome! Please insert your payment now: ")
        i_d = input("What is your ticket id? ")
        if i_d in self.currentTicket:
            self.currentTicket[i_d] = True
        

    def leaveGarage(self):
        # remove i_d from currentTicket
        i_d = input("What is your ticket id? ")
        
        self.currentTicket.pop(i_d)

        # add a space back to parking spaces

        self.parkingSpaces.append(1)
        

    

    

    