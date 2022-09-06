from ldparser import ld_parser

def test():
    print('Testing')
    file = open('hello_world.ld')
    input_str = file.read()
    file.close()
    ld_parser.parse(input_str)
    print('Accepted code')

if __name__ == "__main__":
    test()
