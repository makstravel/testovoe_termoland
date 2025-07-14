from repo.zones_repository import ZonesRepository
from datasource.border_api import BorderAPI
from service.attendance_service import AttendanceService
from mock.mock_border_api import MockBorderAPI

def main():
    zones_repo = ZonesRepository('Справочник.xlsx')
    border_api = MockBorderAPI() #при обращении к реальному IP заменить на BorderAPI()
    service = AttendanceService(zones_repo, border_api)

    date = '3.06.2020'
    df = service.load_attendance(date)
    df.to_excel(f'attendance_{date}.xlsx', index=False)
    print('Выгрузка успешно завершена.')

if __name__ == '__main__':
    main()
