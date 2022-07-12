
import time
from winotify import *
homework_names = ['oihsfguhfsd']
homework_desc =[]
def pop_priority():
    homework_names.pop(0)
def take_hw():
    print('input homework interms of priority(or order to do)')
    x = int(input('how much homework you got today bud?'))
    for i in range(x):
        y = input('enter Homework title: ')
        z = input('enter homework description: ')
        homework_names.append(y)
        homework_desc.append(z)
def help_menue():
    print('homework or 1:   for homework')
while True:
    time.sleep(1)
    hw_completion_notif= Notification(app_id='Glyched School',
                                    title ='Your homework is completed for the day!!',
                                    msg='either time for happiness or more work....')
    if not homework_names:
        hw_completion_notif.show()
        break
    priority_hw = homework_names[0]
    hw_notif = Notification(app_id='Glyched School',
                        title = 'homework',
                        msg =('Top proirity homework: ',priority_hw),
                        duration='long')
    hw_notif.add_actions(label='Completed!,lets move on')
    hw_notif.show()
