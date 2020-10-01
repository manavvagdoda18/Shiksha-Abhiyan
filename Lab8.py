def pro(s,i,j):
    if(i==j):
        print("A{}".format(i),end="")
    else:
        print("(",end="")
        pro(s,i,s[i][j])
        pro(s,s[i][j]+1,j)
        print(")",end="")
p=[5,10,3,12,5,50,6]
n=len(p) 
m = [[0 for x in range(n)] for x in range(n)] 
s=[[0 for x in range(n)] for x in range(n)]  
   
for i in range(1, n): 
    m[i][i] = 0
  
# L is chain length. 
for L in range(2, n): 
    for i in range(1, n-L + 1): 
        j = i + L-1
        m[i][j] =100000 
        for k in range(i, j): 
          
        
            q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j] 
            if q < m[i][j]: 
                m[i][j] = q 
                s[i][j]=k    
print("Product Matrix:")
for i in m:
    print(i)
    
print("\nFor parenthesis:")
for i in s:
    print(i)
    
pro(s,1,n-1)   
            
            
    
    
