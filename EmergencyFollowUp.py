from interface import Interface

class Emergency_followup():

    def setup_followup(self):
        setup_dict = {}
        i = Interface()
        question_list = i.get_question_akut()

        for question in question_list:
            setup_dict[question] = "none"
        with open("followup_setup.txt", "w") as f:
            f.write(str(setup_dict))
            print(setup_dict)

    def change_followup(self, question_id: str, followup: str):

        setup_dict = eval(open("followup_setup.txt").read())
        setup_dict.update({question_id: followup})
        with open("followup_setup.txt", "w") as f:
            f.write(str(setup_dict))

    def read_followup(self, question_id: str):
        followup_dict = eval(open("followup_setup.txt").read())
        answer = followup_dict.get(question_id)
        return answer

    def new_followup(self):
        i = Interface()
        question_list = i.get_question_akut()
        setup_dict = eval(open("followup_setup.txt").read())

        for question in question_list:
            followup = input("What would you encurage yourself with")
            setup_dict[question] = followup
        with open("followup_setup.txt", "w") as f:
            f.write(str(setup_dict))
            print(setup_dict)
