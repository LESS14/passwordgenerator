import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QSpinBox, QMenuBar, QMenu, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gerador de Senhas Fortes")
        self.setGeometry(200, 200, 400, 200)

        self.set_style()

        self.create_menu()

        layout = QVBoxLayout()

        self.password_label = QLabel("Senha gerada:")
        layout.addWidget(self.password_label)

        self.password_field = QLineEdit()
        self.password_field.setReadOnly(True)
        self.password_field.setStyleSheet("QLineEdit { color: black; background-color: white; }")
        layout.addWidget(self.password_field)

        self.include_numbers = QCheckBox("Incluir números")
        self.include_numbers.setChecked(True)
        layout.addWidget(self.include_numbers)

        self.include_uppercase = QCheckBox("Incluir letras maiúsculas")
        self.include_uppercase.setChecked(True)
        layout.addWidget(self.include_uppercase)

        self.include_symbols = QCheckBox("Incluir símbolos")
        self.include_symbols.setChecked(True)
        layout.addWidget(self.include_symbols)

        self.password_length_label = QLabel("Tamanho da senha:")
        layout.addWidget(self.password_length_label)

        self.password_length_spinbox = QSpinBox()
        self.password_length_spinbox.setMinimum(10)
        self.password_length_spinbox.setMaximum(36)
        self.password_length_spinbox.setValue(12)
        layout.addWidget(self.password_length_spinbox)

        self.generate_button = QPushButton("Gerar Senha")
        self.generate_button.clicked.connect(self.generate_password)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def set_style(self):
        app_palette = QPalette()
        app_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        app_palette.setColor(QPalette.WindowText, Qt.white)
        app_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        app_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        app_palette.setColor(QPalette.ToolTipBase, Qt.white)
        app_palette.setColor(QPalette.ToolTipText, Qt.white)
        app_palette.setColor(QPalette.Text, Qt.white)
        app_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        app_palette.setColor(QPalette.ButtonText, Qt.white)
        app_palette.setColor(QPalette.BrightText, Qt.red)
        app_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        app_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        app_palette.setColor(QPalette.HighlightedText, Qt.black)

        self.setPalette(app_palette)

    def create_menu(self):
        menubar = QMenuBar(self)
        menubar.setStyleSheet("QMenuBar { background-color: #353535; color: white; }")

        file_menu = menubar.addMenu("Arquivo")

        close_action = QAction("Fechar", self)
        close_action.triggered.connect(self.close_app)
        file_menu.addAction(close_action)

    def generate_password(self):
        tamanho = self.password_length_spinbox.value()
        incluir_numeros = self.include_numbers.isChecked()
        incluir_maiusculas = self.include_uppercase.isChecked()
        incluir_simbolos = self.include_symbols.isChecked()

        caracteres = string.ascii_lowercase
        if incluir_numeros:
            caracteres += string.digits
        if incluir_maiusculas:
            caracteres += string.ascii_uppercase
        if incluir_simbolos:
            caracteres += string.punctuation

        senha_gerada = ''.join(random.choice(caracteres) for _ in range(tamanho))
        self.password_field.setText(senha_gerada)

    def close_app(self):
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
