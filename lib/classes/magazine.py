class Magazine:
    def __init__(self, name, category):
        self.name = self.check_name(name)
        self.category = self.check_category(category)

    def magazine_name(self) -> str:
        return self.name
    
    def check_name(self, name):
        if len(name) < 2:
            return "Name too short"
        elif len(name) > 16:
            return "Name too long"
        else:
            return name
        
    def magazine_category(self) -> str:
        return self.category
    
    def check_category(self, category):
        if len(category) < 0:
            return "Not valid"
        else:
            return category   

