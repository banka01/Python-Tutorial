## command line arguments
import sys

if __name__ == '__main__':
    params = sys.argv[1:]
    for x in params:
        print(f"params are: {x}")
