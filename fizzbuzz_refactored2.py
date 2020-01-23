def apply_logic(num):
    output = ''
    if num % 3 == 0:
        output += 'Fizz'
    if num % 5 == 0:
        output += 'Buzz'

    if not output:
        output = str(num)

    return output


if __name__ == '__main__':
    moves = range(1, 101)
    game = (apply_logic(move) for move in moves)
    print('\n'.join(game))
