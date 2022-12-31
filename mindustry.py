from PIL import Image
import win32api
import win32con
import keyboard
import mouse
import clipboard
def getpos():
    return win32api.GetCursorPos()
def clickxy(x,y):
    win32api.SetCursorPos((x,y))
    mouse.click('left')
from time import sleep
from os.path import dirname,realpath
p=dirname(realpath(__file__))+"\\"
size = 88, 88
im = Image.open(p+input("Image name: "))
im_resized = im.resize(size, Image.ANTIALIAS)
data = im_resized.getdata()
start = """sensor b switch1 @enabled
jump 3 equal b 1
end
"""
cmds = [start]*22
proc=0
#draw color 255 255 255 255 0 0
#draw rect 40 40 1 1 0 0
#drawflush display1
x,y=0,175
pixel=0
for (r, g, b) in data:
    cmds[proc] += f"\ndraw color {r} {g} {b} 255 0 0\ndraw rect {2*x} {y} 2 2 0 0"
    if pixel>22 and pixel//22%10==0:
        cmds[proc] += "\ndrawflush display1"
    x+=1
    if x>=88:
        x=0
        y-=2
    proc+=1
    pixel+=1
    if proc>21: proc=0
print("Done creating commands")
for i in range(22):
    print(f"Command {i+1}")
    clipboard.copy(cmds[i]+"\ndrawflush display1")
    while not keyboard.is_pressed('esc'): 
        pass
    sleep(0.6)
   