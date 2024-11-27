from all_or_none import minimize_all_or_none_sets
from copy import deepcopy


error_messages = []


def send_msg(channel, msg):
    print(f'TECHIO> message --channel "{channel}" "{msg}"')
    # print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


def check_answer(test, answer):

    global error_messages

    all_or_none_sets = [set(group) for group in test]

    changes_made = True
    while changes_made:
        changes_made = False
        new_all_or_none_sets = []
        for group_1 in all_or_none_sets:
            for i, group_2 in enumerate(new_all_or_none_sets):
                if group_1 & group_2:
                    new_all_or_none_sets[i] = group_1 | group_2
                    changes_made = True
                    break
            else:
                new_all_or_none_sets.append(group_1)

        all_or_none_sets = new_all_or_none_sets

    proper_answers = set(''.join(sorted(group)) for group in all_or_none_sets)
    answers = set(''.join(sorted(group)) for group in answer)

    if len(proper_answers) != len(answers):
        verb = 'was' if len(proper_answers) == 1 else 'were' 
        error_messages.append(f'Your answer has {len(answers)} all-or-none groups. {len(proper_answers)} {verb} expected.')
    elif proper_answers != answers:
        error_messages.append(f'Although you have the correct number of all-or-none groups, the group members are not correct.')
        error_messages.append('')
        error_messages.append('These are the expected all-or-none groups:')
        error_messages.append('')
        for group in sorted(proper_answers):
            error_messages.append(f'   {list(group)}')

        error_messages.append('')
        error_messages.append('These are the groups you found:')
        error_messages.append('')
        for group in sorted(answers):
            error_messages.append(f'   {list(group)}')

    return proper_answers == answers
    

def test_all_or_none():

    global error_message

    TESTS = [
                 [('A', 'B'), ('C', 'D'), ('E', 'F')],  
                 [('A', 'B'), ('B', 'C')],  
                 [('A', 'B'), ('B', 'C'), ('C', 'D'), ('E', 'F')],
                 [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'F'), ('X', 'Y'), ('Z', 'Y'), ('E', 'F'), ('J', 'K'), ('Z', 'P')]
            ]

    all_tests_passed = True
    for test in TESTS:

        try:
            answer = minimize_all_or_none_sets(deepcopy(test))

            assert type(answer) in [list, set], f'Your code must return a list or set. {type(answer)} not allowed for return value.'

            for group in answer:
                assert type(group) in [list, set], f'Improper return value structure. Try returning List[List[str]]'

                for element in group:
                    assert type(element) == str, f'Improper return value structure. Try returning a List[List[str]]'

            assert check_answer(deepcopy(test), answer), f'Failed Test: {test}'
            send_msg("Successful Test Cases:", f'Test Input: {test}')

        except AssertionError as e:
            send_msg("Oops! 🐞", e)
            for msg in error_messages:
                send_msg("Hint 💡", msg)
            all_tests_passed = False
            break

    if all_tests_passed:
        success()
    else:
        fail()



if __name__ == "__main__":
    test_all_or_none()
