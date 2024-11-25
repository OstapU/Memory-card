from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QHBoxLayout,QVBoxLayout,QPushButton,QLabel

menu_win = QWidget()

lb_quest = QLabel("ВВедіть запитання")
lb_right_ans = QLabel("Введіть вірну відповідь")
lb_wrong_ans1 = QLabel("ВВедіть першу хибну відповідь")
lb_wrong_ans2 = QLabel("ВВедіть другу хибну відповідь")
lb_wrong_ans3 = QLabel("ВВедіть третю хибну відповідь")

le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

lb_header_stat = QLabel("Статистика")
lb_header_stat.setStyleSheet("font_size: 19px; font_weight: bold;")

lb_statick = QLabel()

vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)

vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)

hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_lineEdits)

btn_back = QPushButton('Назад')
btn_add_question = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')
hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_question)
hl_buttons.addWidget(btn_clear)

vl_res= QVBoxLayout()
vl_res.addLayout(hl_question)
vl_res.addLayout(hl_buttons)
vl_res.addWidget(lb_header_stat)
vl_res.addWidget(lb_statick)
vl_res.addWidget(btn_back)

menu_win.setLayout(vl_res)
menu_win.resize(550,450)