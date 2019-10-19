def apply_logic(num):
    output = ''
    if num % 3 == 0:
        output += 'Fizz'
    if num % 5 == 0:
        output += 'Buzz'

    if not output:
        output = str(num)

    return output


def play():
    moves = range(1, 101)
    game = (apply_logic(move) for move in moves)
    return '\n'.join(game)
