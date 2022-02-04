# Sources : https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def print_valid(text):
        print(Colors.OKGREEN, text, Colors.ENDC)

    @staticmethod
    def print_warning(text):
        print(Colors.WARNING, text, Colors.ENDC)

    @staticmethod
    def print_error(text):
        print(Colors.FAIL, text, Colors.ENDC)
