#hybrid
class grandma:
    def __init__(self):
        print("grandma")
    def skil(self):
        print("cooking")
class father:
    def __init__(self):
        print("father")
    def skill(self):
        print("painting")
class mother(grandma):
    def skill(self):
        print("teaching")
class son(mother,grandma,father):
    def skill(self):
        print(mother.skill(self))
family=son()
family.skill()

#hiearchical
'''
class father:
    def __init__(self):
        print("father")
    def skill1(self):
        print("painting")
    def skill2(self):
        print("riding")
class son1(father):
    def skill(self):
        print(father.skill1(self))
class son2(father):
    def skill(self):
        print(father.skill2(self))
family=son2()
family.skill()
'''
#multilevel
'''
class grandma:
    def __init__(self):
        print("grandma")
    def skil(self):
        print("cooking")
class father(grandma):
    def skill(self):
        print("painting")
class son(father):
    def skill(self):
        print(father.skill(self))
family=son()
family.skill()
'''
#single
'''
class father:
    def __init__(self):
        print("father")
    def skill(self):
        print("painting")
class son(father):
    def skill(self):
        print(father.skill(self))
family=son()
family.skill()
'''
#multiple
'''
class grandma:
    def __init__(self):
        print("grandma")
    def skil(self):
        print("cooking")
class father:
    def __init__(self):
        print("father")
    def skill(self):
        print("painting")

class mother:
    def __init__(self):
        print("mother")
    def skill(self):
        print("teaching")
class son(grandma,father):
    def skill(self):
        print(father.skill(self))
family=son()
family.skill()
'''  
    
