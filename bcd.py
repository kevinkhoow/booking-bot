import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cd = datetime.date.today()
cm = cd.strftime('%b')
if cd.month <= 11:
    nd = cd.replace(month = cd.month + 1, day = 1)
    nm = nd.strftime('%b')
else:
    nd = cd.replace(year = cd.year + 1, month = 1, day = 1)
    nm = nd.strftime('%b')

j = 0
t = 1.5
w = 0
i = 0
u = 0

def wait(parent):
    return WebDriverWait(parent, 10 * t)
def clickable(element):
    return EC.element_to_be_clickable(element)
def visible(element):
    return EC.visibility_of_element_located(element)
def invisible(element):
    return EC.invisibility_of_element_located(element)

def wait_spinner():
    try:
        wait(dvr).until(invisible((By.CLASS_NAME, 'v-overlay__content')))
    except:
        pass

kname = '<username>'
kpass = '<password>'

date_printed = '0'
time_printed = '0'

slot_dict = {
    'A': 'SESSION 1',
    'B': 'SESSION 2',
    'C': 'SESSION 3',
    'D': 'SESSION 4',
    'E': 'SESSION 5',
    'F': 'SESSION 6',
    'G': 'SESSION 7',
    'H': 'SESSION 8'
}

print('')
print('Note:')
print('*When selecting more than one date, separate them with comma(s).')
print('*Single-digit date numbers may be input with or without a leading zero, e.g. both 7 and 07 are valid.')
print('*Input "0" to select all dates in the current month.')
print('')
print('*Input ">" to select dates from the next month, i.e. ' + nm + '.')
print('*Input "?" to change the refresh rate. Current refresh rate is ' + str(t) + 's.')
print('')

date_input = input('Select date(s) in ' + cm + ' [d/dd]: ')

if date_input == '?':
    t_overwrite = input('Select refresh rate (in s): ')
    t = float(t_overwrite)
    print('refresh rate set to ' + str(t) + 's')
    print('')
    date_input = input('Select date(s) in ' + cm + ' [d/dd]: ')
    if date_input == '>':
        w = 1
        print('')
        print('Note:')
        print('*Input "?" to change the refresh rate. Current refresh rate is ' + str(t) + 's.')
        print('')
        date_input = input('Select date(s) in ' + nm + ' [d/dd]: ')
        if date_input == '?':
            t_overwrite = input('Select refresh rate (in s): ')
            t = float(t_overwrite)
            print('refresh rate set to ' + str(t) + 's')
            print('')
            date_input = input('Select date(s) in ' + nm + ' [d/dd]: ')
elif date_input == '>':
    w = 1
    print('')
    print('Note:')
    print('*Input "?" to change the refresh rate. Current refresh rate is ' + str(t) + 's.')
    print('')
    date_input = input('Select date(s) in ' + nm + ' [d/dd]: ')
    if date_input == '?':
        t_overwrite = input('Select refresh rate (in s): ')
        t = float(t_overwrite)
        print('refresh rate set to ' + str(t) + 's')
        print('')
        date_input = input('Select date(s) in ' + nm + ' [d/dd]: ')

date_list = date_input.replace(' ','').split(',')
if date_list != ['0']: 
    date_list = [date.lstrip('0') for date in date_list]
date_list = [int(date) for date in date_list]
print('')

if date_list != [0]:
    print('Sessions available:')
    print('A: 0730-0910 *non-peak')
    print('B: 0920-1100')
    print('C: 1130-1310')
    print('D: 1320-1500 *non-peak (last slot for sat/sun)')
    print('E: 1520-1700')
    print('F: 1710-1850 *non-peak')
    print('G: 1920-2100')
    print('H: 2110-2250 *non-peak')
    print('')
    print('Note:')
    print('*Input the letter that is tagged to your desired session time.')
    print('*When selecting more than one session time, separate them with comma(s).')
    print('*Input "0" to select all session times.')
    print('*Input is not case-sensitive.')
    print('')

    i = 1
    rslot_input = input('Select session(s): ').upper()
    if rslot_input == '0':
        i = 0 
        slot_list = [0]
        rslot_list = [0]
    else:
        rslot_str = rslot_input.replace(' ','').translate(slot_dict)
        rslot_list = rslot_str.split(',')
        slot_list = [slot_dict[rslot] for rslot in rslot_list]
else:
    slot_list = [0]
    rslot_list = [0]

dvr = webdriver.Chrome()
dvr.get('https://booking.bbdc.sg/#/booking')

login = dvr.find_element(By.ID, 'input-8')
login.send_keys(kname)
login = dvr.find_element(By.ID, 'input-15')
login.send_keys(kpass)

loginbutton = dvr.find_element(By.CLASS_NAME,'v-btn__content')
loginbutton.click()

ted = datetime.datetime.now()

while True:

    try:
        try:
            dvr.find_element(By.CLASS_NAME, 'v-calendar-monthly')
            break
        except:
            pass

        theorybutton = wait(dvr).until(clickable((By.CLASS_NAME, 'v-tab')))
        practicalbutton = dvr.find_element(locate_with(By.CLASS_NAME,'v-tab').to_right_of(theorybutton))
        wait_spinner()
        while True:
            try:
                practicalbutton.click()
                break
            except:
                tdel = (datetime.datetime.now() - ted).seconds
                if tdel >= 20 * t:
                    raise Exception('Unable to load homepage')

        lesson1_div = wait(dvr).until(visible((By.CLASS_NAME, 'C3Practical')))
        lesson1_div2 = wait(lesson1_div).until(visible((By.TAG_NAME, 'button')))
        lessonbutton1 = wait(lesson1_div2).until(clickable((By.TAG_NAME, 'span')))
        wait_spinner()
        while True:
            try:
                lessonbutton1.click()
                break
            except:
                pass

        try:
            lesson1_div.find_elements(By.CLASS_NAME, 'IndexSessionCard')[1]
            u = 1
        except:
            u = 0

        lesson2_div = wait(dvr).until(visible((By.CLASS_NAME, 'InstrutorTypeList')))
        lessonbutton2 = lesson2_div.find_element(By.CLASS_NAME, 'v-input--selection-controls__ripple')
        wait_spinner()
        while True:
            try:
                lessonbutton2.click()
                break
            except:
                pass

        lesson3_div = dvr.find_element(By.CLASS_NAME, 'v-card__actions')
        lessonbutton3 = wait(lesson3_div).until(clickable((By.TAG_NAME, 'button')))
        while True:
            try:
                lessonbutton3.click()
                break
            except:
                pass

        time.sleep(t)
        dvr.find_element(By.CLASS_NAME, 'v-calendar-monthly')
        break

    except:
        if u == 1:
            dvr.get('https://booking.bbdc.sg/#/booking/chooseSlot?courseType=3C&insInstructorId=&instructorType=')
        else:
            dvr.get('https://booking.bbdc.sg/#/booking/chooseSlot?courseType=3A&insInstructorId=&instructorType=')      

try:
    wait(dvr).until(visible((By.CLASS_NAME, 'v-calendar-monthly')))
except:
    print('exception: not on booking page')
wait_spinner()

while True:
    try:
        calendar = wait(dvr).until(visible((By.CLASS_NAME, 'v-calendar-monthly')))
    except:
        print('exception: not on booking page')
        if u == 1:
            dvr.get('https://booking.bbdc.sg/#/booking/chooseSlot?courseType=3C&insInstructorId=&instructorType=')
        else:
            dvr.get('https://booking.bbdc.sg/#/booking/chooseSlot?courseType=3A&insInstructorId=&instructorType=')
        try: 
            calendar = wait(dvr).until(visible((By.CLASS_NAME, 'v-calendar-monthly')))
        except:
            print('error: unable to load booking page')
            raise Exception('Unable to load booking page')

    try:
        if w == 1:
            ndbutton_div2 = dvr.find_element(By.CLASS_NAME, 'calendar-col')
            ndbutton_div4 = ndbutton_div2.find_elements(By.TAG_NAME, 'button')
            ndbutton = ndbutton_div4[1]
            while True:
                try:
                    ndbutton.click()
                    break
                except:
                    pass
            calendar = wait(dvr).until(visible((By.CLASS_NAME, 'v-calendar-monthly')))
            wait_spinner()
        time.sleep(t)
        datebutton = calendar.find_element(By.TAG_NAME,'button')

        gold_date = int(datebutton.find_element(By.TAG_NAME, 'span').text)

        datebutton = calendar.find_element(By.TAG_NAME, 'button')
        while True:
            try:
                datebutton.click()
                break
            except:
                pass

        wait_spinner()
        slot_div1 = dvr.find_element(By.CLASS_NAME, 'web-view')
        slot_div2 = wait(slot_div1).until(visible((By.CLASS_NAME, 'sessionList')))
        slot_div3 = slot_div2.find_element(By.CLASS_NAME, 'd-none')
        slotbutton = wait(slot_div3).until(clickable((By.CLASS_NAME, 'sessionCard')))

        gold_slot = slotbutton.find_elements(By.TAG_NAME,'p')[1].text
        gold_time = slotbutton.find_elements(By.TAG_NAME, 'p')[2].text

        if date_list == [0]:
            print('desired slot available')
            print('')
            break

        else:
            if gold_date in date_list:
                if i == 0:
                    print('desired slot available')
                    print('')
                    break
                else:
                    if str(gold_slot) in slot_list:
                        print('desired slot available')
                        print('')
                        break
                    else:
                        if gold_date != date_printed and gold_time != time_printed:
                            print('slot found on date: ' + str(gold_date) + '; time: ' + gold_time)
                            date_printed = gold_date
                            time_printed = gold_time
                        raise Exception('Not the desired session')
            else:
                if gold_date != date_printed and gold_time != time_printed:
                    print('slot found on date: ' + str(gold_date) + '; time: ' + gold_time)
                    date_printed = gold_date
                    time_printed = gold_time
                raise Exception('Not the desired date')

    except:
        dvr.refresh()
        tdel = (datetime.datetime.now() - ted).seconds
        if tdel >= 300:
            j += 5
            ted = datetime.datetime.now()
            print(str(j), 'min elapsed')

while True:
    try:
        slotbutton.click()
        break
    except:
        pass

book_div = slot_div1.find_element(By.CLASS_NAME, 'col-right')
bookbutton = book_div.find_element(By.TAG_NAME, 'button')
wait_spinner()
while True:
    try:
        bookbutton.click()
        break
    except:
        pass

while True: 
    try: 
        yin = dvr.find_element(By.CLASS_NAME, 'v-card__actions')
        break
    except:
        pass

yang = yin.find_elements(By.TAG_NAME, 'button')
antihero = yang[1]
success = wait(antihero).until(clickable((By.TAG_NAME, 'span')))
patience = wait(dvr).until(visible((By.CLASS_NAME, 'v-dialog--active')))
wait_spinner()

while True:
    try:
        success.click()
        break
    except:
        pass

status_div = wait(dvr).until(visible((By.CLASS_NAME, 'item-bottom')))
status = (status_div.find_element(By.TAG_NAME, 'p')).text.lower().strip('!.* ').replace('.','')
if status.strip() == 'booking confirmed':
    print('success')
    print('slot booked on date: ' + str(gold_date) + '; time: ' + gold_time)
else:
    print('error:', status)
    print('failed to book slot on date: ' + str(gold_date) + '; time: ' + gold_time)
    if status == 'exceed booking limit (immediate)':
        print('')
        print('Note:')
        print('*BBDC only allows users to book up to a maximum of 18 practical lessons.')
        print('*Cancel at least one of your lessons before running this script again.')
        print('')
    elif status == 'exceed booking limit (last minute)':
        print('')
        print('Note:')
        print('*BBDC only allows users to book up to a maximum of 3 practical lessons in the next 7 days.')
        print('*Cancel at least one of your lessons before running this script again.')
        print('')
    elif status == 'consecutive booking is not allowed':
        print('')
        print('Note:')
        print('*BBDC does not allow users to book back-to-back lessons.')
        print('*Do not select a session time that is immediately before or after one of your lessons.')
        print('')

tdel = (datetime.datetime.now() - ted).seconds
jm = int(tdel // 60)
j += jm
js = int(tdel % 60)
if js == 0:
    print(str(j), 'min elapsed')
elif j == 0:
    print(str(js), 's elapsed')
else:
    print(str(j), 'min', str(js), 's elapsed')
print('')

dvr.close()
dvr.quit()

quit()