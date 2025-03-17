import concurrent.futures as fu
import logging

import tinydb

from torm_storage.Torm import TormStorage

MAX = 100
DB = tinydb.TinyDB('./tests/dump/test', storage=TormStorage)

def test(count):
    DB.insert({"test": f"saja {count + 1}"})
    # d = DB.get(doc_id=c)
    # print(d)


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )

    with fu.ThreadPoolExecutor(max_workers=MAX//2) as threader:
        threader.map(test, range(MAX))


if __name__ == '__main__':
    main()
