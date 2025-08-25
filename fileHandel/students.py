class Students:
    def __init__(self,rollno, name, dept):
        self.rollno = rollno
        self.name = name
        self.dept = dept
    
    def display(self):
        print(f'RollNo: {self.rollno} \nName: {self.name}\nDept: {self.dept}')
        