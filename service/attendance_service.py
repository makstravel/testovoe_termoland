import pandas as pd


class AttendanceService:
    """
    Сервис для обработки и агрегации данных посещаемости зон.
    """

    def __init__(self, zones_repo, border_api):
        """
        :param zones_repo: Репозиторий зон
        :param border_api: Источник данных BorderAPI
        """
        self.zones_repo = zones_repo
        self.border_api = border_api

    def load_attendance(self, date: str, mode: str = "halfhour") -> pd.DataFrame:
        """
        Загружает и формирует таблицу посещаемости по всем зонам за выбранную дату.
        :param date: Дата в формате 'дд.мм.гггг'
        :param mode: Режим агрегации (по умолчанию — "halfhour")
        :return: DataFrame с данными посещаемости
        """
        zones = self.zones_repo.get_zones()
        data = self.border_api.fetch_visits(date, mode, list(zones.keys()))

        # Формируем таблицу: время | зона | посещения
        records = []
        for zone_data in data["data"]:
            guid, name, _, time_data = zone_data
            for time_point in time_data:
                time_str, visitors, _ = time_point
                records.append({
                    "Дата": date,
                    "Время": time_str,
                    "Зона": zones.get(guid, name),
                    "GUID": guid,
                    "Посещения": visitors
                })
        return pd.DataFrame(records)
