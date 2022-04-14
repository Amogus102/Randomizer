from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QGroupBox, QButtonGroup
from random import shuffle, randint
class Question():
        def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
            self.question = question
            self.right_answer = right_answer
            self.wrong1 = wrong1
            self.wrong2 = wrong2
            self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Сколько хромосом у человека?', '1', '17', '23', '47'))
questions_list.append(Question('Сколько у меня учебников?', '1', '2', '15', '37'))
questions_list.append(Question('Каким способом можно рассплавить предмет?', 'Вскипятить', 'Заморозить', 'Высушить', 'Сильно нагреть'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
question = QLabel('Какой национальности не существует?')
btn_OK = QPushButton('Ответить')
RadioGroupBox = QGroupBox("Варианты ответов")
rbtn1 = QRadioButton('Энцы')
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
layout_ans1 =QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout() 
layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет здесь!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment= (Qt.AlignHCenter | Qt.AlignVCenter))
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 

layout_line1.addWidget(question, alignment=Qt.AlignCenter)
layout_line1.addWidget(question, alignment= (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)


layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [rbtn1, rbtn2, rbtn3, rbtn4]
def ask(q: Question):
    shuffle(answer)
    answer[0].setText((q.right_answer))
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Result.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистик\n-Всего вопросов:', main_win.total, '\n-Правильных ответов', window.score) 
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (main_win.score/main_win.total*100), '%')




def next_question():
    main_win.total += 1
    print('Статистика:\n-Всего вопросов:', main_win.total, '\n-Правильных ответов', main_win.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()





main_win.score = 0
main_win.total = 0
btn_OK.clicked.connect(click_OK)
next_question()
main_win.setLayout(layout_card)
main_win.show()
app.exec()