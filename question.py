class Question:

    def get_question(category_id: str, question_id: int):
        with open(category_id, "r") as f:
            for _ in range(question_id):
                line =f.readline()
            return line





