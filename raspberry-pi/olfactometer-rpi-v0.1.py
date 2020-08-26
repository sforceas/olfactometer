import os
import time 
​from time import sleep 
​from datetime import datetime
​from gpiozero import Button, Servo, Motor

#GPIO ASSIGNEMENTS
button1 = Button(2)
button2 = Button(3)
button3 = Button(4)

valveA = Servo(5)
valveB = Servo(6)
valveC = Servo(7)

blower = Motor(8,9)



def select_patient():
    
    patientID = input(f'Write the patient ID: ')
    return patientID

def select_odourant():
    
    odourantCode = ("A","B","C")
    odourantList = ("lemon","garlic","coffee")
    index = -1 + int(input(f'Select the odourant by writting the number of the list:[1]{odourantList[0]}, [2]{odourantList[1]}, [3]{odourantList[2]}.'))x
    
    odourant = odourantList[index]
    container = odourantCode[index]
    
    return odourant

def select_correct_button():
    
    correct_button = int(input(f'Select the correct answer button by writting the number of the list:[1] Left,[2] Center, [3] Right.'))
    return correct_button


def press_button(counter):
    
    while True 
        
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
    valve.angle(1)
    return

def close_valve(valve):
    valve.angle(0)
    return


def run_test(container, correct_button):

    blower.forward(1)
    open_valve(container)
    counter = time.time()    
    pressed_button,reactionTime = press_button(counter)

    if correct_button == pressed_button:
        correctAnswer = True
    else:
        correctAnswer = False
    
    blower.stop()
    close_valve(container)

    return reactionTime,correctAnswer

def data_logger(patientID,testID,odour,reactionTime,correctAnswer):
    file = open("/home/pi/data_log.csv", "a")
    i=0
    if os.stat("/home/pi/data_log.csv").st_size == 0:<br>        
        file.write("PatientID,DateTime,TestID,Odour,ReactionTime(s),CorrectAnswer,PreviousDiagnosis\n")
 
    while True:
        
        now = datetime.now()
        file.write(patientID +","+ str(now) +","+ testID +","+ odour +","+ str(reactionTime) +","+ str(correctAnswer) +"\n")
        file.flush()
        time.sleep(5)
        file.close()

​    
if __name__ == "__main__":
    
    patientID = select_patient()

    odourant,container = select_odourant
    correct_button = select_correct_button
    testID = (container & correct_button)
    
    (reactionTime,correctAnswer) = run_test(container,correct_button)
    data_logger(patientID,testID,odour,reactionTime,correctAnswer)


    