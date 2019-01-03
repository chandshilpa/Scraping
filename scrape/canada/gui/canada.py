from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import time
import _thread as thread
import webbrowser
import os

class RequireValueException(Exception):
    pass

class Ui_MainWindow(object):

    currentDirectory = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):
        directory = Ui_MainWindow.currentDirectory
        _dir = os.path.join(directory, 'contacts')
        if not os.path.exists(_dir):
            os.makedirs(_dir)

    def BrowserBtn(self):
        webbrowser.open("file://" + Ui_MainWindow.currentDirectory + "/contacts")

    def process(self, nameInput, addressInput, csvInput):
        try:
            if nameInput.strip() == "":
                raise RequireValueException("Name Required")
            elif addressInput.strip() == "":
                raise RequireValueException("Address Required")
            elif csvInput.strip() == Ui_MainWindow.currentDirectory + "/contacts/":
                raise RequireValueException("Please specify output file name")

            path = "cmain.exe --name {} --location {} --output {}".format(nameInput, addressInput, csvInput)
            out = subprocess.Popen(path, stdout=subprocess.PIPE,
                                           stderr=subprocess.STDOUT)
            stdout, stderr = out.communicate()
            outputstring = str(stdout).split("No more records found. ")
            outputstring = outputstring[1]
            outputstring = outputstring.split(".")
            outputstring = outputstring[0]

            #print(outputstring)
            self.outputLable.setText(str(outputstring))
            self.progressBar.hide()
            enable = self.openOutputFile.setEnabled(True)

        except RequireValueException as e:
            outputstring = e

            #print(outputstring)
            self.outputLable.setText(str(outputstring))
            self.progressBar.hide()
            enable = self.openOutputFile.setEnabled(False)

        except:
            outputstring = "There is an unknown error. Please Check your Internet Connection."

            #print(outputstring)
            self.outputLable.setText(str(outputstring))
            self.progressBar.hide()
            enable = self.openOutputFile.setEnabled(False)



    def processBtnAction(self):
        nameInput = self.nameInput.text()
        addressInput = self.addressInput.text()
        # streetInput = self.streetInput.text()
        csvInput = Ui_MainWindow.currentDirectory + "/contacts/" + self.outputInput.text()
        self.progress()
        ## starting thread
        thread.start_new_thread(self.process, (nameInput, addressInput, csvInput, ))

    def progress(self):
        self.progressBar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_5.addWidget(self.progressBar, 0, 0, 1, 1)
        self.progressBar.show()

    """def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Tab:
            self.parent().focusNextChild()
        elif event.key() == QtCore.Qt.Key_Backtab:
            self.parent().focusPrevChild()"""

    """def focus_next_window(event):
        event.widget.tk_focusNext().focus()
        return ("break")

    text_widget = Text(...)
    text_widget.bind("<Tab>", focus_next_window)"""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 398)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../image.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 1, 1, 1)
        self.outputInput = QtWidgets.QLineEdit(self.frame)
        self.outputInput.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.outputInput.setObjectName("outputInput")
        self.gridLayout_2.addWidget(self.outputInput, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setEnabled(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.PhoneInput = QtWidgets.QLineEdit(self.frame)
        self.PhoneInput.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.PhoneInput.setObjectName("PhoneInput")
        self.gridLayout_2.addWidget(self.PhoneInput, 4, 0, 1, 1)
        self.addressInput = QtWidgets.QLineEdit(self.frame)
        self.addressInput.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.addressInput.setObjectName("addressInput")
        self.gridLayout_2.addWidget(self.addressInput, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.nameInput = QtWidgets.QLineEdit(self.frame)
        self.nameInput.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nameInput.setClearButtonEnabled(False)
        self.nameInput.setObjectName("nameInput")
        self.gridLayout_2.addWidget(self.nameInput, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.processButton = QtWidgets.QPushButton(self.frame)
        self.processButton.setObjectName("processButton")

        self.processButton.clicked.connect(self.processBtnAction)

        self.gridLayout_3.addWidget(self.processButton, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 570, 104))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")


        """self.outputLable = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.outputLable.setText("                        ")
        self.outputLable.setObjectName("outputLable")"""
        self.outputLable=QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.outputLable.setObjectName("outputLable")
        self.gridLayout_5.addWidget(self.outputLable, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.openOutputFile = QtWidgets.QPushButton(self.frame_2)
        self.openOutputFile.setEnabled(False)
        self.openOutputFile.setObjectName("openOutputFile")

        self.openOutputFile.clicked.connect(self.BrowserBtn)

        self.verticalLayout_2.addWidget(self.openOutputFile)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contact Finder"))
        self.label_4.setText(_translate("MainWindow", "Phone"))
        self.label_5.setText(_translate("MainWindow", "Output File Name"))
        self.outputInput.setPlaceholderText(_translate("MainWindow", "Enter Output File Name with .csv"))
        self.label_3.setText(_translate("MainWindow", "address"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Contact Finder</span></p></body></html>"))
        self.PhoneInput.setPlaceholderText(_translate("MainWindow", "Enter Phone no. to be specific (Optional)"))
        self.addressInput.setPlaceholderText(_translate("MainWindow", "Enter Address to find contact from"))
        self.label_2.setText(_translate("MainWindow", "name"))
        self.nameInput.setPlaceholderText(_translate("MainWindow", "Enter Name to find names with"))
        self.processButton.setText(_translate("MainWindow", "Process"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Output</span></p></body></html>"))
        self.openOutputFile.setText(_translate("MainWindow", "Open Output File Location"))
        self.label_7.setText(_translate("MainWindow", "Powered By - Ftechiz Solutions"))
        self.outputLable.setText(_translate("MainWindow",
                                        "                                                                                                    "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

