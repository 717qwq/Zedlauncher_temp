from PyQt5.QtCore import Qt, QPoint, QAbstractTableModel, QVariant
class ServerInfoModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        super(ServerInfoModel, self).__init__(parent)
        self._data = data
        self._headers = ['IP', 'Name', 'Map', 'Players', 'Max Players']

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return QVariant()

        row = index.row()
        column = index.column()

        if row >= len(self._data) or column >= len(self._headers):
            return QVariant()

        item = self._data[row]

        # Map columns to data
        if column == 0:
            return QVariant(f"{item.get('ip', 'N/A')}:{item.get('port', 'N/A')}")
        elif column == 1:
            return QVariant(item.get('name', 'N/A'))
        elif column == 2:
            return QVariant(item.get('map', 'N/A'))
        elif column == 3:
            return QVariant(item.get('players', 'N/A'))
        elif column == 4:
            return QVariant(item.get('max_players', '64'))
        else:
            return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()

        if orientation == Qt.Horizontal:
            return QVariant(self._headers[section])
        return QVariant()
