import os
import time 
from time import sleep 
from datetime import datetime
from gpiozero import Button, AngularServo, Motor

#GPIO ASSIGNEMENTS
button1 = Button(17)
button2 = Button(27)
button3 = Button(22)

valveA = AngularServo(5, min_angle=-90, max_angle=90)
valveB = AngularServo(6, min_angle=-90, max_angle=90)
valveC = AngularServo(13, min_angle=-90, max_angle=90)
valveD = AngularServo(19, min_angle=-90, max_angle=90)

blower = Motor(23,24)

#CONSTANT VARIABLES
purgeTime = 15
openAngle = 45
closeAngle = -45

def select_patient():
    
    patientID = input(f'Write the patient ID: ')
    return patientID

def select_odourant():
    
    odourantCode = ("A","B","C")
    odourantList = ("lemon","garlic","coffee")
    index = -1 + int(input(f'Select the odourant by writting the number of the list:[1]{odourantList[0]}, [2]{odourantList[1]}, [3]{odourantList[2]}.'))
    
    odourant = odourantList[index]
    container = odourantCode[index]
    
    return container,odourant

def select_correct_button():
    
    correct_button = int(input(f'Select the correct answer button by writting the number of the list:[1] Left,[2] Center, [3] Right.'))
    return correct_button

def press_button_test(counter):
    
    pressed_button = int(input())
    reactionTime = time.time() - counter
    reactionTime = round(reactionTime,1)
    print(f'Pressed button {pressed_button}. Reaction time: {reactionTime} seconds.')
    return pressed_button,reactionTime


def press_button(counter):
    
    while True: 
        
        if button1.is_pressed:
            pressed_button = 1
            reactionTime = counter - time.time()
            return pressed_button,reactionTime

        if button2.is_pressed:
            pressed_button = 2
            reactionTime = counter - time.time()
            return pressed_button,reactionTime

        if button3.is_pressed:
            pressed_button = 3
            reactionTime = counter - time.time()
            return pressed_button,reactionTime

def open_valve(valve):
    print(f'Opening valve{valve}...')
    
    if container == 'A':
        valveA.angle = openAngle
    elif container == 'B':
        valveB.angle = openAngle
    elif container == 'C':
        valveC.angle = openAngle
    elif container == 'D':
        valveD.angle = openAngle
    
    print(f'Valve{valve} opened.')
    return

def close_valve(valve):
    print(f'Closing valve{valve}...')
    
    if container == 'A':
        valveA.angle = closeAngle
    elif container == 'B':
        valveB.angle = closeAngle
    elif container == 'C':
        valveC.angle = closeAngle
    elif container == 'D':
        valveD.angle = closeAngle
        
    print(f'Valve{valve} closed.')
    return


def purge():
    
    open_valve('D')
    blower.forward(1)
    t = purgeTime
    
    while t>= 0:
        print(t, end ='s...')
        time.sleep(1)
        t-=1 
    
    blower.stop()
    close_valve('D')



def run_test(container, correct_button):
    print('Purging system (15 seconds)')
    print(f'Runing test... Code: {container}{correct_button}')
    purge()
    open_valve(container)
    print('Blower on.')
    blower.forward(1)
    print('Time counter started. Waiting for button to be pressed...')
    counter = time.time()
    #pressed_button,reactionTime = press_button(counter)

    pressed_button,reactionTime = press_button_test(counter)

    if correct_button == pressed_button:
        correctAnswer = True
        print('The answer is correct.')
    else:
        correctAnswer = False
        print('The answer is not correct.')
    
    print('Blower off.')
    blower.stop()
    close_valve(container)
    print('Purging system (15 seconds)')
    purge()
    print('Purge ended. Test ended succesfully.')

    return reactionTime,correctAnswer

def data_logger(patientID,testID,odour,reactionTime,correctAnswer):
    
    file = open("/home/pi/data_log.csv", "a")
    if os.stat("/home/pi/data_log.csv").st_size == 0:        
        file.write("PatientID,DateTime,TestID,Odour,ReactionTime (TRC),CorrectAnswer\n")
 
    while True:
        
        now = datetime.now()
        file.write(patientID +","+ str(now) +","+ testID +","+ odourant +","+ str(reactionTime) +","+ str(correctAnswer) +"\n")
        print('Data saved correctly.')
        file.flush()
        print('Data Flushed')
        time.sleep(5)
        file.close()
        print('File closed')
        break

if __name__ == "__main__":
    
    patientID = select_patient()
    
    numTest = int(input('Write the number of tests for this session: '))
    for _ in range(numTest):
        container,odourant = select_odourant()
        correct_button = select_correct_button()
        testID = (container + str(correct_button))
        (reactionTime,correctAnswer) = run_test(container,correct_button)
        data_logger(patientID,testID,odourant,reactionTime,correctAnswer) 
    print(f'Session ended for patient {patientID}.')


    