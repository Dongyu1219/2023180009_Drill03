from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
boy = load_image('character.png')

def run_top():
    print('TOP')
    pass
def run_right():
    print('RIGHT')
    pass
def run_bottom():
    print('BOTTOM')
    pass
def run_left():
    print('LEFT')
    pass

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

def run_circle():
    print('CIRCLE')

    r, cx, cy =300, 800//2, 600//2  #파이썬은 이렇게 쓴다
    
    '''
    cx = 800//2     #화면의 크기가 800 600이기 때문에 이렇게 쓴다
    cy = 600//2
    '''
    
    for d in range(0,360):   #d 값은 0부터 359까지
        x= r*math.cos(math.radians(d)) + cx
        y= r*math.sin(math.radians(d)) + cy
    
        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.01)

    pass

while True:
    #탑다운 설계(하향식 설계)
    #고수: 함수 호출 -> 함수 정의
    #하수: 함수 정의 -> 함수 호출
    run_circle()
    run_rectangle()
    break
    
close_canvas()
