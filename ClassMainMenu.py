from interface import Interface
class MainMenu:
    def __init__(self):
        self.choices = {
            "1": self.run_daily_test,
            "2": self.run_emergency_test,
            "3": self.run_history,
            "4": self.run_appeal,
            "5": self.run_quit
        }
    def display_menu(self):
        print("=" * 34)
        print("""
        1. Daily Test
        2. Emergency Test
        3. History
        4. Change Follow Up
        5. Exit Program
                 """)
        print("=" * 34)

    def run(self):

        #Visar menyn och frågar efter användarinput
        while True:
            self.display_menu()
            choice = input("Make a decision: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} Felaktig inmatning".format(choice))

# Funktionerna under skall ej vara med i denna klassen utan används just nu för att säkerställa att Menyn fungerar.


    def run_daily_test(self):
        Interface.interface_daily_questions(self)

    def run_emergency_test(self):
        Interface.interface_questions_akut(self)


    def run_history(self):
        f = open("data.txt", "r")
        message = f.read()
        print(message)
        input("Press Enter to continue")

    def run_appeal(self):
        print("Please check your internet-connection")

    def run_quit(self):
        print("Good bye")
        quit()






def main():
    MainMenu().run()

if __name__ == "__main__":
    main()