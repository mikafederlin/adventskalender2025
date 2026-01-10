# 🎄 Tag 24: DAS FINALE
import time

print("Systeme fahren hoch...")

# Aufgabe 1: Frage nach dem Namen des Piloten und speichere ihn in 'pilot' (input).

pilot=input("name? ")
# (Erinnerung an Tag 11: f-String für den Namen!)
print(f"Hallo Captain {pilot}. Startsequenz eingeleitet.")

# Aufgabe 2: Schreibe einen Countdown von 3 bis 1.
# (Erinnerung an Tag 16: for ... in range(...): )
# Vergiss nicht das time.sleep(1) zwischen den Zahlen!
for zahl in range(3,0,-1):
    print(zahl)
    time.sleep(1)
# Aufgabe 3: Gib den finalen Start-Befehl und "Frohe Weihnachten" aus!

print("FROHE WEINACHTEN!!!!!!")