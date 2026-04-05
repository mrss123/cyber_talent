try : 
    ip1 = int (input ("enter ip part 1:"))
    ip2 = int (input ('enter ip part 2:'))
    ip3 = int (input ("enter ip part 3:"))
    ip4= int  (input ("enter ip part 4:"))
except ValueError:
    print ("-" * 30)
    print ("please enter a number from 0-255 only")
    print ("-" * 30)
if not  (0 <= ip1<= 255 and 0 <= ip2<= 255 and 0 <= ip3<= 255 and 0 <= ip1<= 255 ):
    print (f"The ip {ip1}.{ip2}.{ip3}.{ip4} you entered is not valid")
print ("-" * 30)
print (f"IP: {ip1}.{ip2}.{ip3}.{ip4}")
print ("VALID")
while True:     

        if ip1 <= 127 :
            
            print ("CLASS A")
            print ("8 default subnet")
            
        elif 127 < ip1 <= 191 :
           
            print ("CLASS B")
            print ("16 default subnet")
            
        elif 192 <= ip1 <= 223 :
             
            print ("CLASS C")
            print ("24 default subnet")
            
        elif 224 <= ip1 <= 239 :
            
            print ("CLASS D")
            print ("used for broadcasting multiple hosts")
            
        elif 240 <= ip1 <= 255 :
            
            print("CLASS E")
            print ("reserved for research and future")
            
        if ip1 in (0, 10, 172 ,192 , 127, 224, 240, 255):
            print("private IP")
        else:
            print ("public address")
        print ("-" * 30)
        break    
    