#----------------Author Note------------------------------------------------
# This project is designed to demonstrate a good way of managing
# an application that is processing data that will maniupulate user input
# --
# This file concerns the implementation of runtime components
# Author: Josh
#----------------------------------------------------------------------------

#----------------Imports-----------------------------------------------------
import os
import sys
import typing


#----------------Utility Functions-------------------------------------------
def createDict() -> None:

    return None

#----------------Class-------------------------------------------------------
class Classroom:

    students:      dict = None
    chairAmount:   int  = None
    deskAmount:    int  = None
    teacher:       str  = None
    classroomSize: str  = None

    def __init__(self: object, students: list, chairAmount: int, deskAmount: int,
                 teacher: str, classroomSize: str) -> None:
        
        self.students       = students
        self.chairAmount    = chairAmount
        self.deskAmount     = deskAmount
        self.teacher        = teacher
        self.classroomSize  = classroomSize


    # Tasking Methods
    def createReport(self: object) -> dict:

        classroomReport: dict = {}

        classroomReport['Students']     = self.students
        classroomReport['Chair Amount'] = self.chairAmount
        classroomReport['Desk Amount']  = self.deskAmount
        classroomReport['Teacher']      = self.teacher
        classroomReport['Class Size']   = self.classroomSize

        return classroomReport

    def createDiagram(self: object) -> object:
        return None

    def printClassroom(self: object) -> None:

        print('\n')
        print('*'*50)
        print("Students {}".format(self.students))
        print("Chair Amount {}".format(self.chairAmount))
        print("Desk Amount {}".format(self.deskAmount))
        print("Teacher {}".format(self.teacher))
        print("Class Room Size {}".format(self.classroomSize))
        print('*'*50)
        print('\n')

    # Getter Methods
    def getStudents(self: object) -> list:
        return self.students

    def getChairAmount(self: object) -> list:
        return self.chairAmount

    def getDeskAmount(self: object) -> list:
        return self.deskAmount

    def getTeacher(self: object) -> list:
        return self.teacher

    def getClassroomSize(self: object) -> list:
        return self.classroomSize




