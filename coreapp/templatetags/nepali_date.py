from django import template
import nepali_datetime

register = template.Library()

@register.filter
def nepali(value):
    if value:
        try:
            bs_date = nepali_datetime.date.from_datetime_date(value)
            return bs_date.strftime("%Y-%m-%d")   # Nepali date format
        except:
            return value
    return ""