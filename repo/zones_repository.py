import pandas as pd


class ZonesRepository:
    """
    Репозиторий для получения справочника зон из Excel-файла.
    """

    def __init__(self, path: str):
        """
        :param path: Путь к файлу Excel со справочником зон.
        """
        self.path = path

    def get_zones(self) -> dict:
        """
        Загружает справочник зон.
        :return: Словарь вида {GUID: Наименование}
        """
        df = pd.read_excel(self.path)
        return dict(zip(df['GUID'], df['Наименование']))
