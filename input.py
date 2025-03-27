# zahl1 = input(input("Gib einee Zahl ein: "))
# zahl2 = input(input("Gib eine zweiter Zahl ein: "))
# summe = zahl1 + zahl2
# print("Die Summe ist:", summe)

from getpass import getpass
benutzername = input("Benutzername: ")
kenntwort = getpass("Kennwort: ")

print("Eingegener Benutzername:", benutzername)
print("Eingegebenes Kennwort:", kenntwort)
