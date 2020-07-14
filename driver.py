import csv
from scrapper import ScrapperShopee


if __name__ == "__main__":

    filepath = 'link.txt'
    with open(filepath) as fp:

        line = fp.readline()
        counter = 1

        while line:

            try:
                coba = ScrapperShopee(line, counter)
                coba.scrappe()
                line = fp.readline()
                counter += 1
            except Exception as err:
                print(err)
                line = fp.readline()
                counter += 1