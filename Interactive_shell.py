from cmd import Cmd

class MyPrompt(Cmd):

    # prompt = '>>> '
    intro = "*"*72 + "\n" + "Welcome, to sing-up type signup, to log-in type " \
                            "login, to quit type exit" + "\n" + "*"*72


    def do_exit(self, inp):
        """exit the application"""
        print("Quit the application.")
        return True


    def do_signup(self, input):
        """the function accepts signing-up details."""
        print("provide name, e-mail address, username, password separating "
              "them with space")
        name = input.split()[0] + ' ' + input.split()[1]
        email = input.split()[2]
        username = input.split()[3]
        password = input.split()[4]
        print(f"{name}, {email}, {username}, {password}")

    def do_login(self, input):
        """the function accepts username and password."""
        username = input.split()[0]
        password = input.split()[1]
        print(f"{username}, {password}")


p = MyPrompt()
p.cmdloop()


