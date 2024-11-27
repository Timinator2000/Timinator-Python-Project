from all_or_none import minimize_all_or_none_sets
from copy import deepcopy


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


def test_all_or_none():

    TESTS = [
                 [('A', 'B'), ('C', 'D')],  
                 [('A', 'B'), ('B', 'C')],  
                 [('A', 'B'), ('B', 'C'), ('C', 'D'), ('E', 'F')]
            ]
    
    for test in TESTS:

        try
            answer = minimize_all_or_none_sets(deepcopy(test))
    
            assert check_answer(deepcopy(test), answer), f'Failure: {test}'
            success()
            send_msg("Kudos 🌟", f'Success: {test}')

        except AssertionError as e:
            fail()
            send_msg("Oops! 🐞", e)
            send_msg("Hint 💡", "Did you properly accumulate all stars into 'total_stars'? 🤔")

            break


if __name__ == "__main__":
    test_all_or_none()
