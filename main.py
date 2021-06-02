from A2parser import parser
import sys


def main():
    with open("Test", 'r') as input_file:
        parser.parse(input_file.read())
        print("If nothing is printed, there are no errors.")

main()