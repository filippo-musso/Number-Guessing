def giver(number, guess):
    if guess < number:
        if number % 2 == 0:
            if number % guess == 0:
                return (print(f'Riprova... è un multiplo di {guess} e di 2, ma maggiore di {guess}!'))
            return (print(f'Riprova... è un multiplo di 2, ma maggiore di {guess}!'))
        elif number % 3 == 0:
            if number % guess == 0:
                return (print(f'Riprova... è un multiplo di {guess} e di 3, ma maggiore di {guess}!'))
            return (print(f'Riprova... è un multiplo di 3, ma maggiore di {guess}!'))
        else:
            return (print(f'Riprova... è maggiore di {guess}'))
    else:
        if number % 2 == 0:
            if number % guess == 0:
                return (print(f'Riprova... è un multiplo di {guess} e di 2, ma minore di {guess}!'))
            return (print(f'Riprova... è un multiplo di 2, ma minore di {guess}!'))
        elif number % 3 == 0:
            if number % guess == 0:
                return (print(f'Riprova... è un multiplo di {guess} e di 3, ma minore di {guess}!'))
            return (print(f'Riprova... è un multiplo di 3, ma minore di {guess}!'))
        else:
            return (print(f'Riprova... è minore di {guess}'))
