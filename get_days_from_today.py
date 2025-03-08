from datetime import datetime

def get_days_from_today(date: str) -> int:
    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        return "Неправильний формат дати. Використовуйте РРРР-ММ-ДД з дефісом."
    
    old_date = datetime.strptime(date, "%Y-%m-%d")
    return (old_date - datetime.today()).days
print(get_days_from_today("2024-10-09"))