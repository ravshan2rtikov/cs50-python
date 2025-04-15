months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def parse_date(date_str):
    try:
        date_str = date_str.strip()
        if "/" in date_str:
            month, day, year = date_str.split("/")
            month, day, year = int(month), int(day), int(year)
        elif "," in date_str:
            parts = date_str.split()
            if len(parts) != 3 or "," not in parts[1]:
                return None

            month_str, day, year = parts
            day = day.replace(",", "")
            month = months.index(month_str) + 1
            day, year = int(day), int(year)
        else:
            return None

        if not (1 <= month <= 12 and 1 <= day <= 31):
            return None

        return f"{year:04}-{month:02}-{day:02}"
    except (ValueError, IndexError):
        return None


while True:
    date_input = input("Date: ")
    formatted_date = parse_date(date_input)
    if formatted_date:
        print(formatted_date)
        break
