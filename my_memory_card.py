from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
# from random import shuffle

class Question():
        def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
                self.question = question
                self.right_answer = right_answer
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3

questions_list = [] 
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
        

app = QApplication([])
window = QWidget()
window.setWindowTitle('Викторина')

question = QLabel('Здесь будет вопрос')
btn_OK = QPushButton('Ответить')


RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)



layout_ans1 = QHBoxLayout()  

layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)

layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

# размещаем на горизонтальном лэйауте два вертикальных
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке

# размещаем в группбокс горизонтальный лэйаут с вариантами ответов
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов


# создаем форму ответа
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


# создаем основные лэйауты
layout_line1 = QHBoxLayout() # лэйаут для вопроса
layout_line2 = QHBoxLayout() # лэйаут для вариантов ответов или результат теста
layout_line3 = QHBoxLayout() # лэйаут для кнопки "Ответить"

# размещаем  на лэйаутах вопрос и группбокс с ответами
layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()


# размещаем на лэйауте кнопку и ее форматируем
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)


# Теперь созданные строки разместим друг под другой:
# создаем основной вертикальный лэйаут
layout_card = QVBoxLayout()

# размещаем горизонтальные лэйауты с виджетами на основной и форматируем
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

# размещаем основной лэйаут в окне
window.setLayout(layout_card)
# запускаем приложение

def show_correct(res):
        Ib_Result.setText(res)
        show_result()

def check_answer():
        if answer[0].isChecked():
                show_correct("Правельно")
        else:
                if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
                        show_correct("Неверно")

def next_question():
        window.cur_question += 1
        if window.cur_question >= len(question_list):
                window.cur_question = 0
        q = question_list[window.cur_question]
        ask(q)

def click_Ok():
        if btn_OK.text() == "Ответить":
                check_answer()
        else:
                next_question()

window.cur_question = -1

btn_OK.clicked.connect(click_Ok)

window.show()
app.exec()
