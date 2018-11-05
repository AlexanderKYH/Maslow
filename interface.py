import category, hierarchy

def get_questions_all():

    questions_all = []
    category_list = hierarchy.get_hierarchy_categories()

    for x in category_list:
        questions_all.extend(category.get_category_questions(x))

    return questions_all


