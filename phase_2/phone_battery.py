class Battery:
    def charge_level(self):
        print("Battery is 90% charged")


class Phone:
    def __init__(self):
        self.battery = Battery()

    def check_battery(self):
        self.battery.charge_level()


phone = Phone()
phone.check_battery()