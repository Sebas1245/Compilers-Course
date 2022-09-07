from ldparser import ld_parser

def test():
    print('Enter file name to be tested (with .ld extension)')
    filename = input()
    file = open(filename)
    input_str = file.read()
    file.close()
    ld_parser.parse(input_str)
    print('Accepted code')

if __name__ == "__main__":
    test()
