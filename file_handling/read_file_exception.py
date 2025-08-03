# Gestione eccezioni

try:
    # utilizzo il blocco "with" in modo che sarà lui a chiudere il file automaticamente
    # file in modalità LETTURA
    with open("file.txt", "r") as file:
        contenuto = file.read()
        if not file:
            print("File vuoto")
        else:
            print(contenuto)
except FileNotFoundError:
    print("File non trovato")
except PermissionError:
    print("Accesso al file negato")
except Exception as e:
    print("Errore: ", e)