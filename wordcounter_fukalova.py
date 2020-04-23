import argparse
import sys


def main():
    newparser = argparse.ArgumentParser(description='wordcounter')
    newparser.add_argument('wordcounter')
    newparser.add_argument("znaky", help="Spočítá znaky", action="store_true")
    newparser.add_argument("slova", help="Spočítá slova", action="store_true")
    newparser.add_argument("radky", help="Spočítá řádky", action="store_true")
    arguments = newparser.parse_args()

    try:
        uwu = open(arguments.soubor, "r")
        soubor = uwu.read()
        flag = False
        if arguments.slova:
            pocet_slov = word_counter(wordcounter)
            print(f"Počet slov: {pocet_slov}")
            flag = True

        if arguments.znaky:
            pocet_znaku = znaky_counter(wordcounter)
            print(f"Počet znaků: {pocet_znaku}")
            flag = True

        if arguments.radky:
            pocet_radku = line_counter(wordcounter)
            print(f"Počet řádků: {pocet_radku}")
            flag = True

        if not flag:
            pocet_slov = word_counter(wordcounter)
            pocet_znaku = znaky_counter(wordcounter)
            pocet_radku = line_counter(wordcounter)
            print(uwu"Počet slov: {pocet_slov}\nPočet znaků: {pocet_znaku}\nPočet řádků: {pocet_radku}")

     except PermissionError:
        print("Bez oprávnění")

        sys.exit()
    except:
        print("Něco se pokazilo")
        sys.exit()
if __name__ == "__main__":
    main()
