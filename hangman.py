from view import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
import random
    
###Main function
class Controller(QMainWindow, Ui_window):

    correct_word = ""
    wrong_counter = 0
    right_counter = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        
        ###Easy word list
        self.wordList = ['one','two','six','four','five','nine','three','seven','eight']

        ###Medium word list
        #self.mediumList = ['four','five','nine']

        ###Hard word list
        #self.hardList = ['three','seven','eight']

        ############################################################################
        self.label_pic.setStyleSheet('background-image : url(images/h1.png)')
        
        self.pushButton_a.clicked.connect(lambda: self.button_clicked('a'))
        self.pushButton_b.clicked.connect(lambda: self.button_clicked('b'))
        self.pushButton_c.clicked.connect(lambda: self.button_clicked('c'))
        self.pushButton_d.clicked.connect(lambda: self.button_clicked('d'))
        self.pushButton_e.clicked.connect(lambda: self.button_clicked('e'))
        self.pushButton_f.clicked.connect(lambda: self.button_clicked('f'))
        self.pushButton_g.clicked.connect(lambda: self.button_clicked('g'))
        self.pushButton_h.clicked.connect(lambda: self.button_clicked('h'))
        self.pushButton_i.clicked.connect(lambda: self.button_clicked('i'))
        self.pushButton_j.clicked.connect(lambda: self.button_clicked('j'))
        self.pushButton_k.clicked.connect(lambda: self.button_clicked('k'))
        self.pushButton_l.clicked.connect(lambda: self.button_clicked('l'))
        self.pushButton_m.clicked.connect(lambda: self.button_clicked('m'))
        self.pushButton_n.clicked.connect(lambda: self.button_clicked('n'))
        self.pushButton_o.clicked.connect(lambda: self.button_clicked('o'))
        self.pushButton_p.clicked.connect(lambda: self.button_clicked('p'))
        self.pushButton_q.clicked.connect(lambda: self.button_clicked('q'))
        self.pushButton_r.clicked.connect(lambda: self.button_clicked('r'))
        self.pushButton_s.clicked.connect(lambda: self.button_clicked('s'))
        self.pushButton_t.clicked.connect(lambda: self.button_clicked('t'))
        self.pushButton_u.clicked.connect(lambda: self.button_clicked('u'))
        self.pushButton_v.clicked.connect(lambda: self.button_clicked('v'))
        self.pushButton_w.clicked.connect(lambda: self.button_clicked('w'))
        self.pushButton_x.clicked.connect(lambda: self.button_clicked('x'))
        self.pushButton_y.clicked.connect(lambda: self.button_clicked('y'))
        self.pushButton_z.clicked.connect(lambda: self.button_clicked('z'))
        self.pushButton_new.clicked.connect(lambda: self.reset())
        self.levels()
        #self.pushButton_new.clicked.connect(lambda: self.new_game())

    def reset(self):
        Controller.correct_word = ""
        Controller.wrong_counter = 0
        Controller.right_counter = 0
        self.label_wrong.setText(f'Wrong: {str(Controller.wrong_counter)}')
        self.label_right.setText(f'Right: {str(Controller.right_counter)}')
        self.keys_shown()
        self.levels()

    def keys_shown(self):
        self.pushButton_a.setHidden(False)
        self.pushButton_b.setHidden(False)
        self.pushButton_c.setHidden(False)
        self.pushButton_d.setHidden(False)
        self.pushButton_e.setHidden(False)
        self.pushButton_f.setHidden(False)
        self.pushButton_g.setHidden(False)
        self.pushButton_h.setHidden(False)
        self.pushButton_i.setHidden(False)
        self.pushButton_j.setHidden(False)
        self.pushButton_k.setHidden(False)
        self.pushButton_l.setHidden(False)
        self.pushButton_m.setHidden(False)
        self.pushButton_n.setHidden(False)
        self.pushButton_o.setHidden(False)
        self.pushButton_p.setHidden(False)
        self.pushButton_q.setHidden(False)
        self.pushButton_r.setHidden(False)
        self.pushButton_s.setHidden(False)
        self.pushButton_t.setHidden(False)
        self.pushButton_u.setHidden(False)
        self.pushButton_v.setHidden(False)
        self.pushButton_w.setHidden(False)
        self.pushButton_x.setHidden(False)
        self.pushButton_y.setHidden(False)
        self.pushButton_z.setHidden(False)

    def levels(self):
        #self.pushButton_new.setHidden(True)
        Controller.correct_word = random.choice(self.wordList)
        print(Controller.correct_word)
        self.words()

    def words(self):
        self.word = '*'* len(Controller.correct_word)
        self.label_guessed_letters.setText(self.word)
        # Hide all letter keys
    def keys_hidden(self):
        self.pushButton_a.setHidden(True)
        self.pushButton_b.setHidden(True)
        self.pushButton_c.setHidden(True)
        self.pushButton_d.setHidden(True)
        self.pushButton_e.setHidden(True)
        self.pushButton_f.setHidden(True)
        self.pushButton_g.setHidden(True)
        self.pushButton_h.setHidden(True)
        self.pushButton_i.setHidden(True)
        self.pushButton_j.setHidden(True)
        self.pushButton_k.setHidden(True)
        self.pushButton_l.setHidden(True)
        self.pushButton_m.setHidden(True)
        self.pushButton_n.setHidden(True)
        self.pushButton_o.setHidden(True)
        self.pushButton_p.setHidden(True)
        self.pushButton_q.setHidden(True)
        self.pushButton_r.setHidden(True)
        self.pushButton_s.setHidden(True)
        self.pushButton_t.setHidden(True)
        self.pushButton_u.setHidden(True)
        self.pushButton_v.setHidden(True)
        self.pushButton_w.setHidden(True)
        self.pushButton_x.setHidden(True)
        self.pushButton_y.setHidden(True)
        self.pushButton_z.setHidden(True)
    def button_clicked(self, guess_letter):
        ### disable letters after clicked
        if guess_letter == 'a':
            self.pushButton_a.setHidden(True)
        if guess_letter == 'b':
            self.pushButton_b.setHidden(True)
        if guess_letter == 'c':
            self.pushButton_c.setHidden(True)
        if guess_letter == 'd':
            self.pushButton_d.setHidden(True)
        if guess_letter == 'e':
            self.pushButton_e.setHidden(True)
        if guess_letter == 'f':
            self.pushButton_f.setHidden(True)
        if guess_letter == 'g':
            self.pushButton_g.setHidden(True)
        if guess_letter == 'h':
            self.pushButton_h.setHidden(True)
        if guess_letter == 'i':
            self.pushButton_i.setHidden(True)
        if guess_letter == 'j':
            self.pushButton_j.setHidden(True)
        if guess_letter == 'k':
            self.pushButton_k.setHidden(True)
        if guess_letter == 'l':
            self.pushButton_l.setHidden(True)
        if guess_letter == 'm':
            self.pushButton_m.setHidden(True)
        if guess_letter == 'n':
            self.pushButton_n.setHidden(True)
        if guess_letter == 'o':
            self.pushButton_o.setHidden(True)
        if guess_letter == 'p':
            self.pushButton_p.setHidden(True)
        if guess_letter == 'q':
            self.pushButton_q.setHidden(True)
        if guess_letter == 'r':
            self.pushButton_r.setHidden(True)
        if guess_letter == 's':
            self.pushButton_s.setHidden(True)
        if guess_letter == 't':
            self.pushButton_t.setHidden(True)
        if guess_letter == 'u':
            self.pushButton_u.setHidden(True)
        if guess_letter == 'v':
            self.pushButton_v.setHidden(True)
        if guess_letter == 'w':
            self.pushButton_w.setHidden(True)
        if guess_letter == 'x':
            self.pushButton_x.setHidden(True)
        if guess_letter == 'y':
            self.pushButton_y.setHidden(True)
        if guess_letter == 'z':
            self.pushButton_z.setHidden(True)
        ### guessed correct
        if guess_letter in Controller.correct_word:
            Controller.right_counter += Controller.correct_word.count(guess_letter)
            print(Controller.right_counter)

            position = Controller.correct_word.find(guess_letter, 0)
            while position != -1:  # -1 means not found
                # Place letter in position
                self.word = self.word[:position] + guess_letter + self.word[position + 1:]
                # Search for next occurrence
                position = Controller.correct_word.find(guess_letter, position + 1)
            if Controller.right_counter == len(Controller.correct_word):
                self.label_guessed_letters.setText(self.word +'--You won!')
                self.keys_hidden()
                self.pushButton_new.show()
            else:
                self.label_guessed_letters.setText(self.word)
        ###guessed wrong
        else:
            Controller.wrong_counter +=1
            if Controller.wrong_counter == 1:
                self.label_pic.setStyleSheet('background-image : url(images/h2.png)')
            elif Controller.wrong_counter == 2:
                self.label_pic.setStyleSheet('background-image : url(images/h3.png)')
            elif Controller.wrong_counter == 3:
                self.label_pic.setStyleSheet('background-image : url(images/h4.png)')
            elif Controller.wrong_counter == 4:
                self.label_pic.setStyleSheet('background-image : url(images/h5.png)')
            elif Controller.wrong_counter == 5:
                self.label_pic.setStyleSheet('background-image : url(images/h6.png)')
            elif Controller.wrong_counter == 6:
                self.label_pic.setStyleSheet('background-image : url(images/h7.png)')
                self.label_guessed_letters.setText(self.word +'--You Lost!')
                self.keys_hidden()
                self.pushButton_new.show()

        self.label_wrong.setText(f'Wrong: {str(Controller.wrong_counter)}')
        self.label_right.setText(f'Right: {str(Controller.right_counter)}')

        #######################################################################################
   