from model.book_model import Book
from model.genre_model import Genre


def findall_by_month_and_genre_id(con, month_num: int, genre_id: int) -> list[Book]:
    """
    Возвращает список книг, которые были взяты в заданном месяце
    :param con: соединение с базой данных
    :param genre_id: id жанра книги
    :param month_num: порядковый номер месяца
    :return: список книг заданного жанра, которые были взяты в заданном месяце
    """

    query = f"""
                      SELECT  title, reader_name, borrow_date, genre_id, genre_name
                      FROM book_reader
                      JOIN reader using(reader_id)
                      JOIN book using(book_id)
                      JOIN genre using (genre_id)
                      WHERE strftime('%m', borrow_date) = '{month_num}' and genre_id = {genre_id}
                """

    cursor = con.cursor()
    cursor.execute(query)
    dataset = cursor.fetchall()
    cursor.close()

    return [Book(d[0], d[1], d[2], Genre(d[3], d[4])) for d in dataset]
