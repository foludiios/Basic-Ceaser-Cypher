AL=['A','B','C','D','E','F','G','H','I','J','K','L','M',
       'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def encrypt(input,key):
    result=''
    for i in input:
        for j in AL:
            if i.upper()==j:
                i=j
                if (AL.index(i)+1)+key<=26:
                    res=AL[AL.index(i)+key]
                    result=result+res
                else:
                    over=(AL.index(i)+1)+key
                    while over>=26:
                        over=over-26
                    res=AL[over-1]      # -1 accounts for indexing which starts at 
                    # 0 instead of 1
                    result=result+res
                result=result.lower()
    print(result)

def decrypt(input,key):
    result=''
    for i in input:
        for j in AL:
            if i.upper()==j:
                i=j
                if (AL.index(i)+1)-key>=0:
                    res=AL[AL.index(i)-key]
                    result=result+res
                else:
                    over=(AL.index(i))-key  # +1 not needed when counting backwards into the end of the loop, i guess
                    # because decrypting backwards, we can only overshoot index by -ve numbers, and since we'd be 
                    # indexing the list using -ve numbers, in which case 0-indexing doesn't apply, so we don't need
                    # to use '+1' to make up for the indexing
                    if over>-27:
                        res=AL[over]
                    else:
                        while over<=-27:
                            over=over+26
                        res=AL[over]
                    result=result+res
            result=result.lower()
    print(result)

encrypt('Mofoluwasho',7)
decrypt('tvmvsbdhzov',7)