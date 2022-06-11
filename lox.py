import sys

from lox_exceptions import LoxException
from scanner import Scanner


class Lox:

    @staticmethod
    def run(source: str):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        print(tokens)

    @staticmethod
    def run_file(path: str) -> None:
        try:
            source_file = open(path, 'r')
            source_code = source_file.read()
            Lox.run(source_code)
        except LoxException as err:
            print(err)
        except BaseException as err:
            print(f'Unexpected {err=}, {type(err)=}')

    @staticmethod
    def run_prompt() -> None:
        print('REPL started')

        while True:
            print('>', end=' ')
            line = input()

            if len(line) == 0:
                print('Empty input, ending session')
                break

            try:
                Lox.run(line)
            except LoxException as err:
                print(err)


if __name__ == "__main__":
    match sys.argv:
        case['lox.py']:
            Lox.run_prompt()
        case ['lox.py', filepath]:
            Lox.run_file(filepath)
        case _:
            print('Usage: python lox.py or python lox.py {script_path}')
