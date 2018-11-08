from interface import Interface

class Diagnosis:
    pass


    def get_diagnosis(self):
        pass


    def setup_diagnosis(self):
        setup_dict = {}
        i = Interface()
        question_list = i.get_questions_all()

        for question in question_list:
            setup_dict.pop(question)

        return setup_dict