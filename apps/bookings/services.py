from apps.bookings.models import Booking

class BookingService:

    @staticmethod
    def get_total_bookings():
        return Booking.objects.count()