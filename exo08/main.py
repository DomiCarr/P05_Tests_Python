def log_decorator(func):
    def display_messages():
        print("Avant la fonction")
        func()
        print("Après la fonction")
    return display_messages


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
