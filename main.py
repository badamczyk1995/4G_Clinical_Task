
class Phone:

    def __init__(self):
        self.keypad = self.generate_phone_keypad()
        self.phone_number = None
        self.word = None
        self.used_index_tracker = None

    @staticmethod
    # Generates a dictionary mapping letters to a number key
    def generate_phone_keypad():
        mappings = {
            1: [],
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
            0: []
        }
        return mappings

    def set_phone_number(self, phone_number):
        if not isinstance(phone_number, str):
            raise Exception(f'Error: set_phone_number() - phone number {phone_number} is not a string')
        if not phone_number.isnumeric():
            raise Exception(f'Error: set_phone_number() - phone number {phone_number} is not a numeric value')

        self.phone_number = phone_number
        self.reset_tracker()

    def get_phone_number(self):
        return self.phone_number

    def set_word(self, word):
        if not isinstance(word, str):
            raise Exception(f'Error: set_word() - word {word} is not a string')
        if not word.isalpha():
            raise Exception(f'Error: set_word() - word {word} is not a valid letter')

        self.word = word
        self.reset_tracker()

    def get_word(self):
        return self.word

    def reset_tracker(self):
        self.used_index_tracker = [False for _ in range(len(self.phone_number))]

    def find_number_for_letter(self, letter):
        if not letter.isalpha():
            raise Exception(f'Error: find_number_for_letter() - letter {letter} is not valid')

        for key_number, key_letters in self.keypad.items():
            for key_letter in key_letters:
                if key_letter == letter:
                    return str(key_number)

    def track_digit(self, digit):
        for phone_number_digit, (digit_used_idx, digit_used) in zip(self.get_phone_number(), enumerate(self.used_index_tracker)):
            if digit == phone_number_digit and not digit_used:
                self.used_index_tracker[digit_used_idx] = True
                return True
        return False

    def run_checks(self, words):
        if self.get_phone_number() is None:
            raise Exception('Error: Phone number is None, please run set_phone_number()')

        if not isinstance(words, list):
            raise Exception('Error: Words is not a list')

    # Checks if the phone number can spell a single word
    def run_for_single_word(self, word):
        self.set_word(word)

        # Loop through each letter of the word
        for word_letter in self.get_word():
            key_number = self.find_number_for_letter(word_letter)
            if not self.track_digit(key_number):
                return False

        return True

    # Prints if a list of words can be spelt by a phone number
    def run_for_words(self, words):
        self.run_checks(words)

        print(f'Number: {self.get_phone_number()}\n')
        print('Word \t\tCan be spelt with given number')

        for word in words:
            print(word+'\t\t\t', self.run_for_single_word(word))


if __name__ == '__main__':
    number = '3662277'
    words_list = ['foo', 'bar', 'baz']

    phone = Phone()
    phone.set_phone_number(number)
    phone.run_for_words(words_list)

    print('\n')
    print(phone.run_for_single_word('foo'))
