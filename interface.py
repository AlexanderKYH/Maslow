from hierarchy import Hierarchy
from category import Category
from level import Level
from EmergencyFollowUp import Emergency_followup

def check_int(value):
    if isinstance(value, str):
        if value.isdecimal():
            return 1 <= int(value) <= 10
    return False

class Interface:

    def get_questions_all(self):

        h = Hierarchy()
        questions_all = []
        category_list = h.get_hierarchy_categories()

        for x in category_list:
            questions_all.extend(Category.get_category_questions(self, x))

        return questions_all

    def get_question_akut(self):

        question_akut =[]
        category_list = []

        category_list.extend(Level.get_level_category(self, 0))
        category_list.extend(Level.get_level_category(self, 1))

        for x in category_list:
            question_akut.extend(Category.get_category_questions(self, x))
        return question_akut

    def interface_questions_akut(self):
        questions = Interface.get_question_akut(self)

        for x in questions:
            temp = int(input(x))

            if temp >= 7:
                e = Emergency_followup()
                print(Emergency_followup.read_followup(self, x))

    def interface_daily_questions(self):
        historik = []
        questions = Interface.get_questions_all(self)


        for x in questions:
            while True:
                value = input(x)
                if check_int(value):
                    historik.append(int(value))
                    break
                else:
                    print("Wrong input, must be an integer between 1-10")
















        #skicka historik till historik klassen