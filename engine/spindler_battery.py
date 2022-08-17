from engine.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        changeDate = self.last_service_date.replace(
            year=self.last_service_date.year+2)
        return self.current_date > changeDate
