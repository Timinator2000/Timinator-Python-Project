from list_comprehension_ex_09 import num_spaces
import builtins


sum_builtin_used = False


def new_sum(x):
    global sum_builtin_used
    sum_builtin_used = True
    return orig_sum(x)


orig_sum = builtins.sum
builtins.sum = new_sum


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_num_spaces():
    try:
        spaces = num_spaces('Barkley and Lulu need to go for a walk.')
        assert spaces == 8, f"Trying num_spaces('Barkley and Lulu need to go for a walk.')... Expected 8, got {spaces}"
        spaces = num_spaces('          ')
        assert spaces == 10, f"Trying num_spaces('          ')... Expected 10, got {spaces}"
     
        success()

        if sum_builtin_used:
            send_msg("My personal Yoda, you are. 🙏", "* ● ¸ .　¸. :° ☾ ° 　¸. ● ¸ .　　¸.　:. • ")
            send_msg("My personal Yoda, you are. 🙏", "           　★ °  ☆ ¸. ¸ 　★　 :.　 .   ")
            send_msg("My personal Yoda, you are. 🙏", "__.-._     ° . .　　　　.　☾ ° 　. *   ¸ .")
            send_msg("My personal Yoda, you are. 🙏", "'-._\\7'      .　　° ☾  ° 　¸.☆  ● .　　　")
            send_msg("My personal Yoda, you are. 🙏", " /'.-c    　   * ●  ¸.　　°     ° 　¸.    ")
            send_msg("My personal Yoda, you are. 🙏", " |  /T      　　°     ° 　¸.     ¸ .　　  ")
            send_msg("My personal Yoda, you are. 🙏", "_)_/LI")
        else:
            send_msg("Kudos 🌟", "Back to boring me to death...and I had so much hope for you.  Sigh.")

    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "Are you only counting the spaces? 🤔")


if __name__ == "__main__":
    test_num_spaces()
