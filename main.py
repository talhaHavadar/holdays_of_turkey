from holidayAgency import HolidayAgency
holidays = HolidayAgency.get_holidays_for("tr")
print(sorted(holidays, key=lambda k: k['datetime']))