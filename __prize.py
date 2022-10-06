def calculator(tries, guessed):
    if not guessed:
        tries += 1
        return tries
    else:
        points = 100 * (tries ** (-(tries/45)))

        if points == 100:
            return (print(f'Ottimo lavoro, l\'hai azzeccato hai ottenuto {points} punti con {tries} tentativi!!'))
        elif points >= 85 and points < 100:
            return (print(f'Ottimo, quasi impeccabile hai ottenuto {points} punti con {tries} tentativi!!'))
        elif points >= 70 and points < 85:
            return (print(f'Comlimenti, te la sei cavata piuttosto bene hai ottenuto {points} punti con {tries} tentativi!'))
        elif points >= 40 and points < 70:
            return (print(f'Bravo, anche se ci è voluto un po\' alla fine ce l\'hai fatta hai ottenuto {points} punti con {tries} tentativi!'))
        elif points > 0 and points < 40:
            return (print(f'Direi che si può migliorare... hai ottenuto {points} punti con {tries} tentativi.'))
        else:
            return (print(f'Questo gioco non fa decisamente al caso tuo... hai ottenuto {points} punti con {tries} tentativi.'))
