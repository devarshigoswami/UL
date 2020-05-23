
prevRoom=[["The Inn \t",1,"No Air Conditioning \t\t ","No Free Breakfast \t ","TV Available \t","No Wifi \t\t ",3],["Royal Palace \t",101 ,"Air Conditioning \t\t","Free Breakfast \t","TV Available \t","Wifi Available \t ",8,"Free Airport Pickup/Drop \t"]]
rooms = []
HotelDeets=1
n=0
while(HotelDeets!=0):
    print("1.Press 1 to Add Hotel")
    print("2.Press 2 to View All hotel")
    print("3.Press 3 to search rooms")
    print("4.Press 4 to exit program")
    ch=int(input())
    number=0

    if (ch==1):
        
        name = str(input("name of your hotel?"))
        n = int(input("Number of rooms?" ))
        
        if not (n > 0):
            # sys.exit("Number of rooms must be positive integer")
            n = int(input("Number of rooms must be positive integer, try again:" ))
        
       
        
        for i in range(n):
            temp = [name, i]
        
            ac = str(input("Do you want Air Conditioning?:( press y for yes )"))
            temp.append("Air Conditioning") if (ac.upper() == "Y") else temp.append("No Air Conditioning")
        
            fb = str(input("Do you want complimentary breakfast? :( press y for yes )"))
            temp.append("Free Breakfast") if (fb.upper() == "Y") else temp.append("No Free Breakfast")
        
            tv = str(input("How about Television?: ( press y for yes )"))
            temp.append("TV Available") if (tv.upper() == "Y") else temp.append("No TV")
        
            wifi = str(input("Do you want free wifi as well?: ( press y for yes )"))
            temp.append("Wifi") if (wifi.upper() == "Y") else temp.append("No Wifi")
        
            temp.append(int(input("Enter the cost in USD?")))
        
            prevRoom.append(temp)
            del temp
        
        #print(rooms)
    if(ch==2):
        print(": Hotel Name \t  : Room Number \t :  Air Conditioning \t : Breakfast \t :  Television \t  : Wifi \t : Cost/night :")
        for item in prevRoom:
            print(":",item[0],""*(13-len(item[0])),":",item[1],""*(13-len(str(item[1]))),":",item[2],""*(20-len(item[2])),":",item[3],""*(12-len(item[3])),":",item[4],""*(15-len(item[4])),":",item[5],""*(7-len(item[5])),":",item[6],""*(12-len(str(item[6]))),":")
        for item in rooms:
            print(":",item[0],""*(13-len(item[0])),":",item[1],""*(13-len(str(item[1]))),":",item[2],""*(20-len(item[2])),":",item[3],""*(12-len(item[3])),":",item[4],""*(15-len(item[4])),":",item[5],""*(7-len(item[5])),":",item[6],""*(12-len(str(item[6]))),":")
    if(ch==3):
           print("Finding hotels in your area..")
           cost=int(input("Please enter your budget/night in $?\n"))
           if not (cost > 0):
            
                cost = int(input("Budget/night must be positive integer, try again:" ))
           counter=0
           for b in range(0,(n+2)):
               if(cost <= prevRoom[b][6]):
                   print(prevRoom[b])
                   counter=1
           
           if(counter==0):
                   print("Sorry, couldnt find any hotel in your budget")
                   ex=input("Press any key to continue\n")
                    
    if(ch==4):
        HotelDeets=0
          
else:
      print("Ending Hotel Application...")