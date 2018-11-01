import level

def get_hierarchy_categories():
    temp = []
    category_list = []

    for r in range(5):
        temp.extend(level.get_level_category(r))
        category_list = [x for x in temp]

    return category_list

