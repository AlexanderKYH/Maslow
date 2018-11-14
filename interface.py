from hierarchy import Hierarchy
from category import Category
from level import Level
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
