def paire_ou_impaire(nombre):
    if nombre % 2 == 0:
        return f"{nombre} est pair."
    else:
        return f"{nombre} est impair."

# Exemple d'utilisation
if __name__ == "__main__":
    nombre = int(input("Entrez un nombre : "))
    print(paire_ou_impaire(nombre))

