from pico2d import *

#실행 가능한 큰 뻐대를 먼저 만든다.
#실행가능하다면 커밋한다.
#무한 루프 맞는지 확인한다.
#실행 된다면 커밋한다.
def run_rectangle():
    print('RECTANGLE')
    pass

def run_circle():
    print('CIRCLE')
    pass


open_canvas()

# fill here
grass = load_image('grass.png')
boy = load_image('character.png')

while True:
    #탑다운 설계(하향식 설계)
    #고수: 함수 호출 -> 함수 정의
    #하수: 함수 정의 -> 함수 호출
    run_circle()
    run_rectangle()
    
close_canvas()
