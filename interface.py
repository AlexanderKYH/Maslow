import category, hierarchy, level

def get_questions_all():

    questions_all = []
    category_list = hierarchy.get_hierarchy_categories()

    for x in category_list:
        questions_all.extend(category.get_category_questions(x))

    return questions_all

def get_question_akut():

    question_akut =[]
    category_list = []

    category_list.extend(level.get_level_category(1))
    category_list.extend(level.get_level_category(2))

    for x in category_list:
        question_akut.extend(category.get_category_questions(x))

    return question_akut
