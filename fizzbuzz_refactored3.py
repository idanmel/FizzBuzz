def apply_logic(num):
    rules = [
        (num % 3 == 0, 'Fizz'),
        (num % 5 == 0, 'Buzz'),
    ]
    results = [word for predicate, word in rules if predicate]
    output = ''.join(results)

    if not output:
        output = str(num)

    return output


if __name__ == '__main__':
    moves = range(1, 101)
    game = (apply_logic(move) for move in moves)
    print('\n'.join(game))

