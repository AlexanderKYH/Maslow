from question import Question
from category import Category
from level import Level
from hierarchy import Hierarchy
from interface import Interface
from diagnosis import Diagnosis
from EmergencyFollowUp import Emergency_followup

def main():
    d = Diagnosis()
    c = Category()
    l = Level()
    q = Question()
    e = Emergency_followup()

    #answer = q.get_question("sex.txt", 1)
    #print(answer)
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
    #answer = d.read_diagnosis()
    #answer = d.write_diagnosis("this is question nr 3", "A diagnos")
    #answer = d.get_diagnosis("this is question nr 3")
    #answer = e.setup_followup()
    #answer = e.change_followup("this is question nr 2", "this is a good answer")
    answer = e.read_followup("this is question nr 2")
    print(answer)

if __name__ == '__main__':
    main()