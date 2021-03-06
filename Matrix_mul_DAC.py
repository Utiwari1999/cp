# import numpy as np

def reshape(arr,x,y):
    ark = []
    for i in arr:
        ark.append(i[x:y])
    return ark 

def add(arr,arr1,a,b):
    for i in range(a):
        for j in range(b):
            arr[i][j] =arr[i][j]+arr1[i][j]
    return arr

def col_add(arr,arr1,a,b):
    for i in range(a):
        for j in range(b):
            arr[i].append(arr1[i][j])
    return arr 

def row_add(arr,arr1,a,b):
    for i in range(a):
        arr.append(arr1[i])
    return arr


def mod_mat(arr,arr1,n):
    if n==1:
        arr3 = [[0 for _ in range(1)]for _ in range(1)]
        arr3[0][0] = arr[0][0]*arr1[0][0] 
        return arr3
    j = n//2
    temp = arr[:j]
    a = reshape(temp,0,j)
    b = reshape(temp,j,n)
    temp = arr[j:]
    c = reshape(temp,0,j)
    d = reshape(temp,j,n)
    # print(a)
    # print(b)
    # print(c)
    # print(d)
    temp = arr1[:j]
    e = reshape(temp,0,j)
    f = reshape(temp,j,n)
    temp = arr1[j:]
    g = reshape(temp,0,j)
    h = reshape(temp,j,n)
    # print(e)
    # print(f)
    # print(g)
    # print(h)
    ae = mod_mat(a,e,j)
    print(f"ae ={ae}")
    bg = mod_mat(b,g,j)
    print(f'bg = {bg}')
    af = mod_mat(a,f,j)
    print(f'af =  {af}')
    bh = mod_mat(b,h,j)
    print(f'bh = {bh}')
    ce = mod_mat(c,e,j)
    print(f'ce = {ce}')
    dg = mod_mat(d,g,j)
    print(f'dg= {dg}')
    cf = mod_mat(c,f,j)
    print(f'cf = {cf}')
    dh = mod_mat(d,h,j)
    print(f'dh = {dh}')
    
    p1 = add(ae,bg,len(ae),len(ae[0]))
    p2 = add(af,bh,len(af),len(af[0]))
    p3 = add(ce,dg,len(ce),len(ce[0]))
    p4 = add(cf,dh,len(cf),len(cf[0]))
    # print(f'p1 = {p1}')
    # print(f'p2 = {p2}')
    # print(f'p3 = {p3}')
    # print(f'p4 = {p4}')
    # firstly we are combining the p1 and p2 by column
    first = col_add(p1,p1,len(p1),len(p1[0]))
    # print(f'first = {first}')
    # then we are combining the p3 and p4 by column
    second = col_add(p3,p2,len(p3),len(p3[0])
    matrix = row_add(first,second,len(first),len(first[0]))    
    print(matrix)
    return matrix

# arr5 = np.array([[5, 0, 1, 2], 
#                 [0, 5, 2, 1], 
#                 [3, 5, 4, 1],
#                 [5, 0, 4, 1]])

# arr = [[5, 0, 1, 2], 
#                 [0, 5,2, 1], 
#                 [3, 5,4, 1],
#                 [5, 0,4, 1]]
# arrm = np.array([[5, 0, 1, 2], 
#                 [0, 5,2, 1], 
#                 [3, 5,4, 1],
#                 [5, 0,4, 1]])
# ar = [[1,20],[3,4]]

# print(mod_mat(arr,arr,4))
# print(arrm.dot(arrm))
