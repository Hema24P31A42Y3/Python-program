class Animal():
    def information(self,name,gender,skills):
        self.name=name
        self.gender=gender
        self.skills=skills
        return f"""name={name} gender={gender} skills={skills}"""
    def speaks(self):
        return "cat sounds meow meow"
class pilli(Animal):
    def information(self,name,gender,skills):
        super().information(name,gender,skills)
        return f"""name={name} gender={gender} skills={skills}"""
    def speaks(self):
        return "cat sounds meow meow"
lilli=pilli()
lilli.information("lilli","female","drink milk")
    
