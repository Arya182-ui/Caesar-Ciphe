import csv
from datetime import datetime

def log_operation(mode, shift, input_text, output_text):
    with open('logs.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), mode, shift, input_text, output_text])
