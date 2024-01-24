from tkinter import *

def beregn_boligkjop():
    #Dokumentavgift, egenkapital i prosent, og faktor
    dokumentavgift = 2.5
    ek_prosent = 15
    faktor = 5.0

    #Henter egenkapital og bruttoinntekt
    egenkapital = int(ek.get())
    bruttoinntekt = int(bi.get())

    #Inndata for antall barn og sivilstatus
    antall_barn = int(barn.get())
    sivil_status=int(siv_status.get())

    #Beregner barnefradraget utifra sivil statusen
    if sivil_status==1:
       barnesats = 785000
    else:
       barnesats = 370000

    barnefradrag = barnesats*antall_barn 

    #Beregner makslån med barnefradrag fratrekket
    makslan_ink_fratrekk = (faktor*bruttoinntekt)-barnefradrag

    #Beregner maks kjøp og lån inkludert egenkapital, egenkapital prosenten, og dokumentavgiften
    makskjop_ink_dok = makslan_ink_fratrekk+egenkapital
    makslanogkjop_ink_ek = egenkapital*100/(dokumentavgift+ek_prosent)
    egenkapital_rest = makslanogkjop_ink_ek*ek_prosent/100
    makslan_ink_ek = makslanogkjop_ink_ek-egenkapital_rest
    makskjop_brutto = makskjop_ink_dok/1.025

    #Sjekker maks inntekt opp mot maks lånebeløpet, det gis tilbakemelding ved negativ verdi/resultat
    if makslan_ink_fratrekk<=makslan_ink_ek:
        makslan = makslan_ink_fratrekk
        if makskjop_brutto<=0:
            maks_ksum.set('Får ikke kjøpe')
        else:
            maks_ksum.set(format(makskjop_brutto, '.0f'))
        if makslan<=0:
            maks_lbelop.set('Får ikke lån')
        else:        
            maks_lbelop.set(format(makslan, '.0f'))

    else:
        makslan = makslan_ink_ek
        if makslan<=0:
            maks_ksum.set('Får ikke kjøpe')
        else:
            maks_ksum.set(format(makslanogkjop_ink_ek, '.0f'))
        if makslanogkjop_ink_ek<=0:
            maks_lbelop.set('Får ikke lån')
        else:
            maks_lbelop.set(format(makslan, '.0f'))

window=Tk()

#Navnet på vinduet
window.title('Lånekalkulator')

#Ledetekster for egenkapital, bruttoinntekt, antall barn, sivil status, maks kjøpesum, og max lånebeløp
lbl_ek=Label(window, text='Egenkapital:')
lbl_ek.grid(row=0, column=0, padx=5, pady=5, sticky=E)

lbl_bi=Label(window, text='Bruttoinntekt:')
lbl_bi.grid(row=1, column=0, padx=5, pady=5, sticky=E)

lbl_barn=Label(window, text='Antall barn:')
lbl_barn.grid(row=2, column=0, padx=5, pady=5, sticky=E)

lbl_siv_status=Label(window, text='Sivil status:')
lbl_siv_status.grid(row=3, column=0, padx=5, pady=5, sticky=E)

lbl_maks_ksum=Label(window, text='Maks kjøpesum:')
lbl_maks_ksum.grid(row=6, column=0, padx=5, pady=5, sticky=E)

lbl_maks_lbelop=Label(window, text='Maks lånebeløp:')
lbl_maks_lbelop.grid(row=7, column=0, padx=5, pady=5, sticky=E)

#Inndatafelt for egenkapital og bruttoinntekt
ek=StringVar()
ent_ek=Entry(window, width=10, textvariable=ek)
ent_ek.grid(row=0, column=1, padx=5, pady=5, sticky=W)

bi=StringVar()
ent_bi=Entry(window, width=10, textvariable=bi)
ent_bi.grid(row=1, column=1, padx=5, pady=5, sticky=W)

#Inndatafelt for antall barn med en "spinbox"
ant_barn=IntVar()
barn = Spinbox(window, from_=0, to=3, width=5, textvariable=ant_barn)
barn.grid(row=2, column=1, padx=5, pady=5, sticky=W)

#Inndatafelt for sivilstatus (Enslig/toinntekts familie) med en "radio knapp"
siv_status=IntVar()
enslig = Radiobutton(window, text='Enslig', value=1, variable=siv_status)
enslig.grid(row=3, column=1, padx=1, pady=5, sticky=W)

toinntekt = Radiobutton(window, text='Toinntekt', value=2, variable=siv_status)
toinntekt.grid(row=4, column=1, padx=1, pady=5, sticky=W)

#Utdatafelt for resultatet maks kjøpesum og lånebeløp
maks_ksum=StringVar()
ent_maks_ksum=Entry(window, width=15, state='readonly', textvariable=maks_ksum)
ent_maks_ksum.grid(row=6, column=1, padx=15, pady=5, sticky=W)

maks_lbelop=StringVar()
ent_maks_lbelop=Entry(window, width=15, state='readonly', textvariable=maks_lbelop)
ent_maks_lbelop.grid(row=7, column=1, padx=15, pady=5, sticky=W)

#Knapp for beregning
btn_beregn=Button(window, text='Beregn', command=beregn_boligkjop)
btn_beregn.grid(row=5, column=1, padx=15, pady=20, sticky=E)

#Knapp for å avslutte
btn_avslutt=Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=8, column=0, columnspan=2, padx=15, pady=10, sticky=E)

window.mainloop()
