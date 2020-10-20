import argparse
from random_password.generate import PasswordGenerator


def main():
    parser = argparse.ArgumentParser(description='Generate passwords.')
    parser.add_argument('num_results', type=int, default=1, nargs='?',
                        help='Number of results to return')
    parser.add_argument('num_lowercase', type=int, default=5, nargs='?',
                        help='Number of lowercase characters.')
    parser.add_argument('num_uppercase', type=int, default=2, nargs='?',
                        help='Number of uppercase characters.')
    parser.add_argument('num_digits', type=int, default=2, nargs='?',
                        help='Number of digit characters.')
    parser.add_argument('num_punctuation', type=int, default=1, nargs='?',
                        help='Number of punctuation characters.')
    args = parser.parse_args()

    for password in PasswordGenerator().generate_passwords(args.num_results, args.num_lowercase, args.num_uppercase, args.num_digits, args.num_punctuation):
        print(password)

if __name__ == "__main__":
    main()
