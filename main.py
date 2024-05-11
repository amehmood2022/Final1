import sys
from PyQt6.QtWidgets import QApplication, QDialog
from gui import Ui_FinalVote
from logic import VotingLogic

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = QDialog()
    ui = Ui_FinalVote()
    ui.setupUi(dialog)
    logic = VotingLogic(ui)
    dialog.show()
    sys.exit(app.exec())