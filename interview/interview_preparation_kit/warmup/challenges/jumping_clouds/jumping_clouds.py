def jumping_clouds():
    clouds = []
    last_value = 0   
    count = num_c = int(input("Please enter number of clouds: "))
    if 2 <= num_c <= 100:
        count = num_c
        while num_c != 0:
            value = int(input("Please enter values of clouds: "))            
            while 0 != value != 1:                
                value = int(input("Please enter either {0 or 1} for values: "))
            else:
                clouds.append(value)                                      
                while clouds[0] != 0:
                    clouds.remove(value)
                    value = int(input("Please make sure that the first the last value  is [0]: ")) 
                    clouds.append(value)                                 
            num_c -= 1 
            print(clouds)                  
    else:
        print("Please enter value between 1 and 101")
        jumping_clouds()

    if clouds[num_c-1] != 0:
        print("Last value has to be [0], replacing with zero")
        clouds.remove(value)
        clouds.append(last_value)
       
            
    current = 0
    end = count-1
    jumps = 0
    while current < end:        
        if ((current + 2) <= end) and (clouds[current + 2] == 0):
            current += 2
            jumps += 1
        elif clouds[current + 1] == 0:
            current += 1
            jumps += 1
    print(jumps)       


jumping_clouds()