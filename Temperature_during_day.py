import numpy as np
import matplotlib.pyplot as plt



theta = 2*np.pi/3 #faseforskyvning, maksimal temperatur inntreffer ca 14:00

def temperatur_avvik(dag_i_aret):
    """
    Returnerer estimert avvik mellom maksimal og minimal temperatur for en gitt dag i året.
    dag_i_aret: Heltall (1-365), representerer dagen i året hvor 1 = 1. januar, 365 = 31. desember.
    Returnerer avvik i grader Celsius.
    """
    # Parametre for sinuskurven:
    # Maksimalt avvik (f.eks. 10 grader på de varmeste dagene)
    maks_avvik = 10
    # Minimalt avvik (f.eks. 3 grader på de kaldeste dagene)
    min_avvik = 3
    # Gjennomsnittlig avvik
    gjennomsnitt_avvik = (maks_avvik + min_avvik) / 2
    # Amplitude (halvparten av differansen mellom maks og min)
    amplitude = (maks_avvik - min_avvik) / 2
    # Beregning av avvik som funksjon av dagen i året
    # Bruk en sinuskurve som har en periode på 1 år (365 dager)
    avvik = gjennomsnitt_avvik + amplitude * np.sin(2 * np.pi * (dag_i_aret - 172) / 365)
    return avvik


def temperatur(t, dag_i_aret, temp_avg):
    A= temperatur_avvik(dag_i_aret) / 2
    mue = 0
    T = 24*60
    avviks_frekvens = 30
    temp_uten_stoy = A*np.sin(t*2*np.pi/24 - theta) + temp_avg 
    random_avvik_liste = []

    for i in range(T):
        if(i==0):
            mue=0
        else:
            mue = random_avvik_liste[i-1]
        random_avvik = np.random.normal(mue, 0.08)
        random_avvik_liste.append(random_avvik)
    
    return temp_uten_stoy + random_avvik_liste

t = np.linspace(0,24,24*60)

temp_avg = 12
temperatur_ilop_av_dagen = temperatur(t, 200, temp_avg)
# plt.plot(t, temperatur_ilop_av_dagen)
# plt.show()
