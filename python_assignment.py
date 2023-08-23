dict1={"AI161E90":["From: BLR","To: BOM","Price: 5600"],"BR161F91":["From: BOM","To: BBI ","Price: 6750"],"AI161F99":["From: BBI ","To: BLR ","Price: 8210"],"VS171E20":["From: JLR","To: BBI ","Price: 5500"],"AS171G30":["From: HYD","To: JLR ","Price: 4400"],"AI131F49":["From: HYD ","To: BOM ","Price: 3499"]}
dict2={"BLR":["AI161E90","From: BLR","To: BOM","Price: 5600"],"BOM":["BR161F91","From: BOM","To: BBI ","Price: 6750"],"BBI":["AI161F99","From: BBI","To: BLR ","Price: 8210"],"JLR":["VS171E20","From: JLR","To: BBI ","Price: 5500"],"HYD":["AS171G30","From: HYD","To: JLR ","Price: 4400"],"HYD1":["AI131F49","From: HYD","To: BOM ","Price: 3499"]}
dict3={"BOM":["AI161E90","From: BLR","To: BOM","Price: 5600"],"BBI":["BR161F91","From: BOM","To: BBI ","Price: 6750"],"BLR":["AI161F99","From: BBI","To: BLR ","Price: 8210"],"BBI1":["VS171E20","From: JLR","To: BBI ","Price: 5500"],"JLR":["AS171G30","From: HYD","To: JLR ","Price: 4400"],"BOM1":["AI131F49","From: HYD","To: BOM ","Price: 3499"]}
print('''
    1) Flight ID
    2) The source city 
    3) The destination city 
''')
flag=1
while(flag==1):
    choice=int(input("Enter your choice: "))
    if(choice==1):
        b=input("Enter the Flight Id: ")
        print(dict1[b])
    elif(choice==2):
        b=input("Enter the Source City: ")
        if(b=="HYD"):
            print(dict2["HYD"])
            print(dict2["HYD1"])
        else:
            print(dict2[b])
    elif(choice==3):
         b=input("Enter the Destination City : ")
         if(b=="BOM"):
             print(dict3["BOM"])
             print(dict3["BOM1"])
         elif(b=="BBI"):
             print(dict3["BBI"])
             print(dict3["BBI1"]) 
         else:
             print(dict3[b])
    else:
        flag=0



