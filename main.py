from matplotlib import pyplot as plt
import numpy as np
import math

#? Vector definieren
class Vector():#* Het maken van deze class is niet noodzakelijk, aangezien drie losse variabelen (bijv. Bx, By, Bz) ook zou kunnen, 
                #*maar ik vind het wel zo overzichtelijk om die in één object te kunnen stoppen.
    def __init__(self, x, y, z):
        self.x = x 
        self.y = y
        self.z = z

#? Constanten definiëren:
e = 1.602176565 * 10**-19 #C
#*ITER
B_ITER = 0.11 #T (In het echt is  het magneetveld van ITER 11 T, met zo'n sterk veld is de kurkentrekkerbeweging van de deeltjes echter vrijwel niet zichtbaar.)
r_ITER = 6.2 #m (De straal van de plasmadonut in ITER)
T_ITER = 150 * 10**6 #K
Ek = 1.38064878*10**-23 * T_ITER #J (Kinetische energie van een deeltje in het plasma bij 150 miljoen Kelvin)
#* Electron
m_e = 9.10938291 * 10**-31 #kg 
v_e = Vector(math.sqrt(Ek/m_e), math.sqrt(Ek/m_e), 0.0) #m/s |v_e| = sqrt(sqrt(Ek/m_e)^2 + sqrt(Ek/m_e)^2 + 0^2) = sqrt(2Ek/m_e). Komt voort uit Ek = 1/2mv^2 (i.e. v = sqrt(2Ek/m).
q_e = -e
#* Proton (of H-1-kern)
m_p = 1.672621777 * 10**-27 #kg
v_p = Vector(math.sqrt(Ek/m_p), math.sqrt(Ek/m_p), 0.0) #m/s
q_p = e
#* Deuteriumkern
m_D = 3.344495 * 10**-27 #kg
v_D = Vector(math.sqrt(Ek/m_D), math.sqrt(Ek/m_D), 0.0) #m/s
q_D = 2 * e
#* Tritiumkern
m_T = 5.008267 * 10**-27 #kg
v_T = Vector(math.sqrt(Ek/m_T), math.sqrt(Ek/m_T), 0.0) #m/s
q_T = 3 * e

#? Configuring plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

#? Assen definiëren
ax.set_xlim3d([-r_ITER, r_ITER])
ax.set_xlabel('x (m)')

ax.set_ylim3d([-r_ITER, r_ITER])
ax.set_ylabel('y (m)')

ax.set_zlim3d([-r_ITER, r_ITER])
ax.set_zlabel('z (m)')


#? Magnetic field
#?Toroïdaal magneetveld
def magneticFieldTor(baseValue, px, py): #* Magnetisch veld neemt met 1/r af.
    r = math.sqrt(px**2 + py**2)
    B = Vector(
        -baseValue * py/r * 1/r, 
        baseValue * px/r * 1/r,  
        0
        ) 
    return B
#? Lineair magneetveld
def magneticFieldLin(baseValue, py):
    B = Vector(baseValue * 1/(py+1), 0, 0) #* Magnetisch veld neemt met 1/r af in de y-richting.
    return B

#? Particles
def renderParticle(startx: float, starty: float, startz: float, startv: Vector, q: float, m: float, colour: str, dt: float, tmax: float):
    
    #? matplotlib heeft numpy arrays nodig om het figuurtje te kunnen plotten:
    pxArray = np.empty(int(round(tmax/dt,0))) 
    pyArray = np.empty(int(round(tmax/dt,0)))
    pzArray = np.empty(int(round(tmax/dt,0)))

    #? Een aantal variabelen definiëren zodat dat niet elke keer opnieuw in de loop gebeurt.
    px = startx
    py = starty
    pz = startz

    v = startv

    Flor = Vector(None, None, None)

    #? Loop:
    t = 0 #s
    while round(t,30) < tmax: #* t wordt afgerond op 3 decimalen om floating point errors te voorkomen.
        #? Coördinaten van de iteratie toeveogen aan de lijst.
        pxArray[int(round(t/dt, 0))] = px 
        pyArray[int(round(t/dt, 0))] = py
        pzArray[int(round(t/dt, 0))] = pz

        #? Magneetveld en Lorentzkracht
        B = magneticFieldTor(B_ITER, px, py)
        #B = magneticFieldLin(B_ITER, py)
        
        Flor.x = q * (v.y*B.z - v.z*B.y) #* Uitproduct om de Lorentzkracht te berekenen met Flor = q * v x B
        Flor.y = q * (v.z*B.x - v.x*B.z)
        Flor.z = q * (v.x*B.y - v.y*B.x)


        v.x += Flor.x/m * dt #* v = a * dt; a = F/m 
        v.y += Flor.y/m * dt 
        v.z += Flor.z/m * dt

        px += v.x * dt #* x = v * dt
        py += v.y * dt 
        pz += v.z * dt

        #? Elke paar iteraties een update printen
        if round(t*10000000, 5)%10 == 0:
            print(f"t={t}s. || B: {math.sqrt(B.x**2 + B.y**2)}T. || v: {math.sqrt(v.x**2+v.y**2+v.z**2)}m/s. || x: {round(px,5)}m; y: {round(py,5)}m; z: {round(pz,5)}m.")
        #? Volgende tijdsstap (i.e. volgende iteratie van de loop).
        t += dt
    
    #? De functie om te plotten aanroepen.
    ax.plot3D(pxArray, pyArray, pzArray, colour)

#? Het aanroepen van de renderfunctie.
# Het aanpassen van de sterkte van het magneetveld kan worden gedaan in regel 16. Toroïdaal/linear kan worden aangepast in regel 93/94.
#? TOROÏDAAL VELD:
#* Electron; B_ITER = 0.004 T is het beste voor de visualisatie.
#renderParticle(0.0, 4.0, 0.0, v_e, q_e, m_e, "green", 0.00000000002, 0.0000008) 
#* Tritium; B_ITER = 0.11 T is het beste voor de visualisatie.
renderParticle(4.0, 0.0, 0.0, v_T, q_T, m_T, "red", 0.0000000001, 0.000060)
#* Deuterium; B_ITER = 0.11 T is het beste voor de visualisatie.
#renderParticle(-4.0, 0.0, 0.0, v_D, q_D, m_D, "blue", 0.0000000001, 0.000048)
#* Proton; B_ITER = 0.11 T is het beste voor de visualisatie.
renderParticle(4.0, 0.0, 0.0, v_p, q_p, m_p, "purple", 0.0000000001, 0.000024)

#? LINEAR VELD:
#* Electron; B_ITER = 0.002 T is het beste voor de visualisatie.
#renderParticle(-6.0, 0.0, 0.0, v_e, q_e, m_e, "green", 0.00000000002, 0.0000008) 
#* Tritium; B_ITER = 0.05 T is het beste voor de visualisatie.
#renderParticle(-6.0, 0.0, 4.0, v_T, q_T, m_T, "red", 0.0000000001, 0.000048)
#* Deuterium; B_ITER = 0.05 T is het beste voor de visualisatie.
#renderParticle(-6.0, 0.0, 0.0, v_D, q_D, m_D, "blue", 0.0000000001, 0.000048)
#* Proton; B_ITER = 0.5 T is het beste voor de visualisatie.
#renderParticle(-6.0, 0.0, -4.0, v_p, q_p, m_p, "purple", 0.0000000001, 0.000048)


plt.show()