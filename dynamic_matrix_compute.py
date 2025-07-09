p = [30,35,15,5,10,20,25]
m = []
s = []

def Matrix_Chain_Order(p):
    n = len(p)
    for i in range(1,n):
        m[i,i] = 0
    for l in range(2,n):
        for i in range(1,n-l+1):
            j = i+l-1
            m[i,j]=inf
            for k in range(i,j-1):
                q = m[i,k] + m[k+1,j] + p[i-1]*p[k]*p[j]
                if (q<m[i,j]):
                    m[i,j] = q
                    s[i,j] = k
    return m, s

def Print_Optimal_Parens(s,i,j):
    if (i == j):
        print("A"+i+" ")
    else:
        print("(")
        Print_Optimal_Parens(s,i,s[i,j])
        Print_Optimal_Parens(s,s[i,j]+1,j)
        print(")")
