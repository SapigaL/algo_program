class Zoo:

    def __init__(self, name='', number_of_animals=0, visitors_for_year=0):
        self.name = name
        self.number_of_animals = number_of_animals
        self.visitors_for_year = visitors_for_year

    def __repr__(self):
        return str(self.name) + " " + str(self.number_of_animals) + " " + str(self.visitors_for_year)

    compare = 0
    changes = 0

    @staticmethod
    def compare_count():
        Zoo.compare += 1
        pass

    @staticmethod
    def changes_count():
        Zoo.changes += 1
        pass

    @staticmethod
    def count_reset():
        Zoo.compare = 0
        Zoo.changes = 0
        pass