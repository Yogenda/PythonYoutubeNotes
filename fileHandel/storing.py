import students, pickle
stds = [students.Students(101,'Rahul','CS'),
        students.Students(102,'Ankit','Eng')]

with open('student.data','wb') as f:
    for s in stds:
        pickle.dump(s,f)

    
