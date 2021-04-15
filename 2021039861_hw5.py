class Student:
    
    def __init__(self, name):
        self.name = name
        self.Calculus = 0
        self.Software = 0
        self.English = 0
        self.C = 0
        self.c = 0
        self.S = 0
        self.s = 0
        self.E = 0
        self.e = 0
        self.average3 = 0

    def __str__(self):
        msg = ""+str(self.name)+"\n"
        msg += "Calculus " +str(self.Calculus)+" "+str(self.C)+"\n"
        msg += "Software " +str(self.Software)+" "+str(self.S)+"\n"
        msg += "Engligh " +str(self.English)+ " "+str(self.E)+"\n" 
        msg += "Average " +str(self.average3/3)+ "\n======"
        return msg

    def input_score(self, subject, score):
        if subject == "Calculus":
            self.Calculus = score
            
            if 95<=score<=100:
                self.C = "A+"
                self.c = 4.5
                self.average3 += self.c
                
            elif 90<=score<=94:
                self.C = "A0"
                self.c = 4.0
                self.average3 += self.c
                
            elif 85<=score<=89:
                self.C = "B+"
                self.c = 3.5
                self.average3 += self.c

            elif 80<=score<=84:
                self.C = "B0"
                self.c = 3.0
                self.average3 += self.c

            elif 75<=score<=79:
                self.C = "C+"
                self.c = 2.5
                self.average3 += self.c

            elif 70<=score<=74:
                self.C = "C0"
                self.c = 2.0
                self.average3 += self.c

            elif 65<=score<=69:
                self.C = "D+"
                self.c = 1.5
                self.average3 += self.c
        
            elif 60<=score<=64:
                self.C = "D0"
                self.c = 1.0
                self.average3 += self.c
                
            elif 0<=score<=59:
                self.C = "F"
                self.c = 0
                self.average3 += self.c

        elif subject == "Software":
            self.Software = score
            
            if 95<=score<=100:
                self.S = "A+"
                self.s = 4.5
                self.average3 += self.s
                
            elif 90<=score<=94:
                self.S = "A0"
                self.s = 4.0
                self.average3 += self.s
                
            elif 85<=score<=89:
                self.S = "B+"
                self.s = 3.5
                self.average3 += self.s

            elif 80<=score<=84:
                self.S = "B0"
                self.s = 3.0
                self.average3 += self.s

            elif 75<=score<=79:
                self.S = "C+"
                self.s = 2.5
                self.average3 += self.s

            elif 70<=score<=74:
                self.S = "C0"
                self.s = 2.0
                self.average3 += self.s

            elif 65<=score<=69:
                self.S = "D+"
                self.s = 1.5
                self.average3 += self.s
        
            elif 60<=score<=64:
                self.S = "D0"
                self.s = 1.0
                self.average3 += self.s
                
            elif 0<=score<=59:
                self.S = "F"
                self.s = 0
                self.average3 += self.s

        elif subject == "English":
            self.English = score
            
            if 95<=score<=100:
                self.E = "A+"
                self.e = 4.5
                self.average3 += self.e
                
            elif 90<=score<=94:
                self.E = "A0"
                self.e = 4.0
                self.average3 += self.e
                
            elif 85<=score<=89:
                self.E = "B+"
                self.e = 3.5
                self.average3 += self.e

            elif 80<=score<=84:
                self.E = "B0"
                self.e = 3.0
                self.average3 += self.e

            elif 75<=score<=79:
                self.E = "C+"
                self.e = 2.5
                self.average3 += self.e

            elif 70<=score<=74:
                self.E = "C0"
                self.e = 2.0
                self.average3 += self.e

            elif 65<=score<=69:
                self.E = "D+"
                self.e = 1.5
                self.average3 += self.e
        
            elif 60<=score<=64:
                self.E = "D0"
                self.e = 1.0
                self.average3 += self.e
                
            elif 0<=score<=59:
                self.E = "F"
                self.e = 0
                self.average3 += self.e

    
Students = []

for i in range (3):
    name = input("Student name : ")
    calculus = int(input("Input the Calculus score : "))
    software = int(input("Input the Software score : "))
    english = int(input("Input the English score : "))
    Students.append(Student(name))
    Students[i].input_score("Calculus",calculus)
    Students[i].input_score("Software",software)
    Students[i].input_score("English",english)
    
print()
for i in range(3):
    print(Students[i])
