import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class ChatClient(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Multi-Port Web Chat Client')
        self.setGeometry(100, 100, 1000, 700)
        self.setMinimumSize(800, 600)

        # Создаем встроенный браузер без лишних рамок и строк ввода URL
        self.browser = QWebEngineView()
        # Подключаемся к нашему серверу
        self.browser.setUrl(QUrl("http://127.0.0.1:5000"))
        
        # Устанавливаем браузер главным элементом окна
        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    print("[Клиент] Запуск графического интерфейса...")
    app = QApplication(sys.argv)
    client = ChatClient()
    client.show()
    sys.exit(app.exec_())
