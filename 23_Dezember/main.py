# 🕯️ Tag 23: Passwort-Schutz

geheimnis = "Zimtstern"
eingabe = ""

# != bedeutet "nicht gleich"

# Aufgabe: Schreibe die while-Schleife.
# Solange 'eingabe' NICHT GLEICH 'geheimnis' ist...
# (Erinnerung an Tag 18: while ...:)

while eingabe!=geheimnis:
    eingabe=input("passwort")
    # Frage den User nach dem Passwort (input) und speichere es in 'eingabe'
    
    # (Optional) Wenn du willst, kannst du prüfen:
    # Wenn eingabe richtig -> "Offen!"
    # Sonst ->F!"

print("Zugriff erlaubt! Tor öffnet sich.")
