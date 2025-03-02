from datetime import datetime, date

def get_days_from_today(input_date):
    try:
        delta = date.today() - datetime.strptime(input_date, "%Y.%m.%d").date()
        return delta.days
    except ValueError:
        print("Date format is invalid")
        return None
print(get_days_from_today("2026.02.24"))

