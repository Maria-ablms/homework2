from PyQt6.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QLabel, QPushButton
from modules.app import app
from PyQt6.QtCore import Qt



main_window = QMainWindow()



WIDTH_WINDOW = 650
HEIGHT_WINDOW = 800

primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
width_screen = screen_size.width()
height_screen = screen_size.height()


main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2), 
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, 
    HEIGHT_WINDOW
)


main_frame = QFrame(main_window)
main_frame.setStyleSheet("background-color: #FFB6C1;")
main_frame.setFixedSize(WIDTH_WINDOW, HEIGHT_WINDOW)

main_layout = QVBoxLayout(main_frame)
main_layout.setContentsMargins(30,50,30,30)
main_layout.setSpacing(15)

button_counter = [0]

counter_label = QLabel("0", parent=main_frame)
counter_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
counter_label.setStyleSheet("font-size: 40px;" "color: white;" "font-weight: bold;" "background: transparent;")


def click_plus():
     button_counter[0] += 1   
     counter_label.setText(f"{button_counter[0]}")            
def click_minus(): 
    button_counter[0] -= 1
    counter_label.setText(f"{button_counter[0]}")                   
def click_reset(): 
    button_counter[0] = 0  
    counter_label.setText(f"{button_counter[0]}")                 



button_plus = QPushButton("+", parent=main_frame) 
button_plus.clicked.connect(click_plus)

button_minus = QPushButton("-", parent=main_frame) 
button_minus.clicked.connect(click_minus)

button_reset = QPushButton("reset", parent=main_frame) 
button_reset.clicked.connect(click_reset)


button_style = "QPushButton { background-color: #FFD700; color: white; border-radius: 6px; font-size: 24px; padding: 20px; }"

button_plus.setStyleSheet(button_style) 
button_minus.setStyleSheet(button_style) 
button_reset.setStyleSheet(button_style)

main_layout.addWidget(counter_label,) 
main_layout.addWidget(button_plus) 
main_layout.addWidget(button_minus) 
main_layout.addWidget(button_reset)

main_frame.setLayout(main_layout)














# main_frame.setLayout(main_layout)


# primary_button = QPushButton("0", parent= main_frame)
# main_layout.addWidget(primary_button)
# primary_button.setStyleSheet("font_size: 36px, border: 20 px, solid, green; padding:50px; background-color: #FFB6C1; color: white")

# button_1 = QPushButton("+", parent= main_frame,)
# main_layout.addWidget(primary_button)
# button_1.setStyleSheet("border: 2px, solid, #007BA7, background-color: #40E0D0,  color: #00008B")










# list1= ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
# list2 = ["-10", "-9", "-8", "-7", "-6", "-5", "-4", "-3", "-2", "-1"]










# def click():
#     print("hello")

# button.clicked.connect(click)

# def enter_text(text):
#     print(text)

# linein = QLineEdit(parent= main_frame)
# main_layout.addWidget(linein)
# linein.setPlaceholderText("eneter something")
# linein.setStyleSheet("color: white, background-color: white")
# linein.textChanged.connect(enter_text)