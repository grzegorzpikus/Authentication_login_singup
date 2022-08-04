# shell with while
from Input_checker import log_in, sing_up


def main():

    print("*"*80 + "\n Welcome in personal CERN application (pCERNa). Choose "
          "one of the options below:" + "\n" + "*" * 80 + "\n [1] to log-in "
          "type 1\n [2] to sign-up type 2\n [3] to go back to the main menu "
          "type 3\n [4] to quit the application type exit" + "\n" + "*" * 80)

    inp = input()

    if inp == '1':
        log_in()
    elif inp == '2':
        sing_up()
    elif inp == '3':
        main()
    elif inp == 'exit':
        print("You quite the application.")
        quit()
    else:
        print("Wrong command, try again")
        main()


if __name__ == "__main__":
    main()


