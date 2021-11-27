

import math
import turtle
import tkinter

from math import *

def draw_function():
    turtle.pencolor('blue')
    turtle.pensize(3)
    formula = entry_formula.get()

    # 그래프 그리는 초기 위치로 이동
    turtle.penup()
    magnify = axis_size / int(entry_x_width.get())  # 정의역에 따른 그래프 확대 배율

    initial_x = float(entry_x_width.get())    # x 좌표 초기값

    x = initial_x   # eval 함수를 쓰기 위해 x 에 x 좌표 초기값을 입력
    y = eval(formula)

    turtle.goto(magnify*x, magnify*y)
    turtle.pendown()
    resolution = 100    # 해상도, 그래프 위의 점의 개수

    for n in range(resolution+1):
        x = initial_x * (1 - 2*n/resolution)    # 증가하는 x좌표값
        try: y = eval(formula)
        except: continue
        turtle.goto(magnify*x, magnify*y)

    # 좌표값 입력
    turtle.pencolor('black')
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(-axis_size, -30)
    turtle.write(-initial_x, False, 'center', ('', 15))
    turtle.goto(-20, -30)
    turtle.write(0, False, 'center', ('', 15))
    turtle.goto(axis_size, -30)
    turtle.write(initial_x, False, 'center', ('', 15))
    turtle.goto(-30, axis_size)
    turtle.write(initial_x, False, 'center', ('', 15))
    turtle.goto(-30, -axis_size)
    turtle.write(-initial_x, False, 'center', ('', 15))


def clear():
    turtle.reset()
    turtle.speed(speed)
    turtle.hideturtle()
    entry_x_width.delete(0, tkinter.END)
    entry_formula.delete(0, tkinter.END)
    draw_axis()


# 좌표축 그리기
def draw_axis():
    for i in range(5):
        turtle.setheading(90 * i)
        turtle.forward(axis_size)
        turtle.home()


# 기본 설정
axis_size = 350
speed = 0
turtle.speed(speed)
turtle.hideturtle()
draw_axis()


# tkinter 라벨, 엔트리, 버튼 등 설정
window = turtle.getcanvas()
frame_title = tkinter.Frame(window)
frame_title.grid(row=1, column=0)
frame_bottom = tkinter.Frame(window)
frame_bottom.grid(row=2, column=0)

label_text = '함수 정의역 변수:x, log(x,base) 거듭제곱:**,  곱하기 생략 불가 ex) x**2, log2(x) or log(x,3),sin(x)'
tkinter.Label(frame_title, text=label_text).grid(row=0, column=0)
tkinter.Label(frame_bottom, text='함수 y=').grid(row=0, column=0)
entry_formula = tkinter.Entry(frame_bottom, width=20)
entry_formula.grid(row=0, column=1, padx=10, pady=10)

tkinter.Label(frame_bottom, text='    정의역의 범위  : ').grid(row=0, column=2)
entry_x_width = tkinter.Entry(frame_bottom, width=10)
entry_x_width.grid(row=0, column=3)

tkinter.Button(frame_bottom, text='실행', command=draw_function).grid(row=0, column=4, padx=20)
tkinter.Button(frame_bottom, text='초기화', command=clear).grid(row=0, column=5, padx=20)

turtle.done()
