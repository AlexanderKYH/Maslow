class MainMenu:
    def __init__(self):
        self.choices = {
            "1": self.daily_test,
            "2": self.emergency_test,
            "3": self.history,
            "4": self.quit
        }
    def display_menu(self):
        print("=" * 30)
        print("""
                1. Dagligt test
                2. Akut-test
                3. Historik
                4. Avsluta
                 """)
        print("=" * 30)

    def run(self):

        #Visar menyn och frågar efter användarinput
        while True:
            self.display_menu()
            choice = input("Välj ett alternativ [1-4]: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} Felaktig inmatning".format(choice))

# Funktionerna under skall ej vara med i denna klassen utan används just nu för att säkerställa att Menyn fungerar.

    def daily_test(self):
        print("Dagligt test är inte färdigt ännu")

    def emergency_test(self):
        print("Akut-testet är inte färdigt ännu")

    def history(self):
        print("Historik är inte färdigt ännu")

    def quit(self):
        print("Avslutar programmet")
        print("Hej då :)")
        quit()






def main():
    MainMenu().run()

if __name__ == "__main__":
    main()