#----------------Author Note------------------------------------------------
# This project is designed to demonstrate a good way of managing
# an application that is processing data that will maniupulate user input
# --
# This file concerns the implementation of runtime components
# Author: Josh
#----------------------------------------------------------------------------

#----------------Imports-----------------------------------------------------
from classroom import Classroom
import os
import sys
import typing
import yaml


#----------------Globals-----------------------------------------------------
configDictionary:   dict = {}
userSessionDetails: tuple = None
configPath:         str = None
classRooms:         list = []


#----------------Utility Functions-------------------------------------------
def loadConfig() -> None:

    print("\nLoading config from path {}".format(configPath))

    try:
        with open(os.path.abspath(configPath)) as configFile:
            global configDictionary
            configDictionary = yaml.safe_load(configFile)
        print("\nSuccessful config load")

    except:
        print("Unsuccessful config loading")

    print(configDictionary)
    
#----------------Processing Functions----------------------------------------
def createClassroom(classroomSize: str, classroomId: str) -> object:

    global configDictionary
    if classroomSize == 'Y':
        classroomSize = "Large"
    else:
        classroomSize = "Small"

    print("\nCreating classroom size {} for class {}".format(classroomSize, classroomId))

    classRoomConfig: dict = configDictionary[classroomId]

    classroomA: object = Classroom(classRoomConfig['students'],
                          classRoomConfig['chairAmount'],
                          classRoomConfig['deskAmount'],
                          classRoomConfig['teacher'],
                          classroomSize)

    return classroomA

#----------------Runtime Functions-------------------------------------------
def main() -> None:

    global configPath 
    global configDictionary

    print("Starting up classroom processor.....")

    userName = input("Username: ")
    password = input("Password: ")
    userSessionDetails = (userName, password)

    # Cheat and just pass in any input
    if userName and password is None:
        print("Incorrect userName and password")
        return None
    else: 
        print("\nWelcome {}\n".format(userName))

    # Delete password so not in memory
    del password

    # Hint .\exampleClassroom.yml
    if len(sys.argv) < 2:
        configPath = input("\nNo file provided on cmd line, please input your config location: ")
    else:
        configPath = sys.argv[1]
        print(sys.argv[1])
    loadConfig()

    # Take user input and create the classroom
    classroomSize:  str = input("\nIs your classroom large? (Enter Y/N): ")
    classroomId:    str = input("\nWhat classroom are you configuring?: ")
    classroom: object = createClassroom(classroomSize, classroomId)

    # Now test the class functions
    # Getters
    print('\n')
    print('*'*50)
    print(classroom.getStudents())
    print(classroom.getChairAmount())
    print(classroom.getDeskAmount())
    print(classroom.getTeacher())
    print(classroom.getClassroomSize())
    print('*'*50)

    # Reports
    classroom.printClassroom()
    print(classroom.createReport())
    print('\n')

    # Diagram
    diagram = classroom.createDiagram()

if __name__=="__main__":
    main()


    def createReport(self: object) -> dict:

        classroomReport: dict = {}

        return classroomReport




