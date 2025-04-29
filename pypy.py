import sqlite3
def find_customer(email):
    """Функція для пошуку клієнта в базі даних за email."""
    conn = sqlite3.connect("crm_database.db")  # Підключення до бази
    cursor = conn.cursor()
    query = "SELECT * FROM customers WHERE email = ?"
    cursor.execute(query, (email,))
    result = cursor.fetchone()  # Отримуємо перший знайдений запис
    conn.close()
    return result  # Якщо клієнт є в базі, поверне його дані, якщо ні — None


# **Тест**: Перевіримо, чи існує клієнт із email 'test@example.com'
def test_find_customer():
    email_to_search = "test@example.com"
    customer = find_customer(email_to_search)

    assert customer is not None, f"Клієнта з email {email_to_search} не знайдено!"
    print(f"✅ Тест пройдено! Клієнт {customer} знайдений у базі.")

# Запускаємо тест
test_find_customer()

import requests

def find_customer_api(email):
    """Функція для пошуку клієнта через API CRM за email."""
    url = "https://api.examplecrm.com/customers"  # URL API CRM
    params = {"email": email}  # Параметр для пошуку клієнта за email

    response = requests.get(url, params=params)  # Виконуємо GET запит

    if response.status_code == 200:
        customers = response.json()  # Отримуємо дані у форматі JSON
        return customers
    else:
        return None

# **Тест**: Перевіримо, чи існує клієнт із email 'test@example.com' через API
def test_find_customer_api():
    email_to_search = "test@example.com"
    customers = find_customer_api(email_to_search)

    assert customers is not None and len(customers) > 0, f"Клієнта з email {email_to_search} не знайдено через API!"
    print(f"✅ Тест пройдено! Клієнт з email {email_to_search} знайдений через API.")

# Запускаємо тест
test_find_customer_api()