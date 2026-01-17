import sys

# def main (arguments):
#     for index, argument in enumerate(arguments):
#         print(f'{index} = {argument}')
        
# if __name__ == '__main__':
#     main(sys.argv)

def main(a,b):
    print(f'{a + b}')

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))