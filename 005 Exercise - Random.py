import random


def generate_tickets(ticket_count, max_number):
	ticket_list = random.sample(range(0, max_number), ticket_count)
	winning_ticket = random.choice(ticket_list)
	return ticket_list, winning_ticket


result = generate_tickets(5, 10)
print(result)
