class Rooms:

    def __init__(self, number, items, hotelname): 
        self.number = number
        self.items = items
        self.hotelname = hotelname

    @classmethod
    def from_input(cls):
        return cls(
            input('ID of Rooms: \n '),
            dict(input('enter commodities with price \n').split() for _ in range(2)), 
            str(input('name of hotel \n')),
        )
    def __str__(self):
        return ("you are staying at the {} hotel and the room number is {} and the commodities are {} ".format(self.hotelname,self.number,self.items))


def main():
    noRooms=int(input('enter rooms you want \n '))
    como=int(input('enter number of commodities you want \n '))
    rooms = {}
    for _ in range(noRooms):  # enter room objects 
        room = Rooms.from_input()  # from room input
        rooms[tuple(sorted(room.items))] = room  # and store them in the dictionary
    print(room)

if __name__=="__main__": 
    main()         
