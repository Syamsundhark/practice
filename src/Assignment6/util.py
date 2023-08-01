def values(number):
    for i in range(1,number+1):
        hex_des="{0:x}".format(i)
        print(i," ",oct(i)[2:]," ",hex_des," ",bin(i)[2:])