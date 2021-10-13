import pyowm
from timezone_conversion import gmt_to_eastern

API_KEY = '2b62511b3bb14c8fbb75f8103ccb9f73'

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()


def get_temperature(City):
    forecaster = mgr.forecast_at_place(City, '3h')
    forecast = forecaster.forecast
    days = []
    dates = []
    temp_min = []
    temp_max = []
    for weather in forecast:
        day = gmt_to_eastern(weather.reference_time())
        date = day.date()
        if date not in dates:
            dates.append(date)
            temp_min.append(None)
            temp_max.append(None)
            days.append(date)
        temperature = weather.temperature('fahrenheit')['temp']
        if not temp_min[-1] or temperature < temp_min[-1]:
            temp_min[-1] = temperature
        if not temp_max[-1] or temperature > temp_max[-1]:
            temp_max[-1] = temperature
    return (days, temp_min, temp_max)


if __name__ == '__main__':
    City = input("Enter the City: ")
    get_temperature(City)
