def global_loader(request):
    return {
        "show_loader": getattr(request, "show_loader", False)
    }