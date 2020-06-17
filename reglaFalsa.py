
#Este programa determina una de las raíces reales de la función
#f(x) = (1-0.6x)/x
#Esta funcion lee los valores inicial y final del intervalo de busqueda
#y el error aproximado maximo e invoca a la funcion reglaFalsa para que
#encuentre la raiz
def main():
    print("f(x) = (1-0.6x)/x")
    xi = float(input("Escriba el valor inicial: "))
    xf = float(input("Escriba el valor final: "))
    eam = float(input("Escriba el error aproximado maximo: ")) 
    print()
    reglaFalsa(xi, xf, eam)
    
#Esta funcion recibe como parametro el valor de una abscisa (x) y regresa la
#ordenada (y), esta funcion sera llamada por reglaFalsa cada vez que desee
#obtener el valor de la funcion
def f(x):
    fxi = (1-0.6*x)/x
    print("x: {:.4f}  y: {:.4f}".format(x,fxi))
    
#Esta funcion recibe como parametros valores inicial, final y error aproximado
#maximo. Calcula y despliega los valores de la raiz, el valor de la funcion
#de para esa raiz y el numero de iteraciones requerida pra encontrar la raiz
def reglaFalsa(xi, xf, eam):
    #se calculan las funciones y otros calculos y se empieza un contador en 0
    i = 0
    ea = 100
    fxf = (1-0.6*xf)/xf
    fxi = (1-0.6*xi)/xi
    xr = xi-((xf-xi)/(fxf-fxi))*fxi
    fxr = (1-0.6*xr)/xr
    signo = fxi*fxr
    print("i    xi       xf      f(xi)      f(xf)      xr       f(xr)    f(xi)*f(xr)     ea")
    print("{:d}   {:.4f}   {:.4f}   {:.4f}    {:.4f}    {:.4f}   {:.4f}    {:.4f}".format(i,xi,xf,fxi,fxf,xr,fxr,signo))
    #se usan condicionales para cambiar el valor de xf, xi, o terminar el programa
    if signo < 0:
        xf = xr
    if signo > 0:
        xi = xr
    if signo == 0:
        ea = 0
    xrn = xi-((xf-xi)/(fxf-fxi))*fxi
    i+=1
    #Se crea un while que continua hasta ea ser menor al ea maximo
    while eam < ea:
        fxf = (1-0.6*xf)/xf
        fxi = (1-0.6*xi)/xi
        xr = xi-((xf-xi)/(fxf-fxi))*fxi
        fxr = (1-0.6*xr)/xr
        signo = fxi*fxr
        if signo < 0:
            xf = xr
        if signo > 0:
            xi = xr
        if signo == 0:
            break
        xrn = xi-((xf-xi)/(fxf-fxi))*fxi
        ea = abs((xrn-xr)/xrn)*100
        xr = xrn
        print("{:d}   {:.4f}   {:.4f}   {:.4f}    {:.4f}    {:.4f}   {:.4f}    {:.4f}    {:.4f}".format(i,xi,xf,fxi,fxf,xr,fxr,signo,ea))
        i += 1
    print()
    print("raiz: {:.4f}, funcion(raiz): {:.4f}".format(xr,fxr))
    print()
    print("Desea obtener el valor de la funcion?")
    p = input("Escriba si o no: ")
    if p == "SI" or p == "si":
        x = float(input("Escriba el valor de la abscisa x: "))
        f(x)

#Programa principal
print("Este programa determina una de las raíces reales de la función")
main()
print()
input("Presione enter para salir")