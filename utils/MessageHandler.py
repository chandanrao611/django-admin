from django.contrib import messages
class MessageHandler:
    LOGIN_SUCCESS = "You are now logged in successfully."
    LOGOUT_SUCCESS = "You have been logged out."
    INVALID_CREDENTIALS = "Invalid username or password."
    SAVE_SUCCESS = "Data saved successfully."
    DELETE_SUCCESS = "Data deleted successfully."

    @staticmethod
    def success(request, message):
        messages.success(request, message)

    @staticmethod
    def error(request, message):
        messages.error(request, message)

    @staticmethod
    def warning(request, message):
        messages.warning(request, message)

    @staticmethod
    def info(request, message):
        messages.info(request, message)