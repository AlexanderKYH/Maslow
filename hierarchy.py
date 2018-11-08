from level import Level

class Hierarchy:

    def get_hierarchy_categories(self):
        temp = []
        category_list = []

        for r in range(5):
            temp.extend(Level.get_level_category(r))
            category_list = [x for x in temp]

        return category_list

