class LoxException(Exception):
    def __init__(self, line: int, message: str, where: str = ""):
        self.line = line
        self.where = where
        self.message = message

    def __repr__(self):
        return f'LoxException\non line {self.line}, token {self.where} caused error {self.message}'
