def SynchronizingTables(N, ids, salary):
    idsS = [] 
    salS = []
    idsNoSort = []
    k = 0
    resSal = [] 
    ids_sort = [0]*N
    sal_sort = [0]*N
    
    for i in range(N):
        ids_sort[i] = ids[i]
        sal_sort[i] = salary[i] 
    ids_sort.sort()
    sal_sort.sort()
    
    for i in range(N):
        x = []
        y = []
        x1 = []
        for j in range(2):
            if j%2 == 0:        
                x.append(ids_sort[i])
                y.append(sal_sort[i])
                x1.append(ids[i])
            else:
                x.append(i)
                y.append(i)
                x1.append(i)
        
        idsS.append(x)
        salS.append(y)
        idsNoSort.append(x1)
    
    for i in range(N):
        k = idsNoSort[i][0]   
        for j in range(N):
            if k == idsS[j][0]:
                indx = idsS[j][1]     
                if indx == salS[j][1]:
                    resSal.append(salS[j][0])
    
    return resSal  


   
