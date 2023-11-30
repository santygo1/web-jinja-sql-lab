import sqlite3
from jinja2 import Environment, FileSystemLoader

from dao import genre_dao, book_dao
from util.month import months

env = Environment(loader=FileSystemLoader('../template'))


def render_template(template_name: str, **kwargs):
    template = env.get_template(template_name)
    result_html = template.render(**kwargs)
    f = open('../static/html/' + template_name, 'w', encoding='utf-8-sig')
    f.write(result_html)
    f.close()


qparam_month, qparam_genre_id = 10, 3

con = sqlite3.connect('../library.sqlite')
genres = genre_dao.findall(con)
books = book_dao.findall_by_month_and_genre_id(con, qparam_month, qparam_genre_id)
con.close()

render_template('book-query.html',
                books=books,
                genres=genres,
                months=months,
                filter={"genre": qparam_genre_id, "month": qparam_month})
