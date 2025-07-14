class MockBorderAPI:
    """
    Мок-реализация API для тестирования логики без внешних зависимостей.
    """

    def fetch_visits(self, date: str, mode: str, guids: list[str]) -> dict:
        """
        Возвращает тестовый ответ, имитирующий реальный API.
        """
        return {
            "data": [
                [
                    "vFHlJ5Es",
                    "Хаммам",
                    "some_internal_id",
                    [
                        ["00:00", 2, 0],
                        ["00:30", 4, 0],
                        ["01:00", 1, 0]
                    ]
                ],
                [
                    "Gp7yQFaE",
                    "Парная",
                    "some_internal_id",
                    [
                        ["00:00", 0, 0],
                        ["00:30", 1, 0],
                        ["01:00", 3, 0]
                    ]
                ],
                [
                    "Ab7WxWkw",
                    "Бассейн",
                    "some_internal_id",
                    [
                        ["00:00", 5, 0],
                        ["00:30", 6, 0],
                        ["01:00", 8, 0]
                    ]
                ],
            ]
        }
