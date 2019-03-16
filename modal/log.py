import tablib


def format_info(key, data):
    return {key[x]: data[x] for x in range(0, len(key))}


class LogData(object):
    _FILE_PATH = './data/step2_log.csv'
    _SPLIT_STR = ''
    tableHead = ['phone', 'status', 'update_time']
    tableObj = object

    def __init__(self):
        try:
            self.tableObj = tablib.Dataset().load(open(self._FILE_PATH).read())
        except tablib.core.UnsupportedFormat:
            self.tableObj = tablib.Dataset()
        self.tableObj.headers = self.tableHead
        pass

    def get_data_by_phone(self, phone):
        index = self.get_index_by_phone(phone)
        if index != -1:
            data = format_info(self.tableObj[index])
            return data
        return None

    def save_data(self, data, tags=None):
        index = self.get_index_by_phone(data['phone'])
        if index != -1:
            del self.tableObj[index]
        self.add_data(data, tags=tags)
        self._write_data()

    def add_data(self, data, tags=None):
        """
        保存数据
        :param data: list
        :param tags: list
        """
        if tags is None:
            tags = list()
        self.tableObj.append([x for x in data.values()], tags=tags)
        pass

    def update_data(self, row, data, tags):
        pass

    def get_index_by_phone(self, phone):
        phone_list = self.tableObj.get_col(0)
        if str(phone) in phone_list:
            return phone_list.index(str(phone))
        return -1

    def _write_data(self):
        f = open(self._FILE_PATH, 'w')
        f.write(self.tableObj.export('csv'))
