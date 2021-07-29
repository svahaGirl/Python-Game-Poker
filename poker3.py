from PyQt5.Widgets import QLabel, QDialog, QPushButton

class InputWindow(QDialog):

    pokerActions = ["Action_1",.....,"Action_n"]

    def __init__(self, parent=None)
    super().__init__()
    self.setUI()

    def setUI(self):
        lblAction = QLabel("Type your Action")
        self.lineAction = QLineEdit()
        self.lineAction.editingFinished.connect(self.sendAction)

        layout = QHBoxLayout()
        layout.addWidget(lblAction)
        layout.addWidget(self.lineAction)
        self.setLayout(layout)


    @pyqtSlot()
    def sendAction(self):
        if self.lineAction.text() not in pockeActions:
            return
        parent.getAction(self.lineAction.text()