class Component:
    def __init__(self):
        self.__entity = None

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, entity):
        self.__entity = entity

    def update(self, frametime):
        pass

    def draw(self):
        pass
    def set_Comp(self):
        pass
