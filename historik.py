from typing import Any, Union


class Historik :

    # def set_level_results(self, result):
    #     file = open("data.txt", "a")
    #     file.write(Result)
    #
    #
    #     Average_value = total_result/nr_lines
    #     print(Gamla_level_result)
    #
    #
    # def set_total_results():
    #     Average_value = total_result/nr_lines
    #     print(gamla_total_results)
    #
    # def get_level_results(self):
    #     file = open("data.txt", "r")
    #     level_result += line
    #     data = line.split(";")
    #     data = line.split(" ")
    #
    #
    # def get_total_results(self):
    #     file = open("data.txt", "r")
    #     total_result += line
    #     data = line.split(";")
    #     data = line.split(" ")
    #
    #     print.file.read()
    #
    #
    #
    #     return total_result


    def set_historik_total(self, historik: list):
        ref_value = sum(historik) / len(historik)
        with open("historik_total.txt", "a") as f:
            f.writelines(str(ref_value )+ "\n")

    def get_historik_all_total(self):
        result = []
        with open("historik_total.txt") as f:
            for line in f:
                result.append(line.replace("\n", ""))
        return result






