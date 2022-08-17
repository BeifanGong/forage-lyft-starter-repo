from engine.battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        changeDate = self.last_service_date.replace(
            year=self.last_service_date.year+4)
        return self.current_date > changeDate
