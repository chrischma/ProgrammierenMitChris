import argparse


def greeting(args):
    if args.name:
        print(f'Hallo {args.name}!')
    else:
        print('Hallo unbekannter Freund!')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')

    greeting(parser.parse_args())


if __name__ == "__main__":
    main()
    
