from django.db import transaction
from db.models import User, Order, Ticket


@transaction.atomic
def create_order(tickets: list[dict], username: str, date: str = None):
        user = User.objects.get(username=username)
        order = Order.objects.create(user=user)
        if date is not None:
            order.created_at = date
            order.save()

        for ticket in tickets:
            Ticket.objects.create(order=order, row=ticket['row'], seat=ticket['seat'], movie_session_id=ticket['movie_session'])

        return order

def get_orders(username: str = None):
    if username is not None:
        user = User.objects.get(username=username)
        return Order.objects.filter(user=user)
    else:
        return Order.objects.all()