"""
    lager-pdb-demo
    Simple pdb / breakpoint example

    MIT License

    Copyright (c) 2021 Lager Data
"""

def main():
    my_list = [101, 200, 300, 400]
    my_map = {100: 'hello', 200: 'world', 300: 'goodbye', 400: 'world'}
    breakpoint()
    for key in my_list:
        print(my_map[key])

if __name__ == '__main__':
    main()
