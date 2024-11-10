from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget, QPushButton, QMenu, QAction
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon, QClipboard
import sys
import Query
import PyqtFormModel
import subprocess

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗体标题
        self.setWindowTitle("僵尸乐园登录器（暂时）    ——By 717qwq")

        # 设置窗口图标
        self.setWindowIcon(QIcon('./icon.ico'))  # 替换为你的图标文件路径

        # 获取服务器信息
        server_info = Query.ZombiEden_Server_Query() + Query.EXG_Server_Query()

        # 创建模型
        self.model = PyqtFormModel.ServerInfoModel(server_info)

        # 创建视图
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        # 设置选择模式为行选择
        self.table_view.setSelectionMode(QTableView.SingleSelection)
        self.table_view.setSelectionBehavior(QTableView.SelectRows)

        # 连接选择变化信号
        self.table_view.selectionModel().selectionChanged.connect(self.on_selection_changed)

        # 创建按钮
        self.refresh_button = QPushButton('刷新')
        self.exit_button = QPushButton('退出')

        # 连接按钮点击事件
        self.refresh_button.clicked.connect(self.on_refresh)
        self.exit_button.clicked.connect(self.close)

        # 创建布局
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.exit_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table_view)
        main_layout.addLayout(button_layout)

        # 设置中央窗口小部件
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # 设置窗口初始大小
        self.resize(800, 600)  # 设置窗口宽度为 800，高度为 600

        # 连接右键菜单事件
        self.table_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_view.customContextMenuRequested.connect(self.show_context_menu)

    def resizeEvent(self, event):
        # 先调用父类的 resizeEvent 方法
        super().resizeEvent(event)
        # 调整列宽以适应窗口大小
        self.adjust_table_columns()

    def adjust_table_columns(self):
        # 调整列宽以适应窗口大小
        total_width = self.table_view.viewport().width()
        column_count = self.table_view.model().columnCount()
        if column_count > 0:
            # 每列分配宽度
            width_per_column = total_width // column_count
            for column in range(column_count):
                self.table_view.setColumnWidth(column, width_per_column)
    def on_refresh(self):
        # 处理刷新按钮点击事件
        print("Refresh button clicked")
        # 重新获取数据并更新模型
        server_info = Query.ZombiEden_Server_Query() + Query.EXG_Server_Query()
        self.model = PyqtFormModel.ServerInfoModel(server_info)
        self.table_view.setModel(self.model)
        self.adjust_table_columns()

    def show_context_menu(self, pos: QPoint):
        # 创建上下文菜单
        context_menu = QMenu(self)

        # 添加菜单项
        action1 = QAction('连接服务器', self)
        action1.triggered.connect(self.action1_triggered)
        context_menu.addAction(action1)

        action2 = QAction('复制IP', self)
        action2.triggered.connect(self.action2_triggered)
        context_menu.addAction(action2)

        # 显示菜单
        context_menu.exec_(self.table_view.viewport().mapToGlobal(pos))

    def action1_triggered(self):
        # 获取选中的行
        selection = self.table_view.selectionModel().selectedRows()
        if selection:
            selected_row = selection[0].row()
            item = self.model._data[selected_row]
            ip = item.get('ip', 'N/A')
            port = item.get('port', 'N/A')
            connect_url = f"steam://rungame/730/76561202255233023/+connect%20{ip}:{port}"
            print(f"Connecting to: {connect_url}")
            # 使用系统命令打开链接
            # 根据操作系统选择合适的命令
            if sys.platform == 'win32':
                subprocess.run(["start", connect_url], check=True, shell=True)  # Windows
            elif sys.platform == 'darwin':
                subprocess.run(["open", connect_url], check=True)  # macOS
            else:
                subprocess.run(["xdg-open", connect_url], check=True)  # Linux

    def action2_triggered(self):
        # 处理复制IP和端口的点击事件
        selection = self.table_view.selectionModel().selectedRows()
        if selection:
            selected_row = selection[0].row()
            item = self.model._data[selected_row]
            ip = item.get('ip', 'N/A')
            port = item.get('port', 'N/A')

            # 格式化 IP 和端口
            ip_port = f"{ip}:{port}"

            # 获取剪贴板对象
            clipboard = QApplication.clipboard()
            # 将 IP 和端口复制到剪贴板
            clipboard.setText(ip_port)
            print(f"Copied IP and Port: {ip_port}")

    def on_selection_changed(self):
        # 处理选择变化
        selection = self.table_view.selectionModel().selectedRows()
        if selection:
            selected_row = selection[0].row()
            print(f"Selected Row: {selected_row}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.adjust_table_columns()
    sys.exit(app.exec_())
