#!/usr/bin/env python3
# Semplice script per imparare il codice deontologico del biologo
# Il programma chiede o il numero dell'articolo con titolo corrispondente, o il titolo dell'articolo con numero corrispondente, e restituisce la risposta corretta.

import random

# Dizionario contenente gli articoli del codice deontologico del biologo
codice_deontologico = {
    1: "Ambito Applicativo",
    2: "Doveri Generali e Professionalità Specifica",
    3: "Rapporti Esterni e Privati",
    4: "Obblighi nei confronti della Professione",
    5: "Lealtà e Correttezza",
    6: "Indipendenza",
    7: "Riservatezza",
    8: "Competenza e Diligenza",
    9: "Aggiornamento Professionale",
    10: "Verità",
    11: "Legalità e comunicazione di misure penali all'ONB",
    12: "Doveri nei confronti dell'ONB",
    13: "Società tra biologi",
    14: "Rapporti con i Clienti/Committenti",
    15: "Rapporti con Istituzioni e Terzi. Conflitti di Interesse",
    16: "Partecipazione a Commissioni e Giurie di Concorso",
    17: "Cariche Istituzionali",
    18: "Partecipazione a Campagne Elettorali",
    19: "Rapporti con i Colleghi",
    20: "Concorrenza Sleale",
    21: "Rapporti con Collaboratori e Dipendenti",
    22: "Rapporti con Tirocinanti",
    23: "Incarico Professionale",
    24: "Contratti e Compensi",
    25: "Accettazione dell'Incarico",
    26: "Incarico Congiunto",
    27: "Esecuzione dell'Incarico",
    28: "Cessazione dell'Incarico",
    29: "Rinuncia dell'Incarico",
    30: "Inadempimento",
    31: "Conflitto di Interessi",
    32: "Interferenza tra Interessi Economici e Professione",
    33: "Restituzione dei Documenti",
    34: "Responsabilità Patrimoniale e Polizza Assicurativa",
    35: "Informativa",
    36: "Pubblicità informativa",
    37: "Aggiornamento del Codice Deontologico",
    38: "Entrata in Vigore Formazione Obbligatoria in Materia Deontologica"
}

# Raggruppa gli articoli nei titoli corrispondenti
articoli_per_titolo = {
    "Titolo I - Principi generali": list(range(1, 12)),
    "Titolo II - Rapporti con l'Ordine e la Federazione": [12],
    "Titolo III - Rapporti esterni": list(range(13, 19)),
    "Titolo IV - Rapporti interni": list(range(19, 23)),
    "Titolo V - Esercizio professionale": list(range(23, 37)),
    "Titolo VI - Disposizioni transitorie e finali": [37, 38],
}

# Funzione per ottenere un articolo casuale
def get_random_article(article_numbers):
    article_number = random.choice(article_numbers)
    article_title = codice_deontologico[article_number]
    return article_number, article_title

# Funzione per ottenere il numero dell'articolo dato il titolo
def get_article_number(title):
    for number, article_title in codice_deontologico.items():
        if article_title.lower() == title.lower():
            return number
    return None

# Funzione per ottenere il titolo dell'articolo dato il numero
def get_article_title(number):
    return codice_deontologico.get(number, None)

# Funzione principale del programma
def main():
    print("Digita 'exit' per uscire dal programma.\n")

    titoli = list(articoli_per_titolo)
    print("Scegli su quale titolo concentrarti:")
    for index, titolo in enumerate(titoli, start=1):
        print(f"{index}. {titolo}")
    print("0. Tutti gli articoli")

    while True:
        scelta = input("Inserisci il numero del titolo o 0 per tutti: ").strip().lower()

        if scelta == "exit":
            print("Bye!")
            return

        if scelta == "0":
            articoli_selezionati = list(codice_deontologico)
            break

        if scelta.isdigit() and 1 <= int(scelta) <= len(titoli):
            articoli_selezionati = articoli_per_titolo[titoli[int(scelta) - 1]]
            break

        print("Scelta non valida. Inserisci il numero di un titolo o 0 per tutti.")

    while True:
        article_number, article_title = get_random_article(articoli_selezionati)
        asks_for_number = random.choice([True, False])

        if asks_for_number:
            user_input = input(
                f"{article_title} - inserisci il numero: "
            ).strip()
        else:
            user_input = input(
                f"art {article_number}: inserisci il titolo: "
            ).strip()

        if user_input.lower() == 'exit':
            print("Bye!")
            break

        if asks_for_number:
            if user_input.isdigit() and int(user_input) == article_number:
                print("Risposta corretta!\n")
            else:
                print(f"Risposta errata. Il numero corretto è {article_number}.\n")
        else:
            if user_input.lower() == article_title.lower():
                print("Risposta corretta!\n")
            else:
                print(f"Risposta errata. Il titolo corretto è: {article_title}.\n")

if __name__ == "__main__":
    main()
