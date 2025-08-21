heure= int(input("Entrez l'heure(0-23): "))
if heure == 12:
    print("Il est midi")
elif 0 <= heure < 12:
    print("Il est le matin")
elif 13 <= heure < 18:
    print("Il est l'après-midi")
elif 18 <= heure < 23:
    print ("Il est le soir") 
else:
    print("Heure invalide")
