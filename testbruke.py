from question import Question
from category import Category
from level import Level
from hierarchy import Hierarchy
from interface import Interface
from diagnosis import Diagnosis


def main():
    d = Diagnosis()
    c = Category()
    l = Level()
    q = Question()

    answer = q.get_question("sex.txt", 1)
    print(answer)
    #cat_list = c.get_category_questions("sex.txt")
    #print(cat_list)
    #answer = l.get_level_category(3)
    #print(answer)
    h = Hierarchy()
    #answer = h.get_hierarchy_categories()
    #print(answer)
    I = Interface()
    #answer = I.get_questions_all()
    #print(answer)
    #answer = I.get_question_akut()
    #print(answer)
    #answer = d.setup_diagnosis()
    answer = d.read_diagnosis()
    print(answer)

if __name__ == '__main__':
    main()