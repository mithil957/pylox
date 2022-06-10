import sys

from scanner import Scanner


class Lox:
    had_error = False

    @staticmethod
    def run(source: str):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        print(tokens)

    @staticmethod
    def run_file(path: str) -> None:
        try:
            source_file = open(path, 'r')
        except BaseException as err:
            print(f'Unexpected {err=}, {type(err)=}')
        else:
            source_code = source_file.read()
            Lox.run(source_code)
            if Lox.had_error:
                sys.exit(65)

    @staticmethod
    def run_prompt() -> None:
        print('REPL started')

        while True:
            print('>', end=' ')
            line = input()

            if len(line) == 0:
                print('Empty input, ending session')
                break

            Lox.run(line)
            Lox.had_error = False

    @staticmethod
    def report(line: int, where: str, message: str):
        print(f'on line {line}, token {where} caused error {message}')
        Lox.had_error = True

    @staticmethod
    def error(line: int, message: str):
        Lox.report(line, "", message)


if __name__ == "__main__":
    match str(sys.argv):
        case ['lox.py', filepath]:
            Lox.run_file(filepath)
        case ['lox.py']:
            Lox.run_prompt()
        case _:
            print('Usage: python lox.py or python lox.py {script_path}')
