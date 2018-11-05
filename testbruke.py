import question, category, level, hierarchy, interface

def main():
    #answer = question.get_question("sex.txt", 3)
    #print(answer)
    #cat_list = category.get_category_questions("sex.txt")
    #print(cat_list)
    #answer = level.get_level_category(3)
    #print(answer)
    #answer = hierarchy.get_hierarchy_categories()
    #print(answer)
    answer = interface.get_questions_all()
    print(answer)

if __name__ == '__main__':
    main()