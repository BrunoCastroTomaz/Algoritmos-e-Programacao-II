def fatorial (n):
    x = 1
    while n>1:
        x*=n
        n-=1
    return x
def combinacao(m,n):
    a = fatorial(m)
    b = fatorial(m-n)
    c = fatorial(n)
    d = a /(b*c)
    return d
def main():
    m= int(input())
    n= int(input())
    print(combinacao(m,n))

main()
