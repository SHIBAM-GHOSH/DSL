def transpose(a):
    result = []
    row = len(a[0])   # using column No. of a to get row No. of result 
                         # No. of rows, columns gets interchanged in transpose operation 
    for i in range(row): #traversing through rows of result 
        x = len(a)   # No of columns of result from No. of rows of a 
        l = []
        for i in range(x):
            l.append(0)   # appending elements in each row of result
        result.append(l)    #appending a row in result matrix
    for x in range(len(a)):  #traversing through rows of  input matrix a
        for y in range(len(a[0])):  # traversing through columns of input matrix a
            result[y][x] = a[x][y]    # assign ij th element of a to ji th element of result
    return result
    
l = [[1,2,3],
       [4,5,6], [7,8,9]]   
print(transpose(l))        
