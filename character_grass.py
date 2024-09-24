from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.001)
    
def run_top():
    print('TOP')
    for x in range(0, 700):
        draw_boy(x,550)
    pass
def run_right():
    print('RIGHT')
    for y in range(550, 0, -1):
        draw_boy(700, y)
    pass
def run_bottom():
    print('BOTTOM')
    for x in range(700 , 0 , -1):
        draw_boy(x ,0)
    pass
def run_left():
    print('LEFT')
    for y in range(0, 550):
        draw_boy(0, y)
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
        draw_boy(x, y)

    pass

while True:
    #탑다운 설계(하향식 설계)
    #고수: 함수 호출 -> 함수 정의
    #하수: 함수 정의 -> 함수 호출
    run_circle()
    run_rectangle()
    run_triangle()
    break
    
close_canvas()
