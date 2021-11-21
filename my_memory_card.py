#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QButtonGroup, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox
from random import shuffle, randint

app = QApplication([])


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Какова формула воды?', 'H2O', 'CO2', 'O2', 'Её не существует'))
questions_list.append(Question('Всемирная паутина коммуникаций', 'Интернет', 'WiFi', 'Вебсайт', 'WhatsApp'))
questions_list.append(Question('Самая "дешёвая" компания телефонов и не только', 'Apple', 'Samsung', 'Xiaomi', 'Huawei'))

btn_Ok = QPushButton('Ответить')


quest = QLabel('Какова формула воды?')
RadioGroupBox = QGroupBox('Варианты ответов')

btn1 = QRadioButton('CO2')
btn2 = QRadioButton('H2O')
btn3 = QRadioButton('O2')
btn4 = QRadioButton('Её не существует')

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(btn1)
layout_ans2.addWidget(btn2)
layout_ans3.addWidget(btn3)
layout_ans3.addWidget(btn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
#форма ответа
AnsGroupBox = QGroupBox('Результаты теста')
lb_res = QLabel('Правильно/Неправильно')
lb_cor = QLabel('H2O')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_res, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_cor, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(quest, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_Ok, stretch = 2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_Ok.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    
    btn_Ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)



answers = [btn1, btn2, btn3, btn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    quest.setText(q.question)
    lb_cor.setText(q.right_answer)
    show_question()

def next_question():
    mw.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    print('Статистика\n-Всего вопросов:', mw.total, '\n-Правильных ответов:', mw.score)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_Ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()


def show_correct(res):
    lb_res.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        mw.score += 1
        print('Статистика\n-Всего вопросов:', mw.total, '\n-Правильных ответов:', mw.score)
        print('Рейтинг: ', (mw.score/mw.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('Рейтинг: ', (mw.score/mw.total*100), '%')
mw = QWidget()
mw.setLayout(layout_card)
mw.setWindowTitle('Memory Card')


btn_Ok.clicked.connect(click_OK)
mw.total = 0
mw.score = 0
next_question()
mw.resize(400, 300)
mw.show()
app.exec_()