from component import Component

class Health_Component(Component):
    def __init__(self, hp=1):
        super().__init__()
        self.__hp = hp
        self.__maxHp = hp
        pass
    @property
    def maxHp(self):
        return self.__maxHp
    @maxHp.setter
    def maxHp(self, value):
        self.__Maxhp += value

    def Heal(self, amount=1):
        if self.__maxHp <= self.__hp: return
        self.__hp += amount
        
    def Hit(self, amount=1):
        if self.__hp <= 0: return
        self.__hp -= amount
    def get_hp(self):
        return self.__hp