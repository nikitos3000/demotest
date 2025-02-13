import psycopg2
from types_data import Family, Price
from mainwindow import setupUi

def get_connection():
    connection = psycopg2.connect("dbname=test "
                                  "host=localhost "
                                  "port=5432 "
                                  "user=postgres "
                                  "password=123 ")
    
    cursor = connection.cursor()

    return connection, cursor

from datetime import datetime

def calculate_age(member):
    today = datetime.today()
    age = today.year - member.birth_date.year

    print(age)
    member.years_old = age

def calculate_ratio(member):
    con, cur = get_connection()

    cur.execute("SELECT p.unit_price, pp.quantity "
                "FROM products p "
                "LEFT JOIN expence_products pp ON p.id = pp.product "
                "WHERE pp.quantity IS NOT NULL;")
    products_prices_from_db = cur.fetchall()
    product_prices = [
        Price(x[0], x[1]) for x in products_prices_from_db
                   ]
    for product in product_prices:
        fff = product.unit_price * product.quantity
        print(fff)

    a = 100


if __name__ == '__main__':
    con, cur = get_connection()

    cur.execute("SELECT fm.full_name, fj.position, fj.organization, fj.salary, fm.birth_date "
                "FROM family_members fm "
                "LEFT JOIN family_jobs fj ON fm.id = fj.person;")
    family_jobs_from_db = cur.fetchall()
    family_jobs = [
        Family(x[0], x[1], x[2], x[3], x[4]) for x in family_jobs_from_db
                   ]
    cur.close()
    con.close()

    for member in family_jobs:
        calculate_age(member)

    for member in family_jobs:
        calculate_ratio(member)



    a=100
    setupUi(family_jobs)

