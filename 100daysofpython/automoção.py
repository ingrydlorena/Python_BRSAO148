import pyautogui as p
p.PAUSE = 2
v = 5
while True:
    if v <= 100:
        p.click(x=134, y=83)
        v += 1
        p.write('Day'+ str(v) +  '.py')
        p.press('enter')
        
    else:
        break