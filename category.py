class Category:

    #Function to collect all questions in a category and return them as a list
    def get_category_questions(self, category_id: str):
        questions = []
        with open(category_id, "r") as f:
            for line in f:
                questions.append(line.replace("\n", ""))
        return questions