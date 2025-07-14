import requests

BASE_URL = 'http://185.76.109.236:9006/borders/chart-data'


class BorderAPI:
    """
    Источник данных для получения посещаемости зон через внешний HTTP API.
    """

    def fetch_visits(self, date: str, mode: str, guids: list[str]) -> dict:
        """
        Запрашивает данные посещений по зонам.
        :param date: Дата в формате 'дд.мм.гггг'
        :param mode: Режим выборки ('halfhour', 'hour', 'daysN', 'week', 'month', 'year')
        :param guids: Список GUID зон
        :return: Ответ API в формате dict
        :raises: requests.HTTPError при ошибке запроса
        """
        params = {
            "mode": mode,
            "date": date,
            "objects": ','.join(guids)
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
