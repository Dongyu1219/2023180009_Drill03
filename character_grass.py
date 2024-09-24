from pico2d import *

open_canvas()

# fill here
grass = load_image('grass.png')
boy = load_image('character.png')

def run_rectangle():
    print('RECTANGLE')
    pass

def run_circle():
    print('CIRCLE')

    clear_canvas_now()
    boy.draw_now(400, 300)
    delay(1)

    
    pass

while True:
    #탑다운 설계(하향식 설계)
    #고수: 함수 호출 -> 함수 정의
    #하수: 함수 정의 -> 함수 호출
    run_circle()
    run_rectangle()
    break
    
close_canvas()
