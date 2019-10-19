def get_next_state(game_state):
    next_move = ""
    next_num = len(game_state) + 1
    if next_num % 3 == 0:
        next_move += "Fizz"
    if next_num % 5 == 0:
        next_move += "Buzz"

    if not next_move:
        next_move = str(next_num)

    return game_state + (next_move,)


def game_ended(game_state, limit):
    return len(game_state) == limit


def report(s):
    return '\n'.join(s)


def play(state, limit):
    if game_ended(state, limit):
        return state

    # next_move = get_next_move(state)
    return play(get_next_state(state), limit)


if __name__ == '__main__':
    game = play(state=tuple(), limit=100)
    print(report(game))
