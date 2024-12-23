class student:
    grade=9
    name="Elkan"
    
    def introduction(self):
        print("Hi i am a student")
    
    def details(self):
        print("My name is ",self.name)
        print("I studay in grade",self.grade)

ob=student ()
ob.introduction()
ob.details()

        