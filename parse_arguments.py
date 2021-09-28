import argparse


def greeting(args):
    if args.name:
        print(f'Hallo {args.name}!')
    else:
        print('Es wurde kein Name eingegeben.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')

    greeting(parser.parse_args())


if __name__ == "__main__":
    main()
    
