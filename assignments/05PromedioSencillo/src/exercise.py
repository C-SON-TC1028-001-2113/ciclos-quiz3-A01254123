def main():
    #escribe tu código abajo de esta línea
    n=int(input())
    suma=0
    for i in range(n):
        b=float(input())
        suma=suma+b
    prom=suma/n
    print(prom)
if __name__=='__main__':
    main()
