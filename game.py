from revised_game_search import revised_game_search
from game_status import Exhausted, Poison, NotFound

def game(tree, x, times):
    try:
        revised_game_search(tree, x, times)
    except Exhausted as e:
        print('Failure!')
        print(e)
    except Poison as e:
        print('Failure!')
        print(e)
    except NotFound as e:
        print('Failure!')
        print(e)

