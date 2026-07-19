class Printer:
    def perform_task(self):
        print("Printing document")

class FaxMachine:
    def perform_task(self):
        print("Sending fax")

def start_task(device):
    device.perform_task()

printer = Printer()
fax = FaxMachine()

start_task(printer)
start_task(fax)