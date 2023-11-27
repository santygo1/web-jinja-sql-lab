import sqlite3


class LibraryService:
    __DATABASE_LOCATION = '../resources/library.sqlite'

    def __init__(self):
        self.con = sqlite3.connect(self.__DATABASE_LOCATION)
        f_damp = open('../resources/sql/library.db', 'r', encoding='utf-8-sig')
        damp = f_damp.read()
        f_damp.close()
        self.con.executescript(damp)
        self.con.commit()

    def find_all_by_month(self, month: int, field_sort: str) -> list:
        """
        Возвращает список книг, которые были взяты в заданном месяце
        :param field_sort: Поле по которому нужно сортировать.
        :param month: порядковый номер месяца
        :return: список книг которые были взяты в заданном месяце
        """
        # Получаем доступ к бд
        con = sqlite3.connect(self.__DATABASE_LOCATION)
        cursor = con.cursor()

        # Выполняем запрос
        query = f"""
                      SELECT 
                        title as Название,
                        reader_name as Читатель,
                        borrow_date as Дата
                      FROM book_reader
                      JOIN reader using(reader_id)
                      JOIN book using(book_id)
                      WHERE strftime('%m', borrow_date) = '{month}'
                      {"ORDER BY " + field_sort if field_sort is not None or len(field_sort) == 0 else ""}
                """
        cursor.execute(query)
        result = cursor.fetchall()

        # Закрытие коннекта с бд и возвращение результата
        con.close()
        return result
