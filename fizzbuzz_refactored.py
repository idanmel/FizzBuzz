def play():
    game = []
    for i in range(1, 101):
        next_move = ''
        if i % 3 == 0:
            next_move += 'Fizz'
        if i % 5 == 0:
            next_move += 'Buzz'

        if not next_move:
            next_move = str(i)

        game.append(next_move)

    return '\n'.join(game)


if __name__ == '__main__':
    print(play())
