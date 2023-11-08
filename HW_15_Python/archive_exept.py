import argparse
import os
import logging
from exeptions import InvalidNumberError, InvalidTextError

FORMAT = '{levelname}, {asctime}, {msg}'
current_dir = os.path.dirname(os.path.realpath(__file__))
log_filename = os.path.join(current_dir, 'archive_log.log')
logging.basicConfig(format=FORMAT, style='{', filename=log_filename, filemode='a', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


class Archive:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text, number):
        try:
            if not isinstance(text, str) or len(text.strip()) == 0:
                raise InvalidTextError(f'Invalid text: {text}. Text should be a non-empty string.')
        except InvalidTextError as e:
            logger.error(f'{e}')
        try:
            if not (isinstance(number, int) or isinstance(number, float)) or number <= 0:
                raise InvalidNumberError(f'Invalid number: {number}. Number should be a positive integer or float.')
        except InvalidNumberError as e:
            logger.error(f'{e}')
        self.text = text
        self.number = number
        logger.info(f'Created Archive with text: {text}, number: {number}')

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


def main():
    parser = argparse.ArgumentParser(description='Archive Information')
    parser.add_argument('-t', '--text', type=str, help='Text')
    parser.add_argument('-n', '--number', type=float, help='Number')
    args = parser.parse_args()
    archive = Archive(args.text, args.number)
    return f'{archive}'


if __name__ == "__main__":
    print(main())