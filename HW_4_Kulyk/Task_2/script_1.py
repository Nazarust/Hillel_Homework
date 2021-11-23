
# Реалізуйте контекстний менеджер для роботи з файлом. Якщо під час
# роботи виникає ексепшин, файл повинен «відкотити» зміни.


class File(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        self.backup = self.file.read()
        self.file.close()
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.file.close()
            self.file = open(self.filename, mode="w")
            self.file.write(self.backup)
            self.file.close()
            return True
        self.file.close()


with File('main.txt', 'w') as opened_file:
    opened_file.write('Hello!')


with File('main.txt', 'w') as opened_file:
    opened_file.undefined_function()


