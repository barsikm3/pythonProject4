def get_event_date(event):
    return event.date
def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machines not in machines:
            machines[event.machines] = set()
        if event.type == "login":
            machines[event.machines].add(event.user)
        elif event.type == "logout":
            machines[event.machines].remove(event.user)
    return machines
def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            users_list = ", ".join(users)
        print("{}: {}".format(machine, users_list))