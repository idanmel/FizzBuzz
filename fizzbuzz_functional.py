def get_next_move(game_state):
    output = ""
    next_num = len(game_state) + 1
    if next_num % 3 == 0:
        output += "Fizz"
    if next_num % 5 == 0:
        output += "Buzz"

    if not output:
        output = str(next_num)

    return output


def get_next_state(game_state, next_move):
    return game_state + (next_move,)


def game_ended(game_state, limit):
    return len(game_state) == limit


def report(s):
    return '\n'.join(s)


def play(state, limit):
    if game_ended(state, limit):
        return state

    next_move = get_next_move(state)
    return play(get_next_state(state, next_move), limit)


if __name__ == '__main__':
    game = play(state=tuple(), limit=100)
    print(report(game))
