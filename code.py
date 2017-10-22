import sys
 
def matrix_chain_dynamic(p, n):
    m = [[0 for x in range(n)] for x in range(n)]

    for i in range(1, n):
        m[i][i] = 0         #diagonal of matrix is 0 
    
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = float("inf")
            for k in range(i, j):               
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]       
                display_dynamic(i,j,k, m[i][k], m[k+1][j], p[i-1]*p[k]*p[j], p[i-1], p[k], p[j], q)
                if q < m[i][j]:
                    m[i][j] = q
            print("Chose minimum: " + str(m[i][j]))
            print("**********************")  
 
    return m[1][n-1]
def matrix_chain_capulet(p, n):
    m = [[0 for x in range(n)] for x in range(n)]

    for i in range(1, n):
        m[i][i] = 0         #diagonal of matrix is 0 
    
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = float("inf")
            for k in range(i, j):               
                q = p[i-1]*p[k]*p[j]       
                display_capulet(i,j,k, p[i-1], p[k], p[j], q)
                if q < m[i][j]:
                    m[i][j] = q
            print("Chose minimum: " + str(m[i][j]))
            print("**********************")  
 
    return m[1][n-1]

def display_dynamic(i,j,k, firstValue, secondValue, thirdValue, p0, p1, p2, finalValue):
    print('m[%(i)s,%(j)s] = m[%(i)s][%(k)s] + m[%(k+1)s][%(j)s] + p[%(i-1)s]*p[%(k)s]*p[%(j)s]' % {'i': i, "j": j, "k" : k, "k+1" : k+1, "i-1" : i-1})    
    print('       = %(firstValue)s + %(secondValue)s + %(p0)s*%(p1)s*%(p2)s' % {'firstValue' : firstValue, 'secondValue' : secondValue,
                                                                                            "p0" : p0, "p1" : p1, "p2" : p2} )
    print('       = %(firstValue)s + %(secondValue)s + %(thirdValue)s' % {'firstValue' : firstValue, 'secondValue' : secondValue, 'thirdValue' : thirdValue})
    print('       = %(finalValue)s' % {'finalValue' : finalValue})
def display_capulet(i,j,k, p0, p1, p2, finalValue):
    print('m[%(i)s,%(j)s] = p[%(i-1)s]*p[%(k)s]*p[%(j)s]' % {'i': i, "j": j, "k" : k, "i-1" : i-1})
    print('       = %(p0)s*%(p1)s*%(p2)s' % {"p0" : p0, "p1" : p1, "p2" : p2})
    print('       = %(finalValue)s' % {'finalValue' : finalValue})

arr = [3,6,9,4,2]
size = len(arr)
 
minimum_dynamic = str(matrix_chain_dynamic(arr, size))
minimum_capulet = str(matrix_chain_capulet(arr, size))
print("Minimum number of multiplications using dynamic approach is " + minimum_dynamic)
print("Minimum number of multiplications using Capulet approach is " + minimum_capulet)