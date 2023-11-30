from model.genre_model import Genre


def findall(con) -> list[Genre]:
    """
    Возвращает список всех жанров
    """

    query = f"""SELECT * FROM genre"""
    cursor = con.cursor()
    cursor.execute(query)
    dataset = cursor.fetchall()
    cursor.close()

    return [Genre(d[0], d[1]) for d in dataset]
