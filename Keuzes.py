from rich import table
from rich import console
import sys
import subprocess
import os



def keuzes():
    while True:
        print("Welke keuze wil je maken ?")
        keuze = input("[1] Server toevoegen\n"
                      "[2] Server Verwijderen\n"
                      "[3] Server lijst tonen\n"
                      "[0] Stoppen\n")
        match keuze:
            case "1":
                print("Server toevoegen")
            case "2":
                print("Server verwijderen")
            case "3":
                print("Lijst vertonen")
            case "0":
                print("Programma stoppen")
                exit()
            case _:
                print("Foutmelding, foute ingave")
        



                    

