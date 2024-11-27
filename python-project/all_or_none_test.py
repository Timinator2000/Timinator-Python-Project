from all_or_none import minimize_all_or_none_sets
from copy import deepcopy


error_message = ''


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")


def check_answer(test, answer):

    global error_message

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
        error_message = f'Your answer has {len(answers)} all-or-none groups. Only {len(proper_answers)} {verb} expected.'
    elif proper_answers != answers:
        error_message = f'Although you have the correct number of all-or-none groups, the group members are not correct.\n\n'
        error_message += 'These are the expected all-or-none groups:\n'
        for group in sorted(proper_answers):
            error_message += f'   {list(group)}\n'

        error_message += '\nThese are the groups you found:\n'
        for group in sorted(answers):
            error_message += f'   {list(group)}\n'

    return proper_answers == answers
    

def test_all_or_none():

    global error_message

    TESTS = [
                 [('A', 'B'), ('C', 'D')],  
                 [('A', 'B'), ('B', 'C')],  
                 [('A', 'B'), ('B', 'C'), ('C', 'D'), ('E', 'F')]
            ]

    all_tests_passed = True
    for test in TESTS:

        try:
            answer = minimize_all_or_none_sets(deepcopy(test))
    
            assert check_answer(deepcopy(test), answer), f'Failed Test: {test}'
            send_msg("Successful Test Cases:", f'Success: {test}')

        except AssertionError as e:
            send_msg("Oops! 🐞", e)
            send_msg("Hint 💡", error_message)
            all_tests_passed = False
            break

    if all_tests_passed:
        success()
    else:
        fail()


if __name__ == "__main__":
    test_all_or_none()
