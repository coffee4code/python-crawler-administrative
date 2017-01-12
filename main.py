from lib.JSONReader import JSONReader
from lib.Parser import Parser
import config


def main():
    cities = config.cities
    reader = JSONReader()
    parser = Parser()
    for i in range(len(cities)):
        data = reader.read(cities[i]["name"], cities[i]["subdistrict"])
        parser.parse(data, cities[i]["id"])


if __name__ == '__main__':
    print('=====================================开始===============================')
    main()
    print('=====================================完成===============================')
