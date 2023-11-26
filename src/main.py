from collections import Counter

from src import log
from src.bank_operations_utils import count_operations_by_category, search_operations
from src.settings import PATH_CSV
from src.utils import read_csv_xlsx_file

logger = log.setup_logging()


def main() -> None:
    """Данный код для проверки"""

    print(search_operations(read_csv_xlsx_file(PATH_CSV), "Перевод со счета на счет"))

    dict_categories = dict(Counter(item['description'] for item in read_csv_xlsx_file(PATH_CSV)).most_common())

    for key in dict_categories:
        dict_categories[key] = 0

    print(count_operations_by_category(read_csv_xlsx_file(PATH_CSV), dict_categories))


if __name__ == "__main__":
    main()
