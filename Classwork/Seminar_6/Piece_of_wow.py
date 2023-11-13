from sys import argv

if __name__ == '__main__':
    gen = (int(argv[a]) for a in range(1, len(argv)))
