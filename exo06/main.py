# Fonction calculate_average

def calculate_average(numbers):
    tot = 0
    num = 0
    for n in numbers:
        tot = tot + n
        num = num + 1
    moy = tot/num
    print(f"tot: {tot}")
    print(f"moy: {moy}" )
    return moy

# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)






