import random

# Proprietà
lista_mosse = ["SASSO", "CARTA", "FORBICE"]
gioca_ancora = "SI"

while gioca_ancora in ["SI", "S"]:

    # Chiede all' autente di inserire la sua scelta
    # replace rimuove gli eventuali spazi bianchi inseriti dall' utente
    mossa_scelta = input("Inserisci la tua scelta tra SASSO, CARTA, FORBICE: ").upper().replace(" ", "")

    while mossa_scelta not in lista_mosse:
        mossa_scelta = input("Scelta non valida. Riprova: ").upper().replace(" ", "")

    # Scelta casuale tra le mosse disponibili nella lista
    mossa_cpu = random.choice(lista_mosse)  # IN ALTERNATIVA avremmo potuto usare lista_mosse[random.randint(0, len(lista_mosse) - 1)]


    # Mostra le scelte
    print("hai scelto", mossa_scelta, ", lui ha scelto", mossa_cpu)

    # Logica di gioco
    if(mossa_scelta == mossa_cpu):
        print("Avete pareggiato")
    elif (mossa_scelta == "SASSO" and mossa_cpu == "FORBICE"):
        print("Hai vinto")
    elif (mossa_scelta == "CARTA" and mossa_cpu == "SASSO"):
        print("Hai vinto")
    elif (mossa_scelta == "FORBICE" and mossa_cpu == "CARTA"):
        print("Hai vinto")
    else:
        print("Hai perso")

    gioca_ancora = input("Vuoi gioca ancora? ").upper().replace(" ", "")

else:
    print("Grazie per aver giocato!")