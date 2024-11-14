from serial.models import Serial, Category
import random
from django.utils import timezone


def serial_list(request):
    serials = Serial.objects.all()[:6]

    return {"serials": serials}


def recent_serial(request):
    recent_serials = Serial.objects.all().order_by("-created_at")[:6]

    return {"recent_serials": recent_serials}


def live_action(request):
    live_action_category = Category.objects.filter(name="live action").first()

    if live_action_category:
        serial_live_action = Serial.objects.filter(category=live_action_category).order_by("-created_at")[:6]
    else:
        serial_live_action = Serial.objects.none()

    return {"serial_live_action": serial_live_action}


def popular(request):
    popular_serial = Serial.objects.all().order_by("-score")[:6]

    return {"popular_serial": popular_serial}


def hero_serial(request):
    hero_serials = Serial.objects.all().order_by("-created_at")[:3]
    return {"hero_serials": hero_serials}


def random_serial(request):
    serials = list(Serial.objects.all())
    random_serials = random.sample(serials, min(4, len(serials)))

    return {"random_serials": random_serials}


def categories(request):
    category_list = Category.objects.all()

    return {"category_list": category_list}


def serials_view(request):
    filter_type = request.GET.get('filter', 'day')
    now = timezone.now()

    if filter_type == '.week':
        start_date = now - timezone.timedelta(weeks=4)
    elif filter_type == '.month':
        start_date = now - timezone.timedelta(days=30)
    elif filter_type == '.years':
        start_date = now - timezone.timedelta(days=365)
    else:
        start_date = now - timezone.timedelta(days=1)

    serials_filter = Serial.objects.filter(created_at__lte=start_date)

    return {"sidebar": serials_filter}
