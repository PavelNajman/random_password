# Random Password Generator

A package to randomly generate passwords.

Inspiration from [williexu](https://github.com/williexu/random_username).

## Installation

You can install the Random Password Generator using:

    python setup.py install

This package is supported on Python 3.6 and above.

## How to use

This is a command-line application to generate passwords. To use, simply call:

    $ random_password -h
    usage: [-h] [num_results] [num_lowercase] [num_uppercase] [num_digits] [num_punctuation]

    Generate passwords.

    positional arguments:
    num_results      Number of results to return
    num_lowercase    Number of lowercase characters.
    num_uppercase    Number of uppercase characters.
    num_digits       Number of digit characters.
    num_punctuation  Number of punctuation characters.

    optional arguments:
    -h, --help       show this help message and exit

To generate passwords, call the program like so (not specifying a number will default to 1):

    $ random_passwords 10 5 2 2 1
    Pt7fT&rv1g
    le^5jI0fHn
    Gjh6x/o8rE
    q/1l4ldQHp
    wpaC45g+Kg
    t2YkX6|zad
    h11m:dFziP
    a2{ooO3Dux
    7~KEr9eref
    eZj+1pqo8X

You can also call the Random Password Generator from your own python code by importing from `random_password.generate`

    >>> from random_password.generate import PasswordGenerator
    >>> PasswordGenerator().generate_passwords(5, 5, 2, 2, 1)
    ['Pt7fT&rv1g', 'le^5jI0fHn', 'Gjh6x/o8rE', 'q/1l4ldQHp', 'wpaC45g+Kg']
