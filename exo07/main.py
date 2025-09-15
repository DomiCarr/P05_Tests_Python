# Écrivez votre code ici !
def square(val):
    try:
        val = float(val)
        print(f"val: {val}")
        return val * val
    except ValueError:
        print("Le paramètre doit être un nombre !")
        return None


val = input("Donnez un nombre : ")
print(f"val: {val} carré: {square(val)}")