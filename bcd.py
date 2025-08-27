import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait(parent):
    return WebDriverWait(parent, 15)
def clickable(element):
    return EC.element_to_be_clickable(element)
def visible(element):
    return EC.visibility_of_element_located(element)
def invisible(element):
    return EC.invisibility_of_element_located(element)

def wait_spinner():
    wait(dvr).until(invisible((By.CLASS_NAME, 'v-overlay__content')))

kname = '<username>' # insert username here
kpass = '<password>' # insert password here

j = 0
k = 0 # set at 0 for live run, 1 for test run, or 2 for timed run
t = 1.5 # refresh speed
u = 10 # timed run duration

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
if k != 0 :
    print('WARNING: Check bot settings.')
    print('')

print('Note:')
print('*When selecting more than one date, separate them with comma(s).')
print('*Input "0" to select all dates in the current month.')
print('')

date_input = input('Select date(s) [d/dd]: ')
date_list = date_input.replace(' ','').split(',')
if date_list != ['0'] : 
    date_list = [date.lstrip('0') for date in date_list]
date_list = [int(date) for date in date_list]
print('')

if date_list != [0] :
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

theorybutton = wait(dvr).until(clickable((By.CLASS_NAME, 'v-tab')))
practicalbutton = dvr.find_element(locate_with(By.CLASS_NAME,'v-tab').to_right_of(theorybutton))
wait_spinner()
while True:
    try:
        practicalbutton.click()
        break
    except:
        print('exception: practicalbutton')

lesson1_div = wait(dvr).until(visible((By.CLASS_NAME, 'C3Practical')))
lesson1_div2 = wait(lesson1_div).until(visible((By.TAG_NAME, 'button')))
lessonbutton1 = wait(lesson1_div2).until(clickable((By.TAG_NAME, 'span')))
wait_spinner()
while True:
    try:
        lessonbutton1.click()
        break
    except:
        print('exception: lessonbutton1')

lesson2_div = wait(dvr).until(visible((By.CLASS_NAME, 'InstrutorTypeList')))
lessonbutton2 = lesson2_div.find_element(By.CLASS_NAME, 'v-input--selection-controls__ripple')
wait_spinner()
while True:
    try:
        lessonbutton2.click()
        break
    except:
        print('exception: lessonbutton2')

lesson3_div= dvr.find_element(By.CLASS_NAME, 'v-card__actions')
lessonbutton3 = wait(lesson3_div).until(clickable((By.TAG_NAME, 'button')))
while True:
    try:
        lessonbutton3.click()
        break
    except:
        print('exception: lessonbutton3')
    
try:
    wait(dvr).until(visible((By.CLASS_NAME, 'v-calendar-monthly')))
except:
    print('exception: not on booking page')
wait_spinner()

if k == 1:
    time.sleep(5)
    print('test parameters set')
    print('')

while True:
    calendar = wait(dvr).until(visible((By.CLASS_NAME, 'v-calendar-monthly')))

    try:
        time.sleep(t)
        datebutton = calendar.find_element(By.TAG_NAME,'button')

        gold_date = int(datebutton.find_element(By.TAG_NAME, 'span').text)

        datebutton = calendar.find_element(By.TAG_NAME, 'button')
        while True:
            try:
                datebutton.click()
                break
            except:
                print('exception: datebutton')

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
                    if str(gold_slot) in slot_list :
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
                if gold_date != date_printed and gold_time != time_printed :
                    print('slot found on date: ' + str(gold_date) + '; time: ' + gold_time)
                    date_printed = gold_date
                    time_printed = gold_time
                raise Exception('Not the desired date')

    except:
        dvr.refresh()
        j += t
        jm = int(j // 60)
        js = int(j % 60)
        if jm % 5 == 0 and js == 0 :
            print (str(jm), 'min elapsed')
        if j >= u and k == 2 :
            dvr.close()
            dvr.quit ()
            print('')
            print ('timed run completed')
            quit()

while True:
    try:
        slotbutton.click()
        break
    except:
        print('exception: slotbutton')

book_div = slot_div1.find_element(By.CLASS_NAME, 'col-right')
bookbutton = book_div.find_element(By.TAG_NAME, 'button')
wait_spinner()
while True:
    try:
        bookbutton.click()
        break
    except:
        print('exception: bookbutton')

yin = wait(dvr).until(visible((By.CLASS_NAME, 'v-card__actions')))
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
        print('exception: success')

print('success')
print('slot booked on date: ' + str(gold_date) + '; time: ' + gold_time)
if js == 0:
    print(str(jm), 'min elapsed')
else:
    print(str(jm), 'min', str(js), 'sec elapsed')
print('')
time.sleep(5)

dvr.close()
dvr.quit()


quit()
