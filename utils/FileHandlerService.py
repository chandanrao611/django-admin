from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import csv
from django.shortcuts import render

class FileHandlerService:

    @staticmethod
    def read_csv(file, batch_size= 1000):
        # Stream file without loading full into memory
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        batch = []
        for row in reader:
            batch.append(row)

            if len(batch) == batch_size:
                yield batch
                batch = []

        if batch:
            yield batch