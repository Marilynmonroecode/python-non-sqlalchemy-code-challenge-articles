class Author:
    def __init__(self, name) -> None:
        self.name = self.check_name(name)

    def author_name(self) -> str:
        return self.name  
    
    def check_name(self, name):
        if self.hasattr(name):
            return "Name already exist"
        if len(name) < 0:
            return "Not valid"
        else:
            return name   