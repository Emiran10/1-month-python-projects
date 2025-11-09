'''
1. Görev Ekle
2. Görev Sil
3. Görevleri Görüntüle
    a. Görevi completed olarak işaretle
4. Tamamlanan Görevleri görüntüle
    a. Görevi uncompleted olarak işaretle


'''
import time
Tasks = []
ComplTasks = []
amountOftasks = 0
amountofComplTasks= 0
skip = '*' * 30
while True:
        print(skip)
        time.sleep(.25)
        print('1. Add Task')
        time.sleep(.25)
        print('2. Delete Task')
        time.sleep(.25)
        print('3. View Incomplete Tasks')
        time.sleep(.25)
        print('4. View Completed Tasks')
        time.sleep(.25)
        print('5. Finish the Process. / View the tasks and task amounts.')
        print(skip)

        time.sleep(1)
        first = input('Enter the number of the process you want to make: ')
        first = first.strip()
        print(skip) 
        time.sleep(1)
        if first.isdigit():
            intfirst = int(first)
            if intfirst == 1:
                while True:
                    tsk = input('Please enter the task you want to add: ').upper()
                    if not tsk.strip() == '' and tsk not in Tasks and tsk not in ComplTasks  :
                        Tasks.append(tsk)
                        amountOftasks += 1 
                        print(skip)
                        time.sleep(.3)
                        break
                        
                    else:
                        print('Try Again.')
                        time.sleep(.25)
                        print(skip)
                        time.sleep(.25)
                                   
            elif intfirst == 2:
                if amountOftasks == 0:
                    print('Please add a task first.')
                    time.sleep(1.5)
                while amountOftasks > 0:
                    destque = input('Please enter the task number you want to delete: ')
                    if destque.isdigit() and not destque.strip() == '':
                        destque = int(destque)
                        if 1 <= destque <= amountOftasks:
                            amountOftasks -= 1
                            Tasks.pop(destque-1)
                            print(skip) 
                            break
                        else:
                            print('Please enter a valid process number.')
                            time.sleep(.1)
                            print(skip)
                            time.sleep(.1)
                            
                    else:
                        print('Please enter a valid process number')
                        time.sleep(.1)
                        print(skip)
                        time.sleep(.1)


                
            elif intfirst == 3:
                if amountOftasks == 0:
                    print('Please add tasks first.')
                else:
                    cont = 0
                    for x in Tasks:
                        cont += 1
                        count = str(cont)
                        print(count+'.'+' '+x)
                    time.sleep(1.5)
                    print(skip)
                    print('The tasks above are incomplete.')
                    while True:
                        compton = input('Do you want to mark any of the tasks above as completed? (y/n): ')
                        if compton.upper() == 'Y':
                            choosing = input('Please type the number of the task that u want to mark as completed: ')
                            if choosing.isdigit():
                                choosing = int(choosing)
                                if 1 <= choosing <= amountOftasks:
                                    choosing = int(choosing)
                                    ComplTasks.append(Tasks[choosing - 1])
                                    Tasks.pop(choosing - 1)
                                    amountOftasks -= 1
                                    amountofComplTasks += 1
                                    time.sleep(.4)
                                    break
                        if compton.upper() == 'N':
                            print('OK.')
                            break         
                        else:
                            print('You might have misclicked. Try again.')         
            elif intfirst == 4:
                while True:
                    if amountofComplTasks == 0:
                        print('Complete a task first.')
                        print(skip)
                        time.sleep(.25)
                        break
                    for x in ComplTasks:
                        dandex = str(ComplTasks.index(x) + 1) 
                        print(dandex + '.' + ' ' + x)
                        time.sleep(.25)
                    print(skip)
                    time.sleep(.5)
                    backfr = input('Do you want to mark any of the tasks above as incomplete? (y/n): ')
                    if backfr.upper() == 'Y':
                        while True:
                            damit = input('Please type the number of the task that u want to mark as incomplete: ')
                            if damit.isdigit():
                                damit = int(damit)
                                if 1 <= damit <= amountofComplTasks:
                                    
                                    Tasks.append(ComplTasks[damit - 1])
                                    ComplTasks.pop(damit - 1)
                                    amountofComplTasks -= 1
                                    amountOftasks += 1
                                    break
                                
                                
                                print(skip)
                                time.sleep(.5)
                                break      
                    elif backfr.upper() == 'N':
                        print('OK.')
                        time.sleep(.25)
                        print(skip)
                        time.sleep(.25)
                        break
                    else:
                        print('Please enter a valid process number.')
                        time.sleep(.25)
                        print(skip)       
                        time.sleep(.25)   
                        break
            elif intfirst == 5:
                print(f'Your completed task amount is {amountofComplTasks} and your incomplete task amount is {amountOftasks}')
                print('Your completed tasks are;')
                if not amountofComplTasks == 0:
                    for x in ComplTasks:
                        print(str(int((ComplTasks.index(x))+1))+'.'+' '+ x)
                else:
                    print("You don't have any completed tasks.")
                print('Your incomplete tasks are;')
                if not amountOftasks == 0:
                    for y in Tasks:
                        print(str((int(Tasks.index(y))+1))+'.'+' '+ y)
                else:
                    print("You don't have any incomplete tasks.")
                break
                
            else:
                print('Please enter a valid process number. ')
                time.sleep(.25)
                print(skip)
                time.sleep(.25)
        else:
            print('Please enter a valid process number.')
            time.sleep(.25)
            print(skip)
            time.sleep(.25)

