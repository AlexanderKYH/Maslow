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
        print("=" * 60)
        print("""
                1. Starta dagligt Test
                2. Starta akut-test
                3. Historik
                4. Ändra uppmaningar
                5. Avsluta programmet
                 """)
        print("=" * 60)

    def run(self):

        #Visar menyn och frågar efter användarinput
        while True:
            self.display_menu()
            choice = input("Välj ett alternativ [1-5]: ")
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
         # file-input.py
        f = open('data.txt', 'r')
        message = f.read()
        print(message)
        input("Press Enter to continue")
        
    def run_appeal(self):
        print("Ring Bosse")

    def run_quit(self):
        print("Avslutar programmet")
        print("Hej då :)")
        quit()






def main():
    MainMenu().run()

if __name__ == "__main__":
    main()
