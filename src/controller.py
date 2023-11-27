from service import LibraryService
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('../resources/template/'))
service = LibraryService()

if __name__ == '__main__':
    template_name = 'book_query.html'
    template = env.get_template(template_name)

    months = {1: "Январь", 2: "Февраль", 3: "Март",
              4: "Апрель", 5: "Май", 6: "Июнь",
              7: "Июль", 8: "Август", 9: "Сентябрь",
              10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}

    fields = [{"title": "Название", "value": "title"},
              {"title": "Читатель", "value": "reader_name"},
              {"title": "Дата", "value": "borrow_date"}]

    books = service.find_all_by_month(10, "title")

    result_html = template.render(books=books, months=months, fields=fields)

    f = open('../resources/static/html/' + template_name, 'w', encoding='utf-8-sig')
    f.write(result_html)
    f.close()
