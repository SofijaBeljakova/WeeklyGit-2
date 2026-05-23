import os
from datetime import datetime, timezone, timedelta

README_PATH = "README.md"
START_DATE = datetime(2026, 5, 23, tzinfo=timezone.utc)

def main():
    ee_tz = timezone(timedelta(hours=3))
    today = datetime.now(ee_tz)
    delta = today.date() - START_DATE.date()
    if delta.days < 0: return
    day_number = delta.days + 1
    formatted_date = today.strftime("%d.%m.%Y")
    if not os.path.exists(README_PATH):
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write("# Project\n")
    with open(README_PATH, "a", encoding="utf-8") as f:
        f.write(f"- {formatted_date}: Päev {day_number}\n")

if __name__ == "__main__":
    main()
