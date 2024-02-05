from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
from django.conf import settings
from decimal import Decimal


# Create your views here.


def view_bag(request):
    """A view that renders the bag contents page"""
    bag = request.session.get("bag", {})

    bag_items = []
    total = 0
    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        # this means we are dealing with sizes
        if isinstance(item_data, dict):
            for size, quantity in item_data["items_by_size"].items():
                total += quantity * product.price
                bag_items.append(
                    {
                        "item_id": item_id,
                        "product": product,
                        "size": size,
                        "quantity": quantity,
                    }
                )
        else:  # this means no size is associated
            total += item_data * product.price
            bag_items.append(
                {
                    "item_id": item_id,
                    "product": product,
                    "quantity": item_data,
                }
            )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * \
            Decimal(
                settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        "bag_items": bag_items,
        "grand_total": grand_total,
        "total": total,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
    }

    return render(request, "bag/bag.html", context)


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")

    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    bag = request.session.get("bag", {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]["items_by_size"].keys():
                bag[item_id]["items_by_size"][size] += quantity
                messages.success(
                    request,
                    f'''
                    Updated size {size.upper()} {product.name} quantity to
                    {bag[item_id]["items_by_size"][size]}
                    ''',
                )
            else:
                bag[item_id]["items_by_size"][size] = quantity
                messages.success
                (
                    request,
                    f"Added size {size.upper()} {product.name} to your bag"
                )
        else:
            bag[item_id] = {
                "items_by_size": {size: quantity}}
            messages.success(
                request,
                f"Added size {size.upper()} {product.name} to your bag"
            )
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f"Updated {product.name} quantity to {bag[item_id]}"
            )
        else:
            bag[item_id] = quantity
            messages.success(
                request, f"Added {product.name} to your bag")

    request.session["bag"] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    bag = request.session.get("bag", {})

    if size:
        if quantity > 0:
            bag[item_id]["items_by_size"][size] = quantity
            messages.success(
                request,
                f'''Updated size {size.upper()}
                {product.name}
                quantity to {bag[item_id]["items_by_size"][size]}''',
            )
        else:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
            messages.success(
                request,
                f"Removed size {size.upper()} {product.name} from your bag"
            )
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f"Updated {product.name} quantity to {bag[item_id]}"
            )
        else:
            bag.pop(item_id)
            messages.success(
                request, f"Removed {product.name} from your bag")

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if "product_size" in request.POST:
            size = request.POST["product_size"]
        bag = request.session.get("bag", {})

        if size:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
            messages.success(
                request,
                f"Removed size {size.upper()} {product.name} from your bag"
            )
        else:
            bag.pop(item_id)
            messages.success(
                request, f"Removed {product.name} from your bag")

        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
