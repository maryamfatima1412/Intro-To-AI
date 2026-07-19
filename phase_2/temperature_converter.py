class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @classmethod
    def default_temperature(cls):
        return cls(0)


temp = TemperatureConverter.default_temperature()

print("Default Celsius:", temp.celsius)
print("25°C =", TemperatureConverter.celsius_to_fahrenheit(25), "°F")