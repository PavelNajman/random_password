import string
import random
import secrets

class PasswordGenerator(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PasswordGenerator, cls).__new__(cls)
        return cls._instance

    def generate_password(self, numLowerCaseChars, numUpperCaseChars, numDigitChars, numPunctuationChars):
        chars = []
        chars += [secrets.choice(string.ascii_lowercase) for i in range(numLowerCaseChars)]
        chars += [secrets.choice(string.ascii_uppercase) for i in range(numUpperCaseChars)]
        chars += [secrets.choice(string.digits) for i in range(numDigitChars)]
        chars += [secrets.choice(string.punctuation) for i in range(numPunctuationChars)]
        random.shuffle(chars)
        return ''.join(chars)

    def generate_passwords(self, num_results, numLowerCaseChars, numUpperCaseChars, numDigitChars, numPunctuationChars):
        return [self.generate_password(numLowerCaseChars, numUpperCaseChars, numDigitChars, numPunctuationChars) for _ in range(num_results)]
