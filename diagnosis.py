from interface import Interface

class Diagnosis:


    def setup_diagnosis(self):
        setup_dict = {}
        i = Interface()
        question_list = i.get_questions_all()

        for question in question_list:
            setup_dict[question] = "none"
        with open("diagnosis_setup.txt", "w") as f:
            f.write(str(setup_dict))



    def read_diagnosis(self):
        setup_dict = eval(open("diagnosis_setup.txt").read())
        return setup_dict


    def write_diagnosis(self, question, diagnosis):
        diagnosis_dic = eval(open("diagnosis_setup.txt").read())
        with open("diagnosis_setup.txt", "w") as f:
            diagnosis_dic.update({question: diagnosis})
            f.write(str(diagnosis_dic))

    def get_diagnosis(self, question):
        diagnosis_dict = eval(open("diagnosis_setup.txt").read())
        diagnose = diagnosis_dict.get(question)
        return diagnose
