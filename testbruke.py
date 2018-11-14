from question import Question
from category import Category
from level import Level
from hierarchy import Hierarchy
from interface import Interface
from diagnosis import Diagnosis
from EmergencyFollowUp import Emergency_followup
from historik import Historik
def main():
    d = Diagnosis()
    c = Category()
    l = Level()
    q = Question()
    e = Emergency_followup()
    hist = Historik()
    value_list = [3, 4, 5, 4, 5, 6, 6, 5, 4]
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
    #answer = e.change_followup("How have your general health been today?", "Go for a run")
    #answer = e.read_followup("How have your general health been today?")
    #answer = e.new_followup()
    #answer = I.interface_questions_akut()
    #answer = I.interface_daily_questions()
    #answer = hist.set_historik_total([1, 2 , 3, 6])
    #answer = hist.get_historik_all_total()
    answer = l.level_count()

    print(answer)

if __name__ == '__main__':
    main()