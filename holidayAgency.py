from umalqurra.hijri_date import HijriDate
from umalqurra.hijri import Umalqurra
import arrow
import turkey

class HolidayAgency(object):
    
    @staticmethod
    def get_holidays_for(country='tr'):
        if country == turkey.COUNTRY_CODE:
            holidays = HolidayAgency.get_ramadan_feast() + HolidayAgency.get_sacrificing_feast()
            holidays += [x.to_dict() for x in turkey.NATIONAL_HOLIDAYS]
            return holidays

    @staticmethod
    def __get_hijri_today__(timezone="Europe/Istanbul") -> HijriDate:
        current_timestruct = arrow.now(timezone).timetuple()
        return HijriDate(current_timestruct[0], # Year
                                current_timestruct[1], # Month
                                current_timestruct[2], # Day
                                gr=True)

    @staticmethod
    def get_ramadan_feast(timezone="Europe/Istanbul") -> list:
        hijri_today = HolidayAgency.__get_hijri_today__()
        hijri_year = hijri_today.year
        end_of_the_ramadan = HijriDate(hijri_year, 9, 30)
        day_list = [{
            'name': 'arefe_ramadan',
            'datetime': arrow.Arrow(end_of_the_ramadan.year_gr,
            end_of_the_ramadan.month_gr,
            end_of_the_ramadan.day_gr).for_json()
        }]
        start_of_feast_gr = arrow.Arrow(
            end_of_the_ramadan.year_gr,
            end_of_the_ramadan.month_gr,
            end_of_the_ramadan.day_gr).shift(days=1)
        feast_days = [x[0] for x in arrow.Arrow.span_range('day', start_of_feast_gr, start_of_feast_gr.shift(days=2))]
        for i, day in enumerate(feast_days, start=1):
            day_list += [{
                'description': f"ramadan_feast_{i}",
                'datetime': day.for_json()
            }]
        return day_list

    @staticmethod
    def get_sacrificing_feast(timezone="Europe/Istanbul") -> list:
        hijri_today = HolidayAgency.__get_hijri_today__()
        hijri_year = hijri_today.year
        start_hijri = HijriDate(hijri_year, 12, 10)
        start_of_feast_gr = arrow.Arrow(start_hijri.year_gr, start_hijri.month_gr, start_hijri.day_gr)
        end_of_feast_gr = arrow.Arrow(start_hijri.year_gr, start_hijri.month_gr, start_hijri.day_gr + 3)
        day_list = [{
            'description': 'arefe_sacrifice',
            'datetime': start_of_feast_gr.shift(days=-1).for_json()
        }]
        feast_days = [x[0] for x in arrow.Arrow.span_range('day', start_of_feast_gr, end_of_feast_gr)]
        for i, day in enumerate(feast_days, start=1):
            day_list += [{
                'name': f"sacrifice_feast_{i}",
                'datetime': day.for_json()
            }]
        return day_list
