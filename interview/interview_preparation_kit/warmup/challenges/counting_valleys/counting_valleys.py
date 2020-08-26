def countingValleys(n, s):
    cu=0
    cd=0
    count=0    
    mv=0
    vv=0
    end=n-1

    while end > 0:
        m = cu+cd
        v = cu+cd
        if s[count] == 'U':
            cu+=1
            count+=1
            if m==0:
                mv+=1
        elif s[count] == 'D':
            cd-=1
            count+=1
            if v==0:
                vv+=1
        end -= 1
    return vv