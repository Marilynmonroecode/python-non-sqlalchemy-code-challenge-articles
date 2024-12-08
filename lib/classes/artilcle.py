class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = self.check_title(title)

    def get_title (self):
        return str(self.title)
    
    def check_title(self,title):
        if self.hasattr(title):
            return "Title already exist"
        if len(title) > 50:
            return "Title is too long"
        elif len(title) < 5:
            return "Title is too short"
        else:
            return title