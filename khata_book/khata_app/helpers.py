from .models import Khata_book


def grand_total(datas):
    amount = 0
    for data in datas:
        amount += data.total_amount
    return amount


def getClientList(user=None, client=None):
    user_data = Khata_book.objects.filter(user=user)
    if client is None:
        entries = user_data.values('client_name').distinct()
        all_clients = {}
        for entry in entries:
            # gives arranged lists of same clients
            name = list(entry.values())
            # gives query sets of that particular client, so that we can display it further
            data_sets = user_data.filter(client_name=name[0])

            all_clients[data_sets[0]] = grand_total(data_sets)
        # passing the final list of query set to the frontend
        return all_clients
    else:
        entries = user_data.filter(client_name=client).distinct()
        all_clients = {}
        for entry in entries:
            data_sets = user_data.filter(client_name=client)
            all_clients[data_sets[0]] = grand_total(data_sets)
        # passing the final list of query set to the frontend
        return all_clients
