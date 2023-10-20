from datetime import datetime, timedelta


def get_last_friday(input_date):
    try:
        month, year = map(int, input_date.split('/'))

        next_month = (month % 12) + 1
        next_year = year + (1 if month == 12 else 0)
        first_day_of_next_month = datetime(next_year, next_month, 1)
        last_day_of_month = first_day_of_next_month - timedelta(days=1)
        last_day_weekday = last_day_of_month.weekday()
        if last_day_weekday < 4:
            days_until_friday = 4 - last_day_weekday
            last_friday = last_day_of_month - timedelta(days=days_until_friday)
        else:
            days_until_next_friday = 11 - last_day_weekday
            last_friday = last_day_of_month + timedelta(days=days_until_next_friday)

        result = last_friday.strftime("%d.%m.%Y")
        return result
    except ValueError:
        return "Некорректный формат даты"
