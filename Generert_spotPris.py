import numpy as np
import matplotlib.pyplot as plt
def spotpris_gjennomsnitt(dag, P_snitt=45, amplitude=25, faseforskyvning=-61): #gjennomsnittlig spotpris for dagen i året
    # Beregner spotpris som en funksjon av dag i året
    return P_snitt + amplitude * np.sin((2 * np.pi / 365) * (dag - faseforskyvning))



def spotpris_dagen(t, T, gjennomsnitt): #generering av spotpriser iløpet av dagen som har topper klokken 14:00 og 19:00
     

    spotpris_dagen = []
    for i in range(len(t)):
        if(i==0):
                mue=0
        else:
            mue = 1/(min(abs(t[i]-8), abs(t[i]-19))+1)*0.6
        
        if(T<15):
            mue*=(15-T)*0.2
        random_avvik = np.random.normal(mue, 0.08)
        spotpris_dagen.append(random_avvik)


    return np.array(spotpris_dagen) + gjennomsnitt/2


def spotpris(t, T, dag): #spotpris, basert på tid på dagen, temperatur og dagen i året
     gjennomsnitt = spotpris_gjennomsnitt(dag)
     spotpris = spotpris_dagen(t, T, gjennomsnitt)
     return spotpris

# tid = np.linspace(0,24,24)
# temperatur = 0
# gjennomsnitt = 1
# plt.plot(tid, spotpris_dagen(tid, temperatur, gjennomsnitt))
# plt.show()