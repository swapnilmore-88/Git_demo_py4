#
# class MedicineExpire(Exception):
#     def __init__(self, message):
#         self.message = message
#
# try:
#     10/0
# except Exception:
#     raise MedicineExpire("Medicine has expired")

#*********************************************************#
class TooYoungException(Exception):
    def __init__(self,age,mes):
        self.age = age
        self.mes = mes


class TooOldException(Exception):
    def __init__(self,age,mes):
        self.age = age
        self.mes = mes


class Matrimony:
    def __init__(self, age, gender):
        if age <21 and gender == "M":
            raise TooYoungException(age,"you are too young")

        if age<18 and gender == "F":
            raise TooYoungException(age, "you are too young")
        if age >60:
            raise TooOldException(
                age, "you are too old")
        self.age =age
        self.gender =gender

    def samplefunction(self):
        pass # we can write above if conditions here also


a = Matrimony(77,"M")
a.samplefunction()


"before stash save"

<<<<<<< Updated upstream

<<<<<<< HEAD
"before stash"
=======


"after saving stash2"
=======

"fgfdgdfgdgdg"
"jnvjbvj"

"changes made for stash"
>>>>>>> Stashed changes
>>>>>>> 08b20c0b50a52b66ec16ce64ef56769031ca7063



"made after saving and before apply"
=======
>>>>>>> Stashed changes
