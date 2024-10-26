import numpy as np
import matplotlib.pyplot as plt

# # Definer eksempelparametere
A = 1  # Arealet til solcellepanelet (m²)
eta = 0.2  # Virkningsgrad (effektivitet, typisk mellom 0 og 1)
I0 = 1000  # Maksimal solinnstråling under klare himmelforhold (W/m²)
phi = 60  # Breddegrad (grader)
n = 200  # Dagnummer (1 = 1. januar, 365 = 31. desember)
S = 0.3  # Skyfaktor (andel mellom 0 og 1)
alpha = 0.004  # Temperaturkoeffisient (typisk mellom 0.003 og 0.005 per °C)
T = 10  # Aktuell temperatur (°C)
T0 = 25  # Referansetemperatur, vanligvis 25°C
t = 14  # Tidspunkt på dagen (i 24-timers format, f.eks. 14 for kl. 14:00)


#Beregn deklinasjon (delta)
def solcellepanel_effekt(A, eta, I0, phi, n, S, alpha, T, T0, t): #målt i watt
    delta = 23.44 * np.sin(np.radians((360 / 365) * (n - 81)))

    # Beregn timevinkel (omega)
    omega = 15 * (t - 12)

    # Beregn solhøyde (h)
    h = np.maximum(0,np.degrees(np.arcsin(np.sin(np.radians(phi)) * np.sin(np.radians(delta)) +
                            np.cos(np.radians(phi)) * np.cos(np.radians(delta)) * np.cos(np.radians(omega)))))

    # Endelig formel for estimert effekt (P)
    P = A * eta * I0 * np.sin(np.radians(h)) * (1 - S) * (1 - alpha * (T - T0))

    return P

#print(solcellepanel_effekt(A, eta, I0, phi, n, S, alpha, T, T0, t))

tlist = np.linspace(0,24,60*24)
#print(tlist)

sunlist = solcellepanel_effekt(A, eta, I0, phi, n, S, alpha, T, T0, tlist)

fig, ax = plt.subplots()

# ax.plot(tlist,sunlist)
# print(sunlist)
# plt.show()