def Biseccion(xi,xf,ea):

    primerxr = ((xi + xf) / 2)
    primerfxr = f(primerxr)  # f(xr)
    primerfxi = f(xi)  # f(xi)
    primerfxixfxr = primerfxi * primerfxr  # f(xi)*f(xr)
    y = primerfxixfxr
    primererrora=100
    if primerfxixfxr < 0:
        primervacafxixfxr = "-"
    else:
        vacafxixfxr = "+"
    primerfxixfxr = vacafxixfxr
    print('_________________________________________________')
    print('=================================================')
    print("xi=", "{:.6f}".format(xi), "|| xf=", "{:.6f}".format(xf),
          "|| xr=", "{:.6f}".format(primerxr), "|| f(xi)=",  "{:.6f}".format(primerfxi),
          "|| f(xr)=", "{:.6f}".format(primerfxr), "|| f(xi)*f(xr)=", (primerfxixfxr),
          "|| ea =", "{:.6f}".format(primererrora))
    xrvieja = primerxr
    errora = primererrora

    xrtemp=xrvieja
    xitemp=xi
    xftemp=xf
    xr=xrvieja
    while ea<=errora:
        xi=xitemp
        xf=xftemp

        if y >= 0:
            xi = xrtemp
        else:
            xi = xi
        if y <= 0:
            xf = xrtemp
        else:
            xf = xf

        xr = ((xi + xf) / 2)
        fxr=f(xr)       #f(xr)
        fxi=f(xi)       #f(xi)
        fxixfxr = fxi*fxr   #f(xi)*f(xr)
        y = fxixfxr
        if fxixfxr<0:
            vacafxixfxr="-"
        else:
            vacafxixfxr= "+"
        fxixfxr = vacafxixfxr

        errora = abs(((xr - xrtemp) / xr) * 100)
        print("xi=", "{:.6f}".format(xi), "|| xf=", "{:.6f}".format(xf), "|| xr=", "{:.6f}".format(xr), "|| f(xi)=","{:.6f}".format(fxi), "|| f(xr)=", "{:.6f}".format(fxr), "|| f(xi)*f(xr)=", (fxixfxr), "|| ea =","{:.6f}".format(errora))

        if y >= 0:
            xitemp=xr
        else:
            xitemp=xi

        if y <= 0:
            xftemp=xr
        else:
            xftemp=xf
        xrtemp=xr

    print("_________________________________________________")
    print('                  Terminamos                     ')

def main():

    xi = float(input("Ingrese xi ="))
    xitemp = xi
    xf = float(input("Ingrese xf ="))
    xftemp = xf
    ea = float (input("Ingrese ea  ="))

    Biseccion (xi,xf,ea)

def f(x):

    fx = (9 * (x * x * x * x)) + (18 * (x * x * x)) + (38 * (x * x)) - (57 * x) + 14
    return fx

main()


