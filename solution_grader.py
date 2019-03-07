# -*- coding: utf-8 -*-

class Grader():
    
    def __init__(self):
        self.result  = 0
        self.classes = 0
           
    def classes_updater(self, num):
        self.classes = num
    
    @staticmethod
    def find_min(list_of_floats):
        return sorted(list_of_floats)[0]
    
    @staticmethod
    def find_max(list_of_floats):
        return sorted(list_of_floats)[-1]
    
    def find_gpa(self, list_of_floats):
        self.result = sum(list_of_floats) / self.classes
        return self.result
    
    
if __name__ == "__main__":  
    g = Grader()
    number_of_classes = int(input("How many classes total?"))
    g.classes_updater(number_of_classes)
    classes_grades = []
    
    for c in range(0, g.classes):
        classes_grades.append(float(input("Enter grade for class #{}:\n".format(c + 1))))
                 
    print("\nREPORT:\n")                                          
    print("Lower grade   {}".format(g.find_min(classes_grades)))
    print("Highest grade {}".format(g.find_max(classes_grades)))
    print("GPA           {}".format(g.find_gpa(classes_grades)))
