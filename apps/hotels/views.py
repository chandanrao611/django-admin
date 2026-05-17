from datetime import datetime

from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render
from django.views import View
from apps.hotel_admin.CommonChoice import HotelBookingStatus, AccountStatus
from apps.hotel_admin.forms import FileForm
from apps.hotels.models import Hotel
from utils.FileHandlerService import FileHandlerService
from utils.MessageHandler import MessageHandler


# Create your views here.
class HotelListView(View):
    def get(self, request):
        request.show_loader = True
        hotels = Hotel.objects.all()
        # Create paginator: 10 employees per page
        limit = int(request.GET.get('limit', 10))
        paginator = Paginator(hotels, limit)
        # Get current page number from query string (?page=2)
        page_number = request.GET.get('page', 1)
        # Get the page object
        page_obj = paginator.get_page(page_number)
        fileForm = FileForm()
        request.show_loader = False
        return render(request, 'hotel-list.html', {'page_obj': page_obj, 'fileForm':fileForm})
    def post(self, request):
        form = FileForm(request.POST, request.FILES)
        if not form.is_valid():
            MessageHandler.error(request, MessageHandler.INVALID_CREDENTIALS)
            print('----------')
            return self.get(request)
        file = request.FILES.get("csv_file")
        if not file:
            MessageHandler.error(request, MessageHandler.INVALID_CREDENTIALS)
            return self.get(request)
        mob = 1234567890
        email = 1
        for batch in FileHandlerService.read_csv(file, 1000):
            hotels = []

            for row in batch:
                mob = mob + 1
                email = email + 1
                hotels.append(
                    Hotel(
                        name=row.get('name'),
                        nick_name = row.get('nick_name'),
                        about = row.get('about'),
                        address = row.get('address'),
                        city = row.get('city'),
                        state = row.get('state'),
                        country = row.get('country'),
                        mobile = mob,
                        # row.get('mobile'),
                        alternative_mobile = mob,
                        email = 'hotel'+str(email)+'@yopmail.com',
                        # row.get('email'),
                        alternative_email = 'hotel_'+str(email)+'@yopmail.com',
                # row.get('alternative_email'),
                        established = datetime.strptime(row.get('established'), "%Y-%m-%d %H:%M:%S %z").date() if row.get('established') else None,
                        booking_status = HotelBookingStatus.OPEN,
                        status = AccountStatus.PENDING
                    )
                )

            try:
                with transaction.atomic():
                    Hotel.objects.bulk_create(hotels)
                print("Inserted:", len(hotels))
            except Exception as e:
                print("Insert Error:", e)

        return self.get(request)