#! /usr/bin/python3

import random
from models import *

"""
	console interface for pizzeria.
"""

def add_dough(description, price):
	row = Dough(dough_description = description, dough_price = price)
	row.save()

def find_all_doughs():
	return Dough.select()

def find_dough(dough_id):
	return Dough.get(Dough.id == dough_id)

def add_topping(description, price):
	row = Topping(topping_description = description, topping_price = price)
	row.save()

def find_all_toppings():
	return Topping.select()

def find_topping(topping_id):
	return Topping.get(Topping.id == topping_id)

def add_snacks(description, price):
	row = Snacks(snacks_description = description, snacks_price = price)
	row.save()

def find_all_snacks():
	return Snacks.select()

def find_snack(snacks_id):
	return Snacks.get(Snacks.id == snacks_id)

def set_ordered_toppings(name_of_your_order, topping_id):
	row = Ordered_toppings(name_of_your_order = name_of_your_order, topping_id = topping_id)
	row.save()

def pizza_construct(dough_id, name_of_your_order):
	dough = Dough.select().where(Dough.id == dough_id).get()
	title = str(dough.dough_description) + ' '
	for topping in Topping.select().join(Ordered_toppings).where(Ordered_toppings.name_of_your_order == name_of_your_order):
		title = title + str((topping.topping_description)) + ' '
	row = Pizza(dough_id = dough_id, list_ordered_toppings = name_of_your_order, pizza_title = title)
	row.save()
	return Pizza.get(Pizza.list_ordered_toppings == name_of_your_order)

def set_list_ordered_snacks(list_ordered_snacks, snacks_id):
	row = Ordered_snacks(name_of_your_order = list_ordered_snacks, snacks_id = snacks_id)
	row.save()

def set_order(pizza_id, name_of_your_order):
	dough = Dough.select().join(Pizza).where(Pizza.id == pizza_id).get()
	price = dough.dough_price
	for snack in Snacks.select().join(Ordered_snacks).where(Ordered_snacks.name_of_your_order == name_of_your_order):
		price = price + snack.snacks_price
	for topping in Topping.select().join(Ordered_toppings).where(Ordered_toppings.name_of_your_order == name_of_your_order):
		price = price + topping.topping_price
	row = Order(pizza_id = pizza_id, list_ordered_snacks = name_of_your_order, price_order = price)
	row.save()
	return Order.get(Order.list_ordered_snacks == name_of_your_order)

def set_transaction(transaction_id):
	row = Order_payment(transaction_id = transaction_id)
	row.save()

def set_person(f_name, l_name, adress, phone):
	row = Person(first_name = f_name, last_name = l_name, adress = adress, phone = phone)
	row.save()
	return row.id

def set_client(credit_card_indicator, client_deposit, date_enroller, date_terminate):
	row = Client_account(credit_card_indicator = credit_card_indicator, client_deposit = client_deposit, date_enroller = date_enroller, date_terminate = date_terminate)
	row.save()

def set_client_account(client_id, person_id):
	row = Client_account_person(client_account_id = client_id, person_id = person_id)
	row.save()

def set_employee(employee_tax_id, employee_job_category, person_id):
	row = Employee(employee_tax_id = employee_tax_id, employee_job_category = employee_job_category, person_id = person_id)
	row.save()

def find_all_employes():
	return Employee.select()

def find_employee(employee_id):
	employee = Employee.get(Employee.id == employee_id)
	return Person.get(Person.id == employee.id)

def set_client_transaction(client_account_id, employee_id):
	row = Client_transaction(client_account_id = client_account_id, employee_id = employee_id)
	row.save()

def check_correct_value(choise_of_option, diapason_of_choice, correction_variable):
	while True:
		if correction_variable == True:
			if not choise_of_option.isdigit() or not int(choise_of_option) in range(1, diapason_of_choice + 1):
				print('Может вы ошиблись?')
				return True
			else:
				return False
		else:
			if not choise_of_option.isdigit() or not int(choise_of_option) in range(1, diapason_of_choice + 1):
				print('Выход из меню выбора \n')
				return True
			else:
				return False


def main():
	try:
		Dough.create_table()
		Topping.create_table()	
		Ordered_toppings.create_table()
		Pizza.create_table()
		Snacks.create_table()
		Ordered_snacks.create_table()
		Order.create_table()
		Order_payment.create_table()
		Person.create_table()
		Client_account.create_table()
		Client_account_person.create_table()
		Employee.create_table()
		Client_transaction.create_table()

	except InternalError as px:
		print(str(px))
	

	while  True:
		who_are_you = input("""Шалом! Приветсвуем в нашей хычинной! 
			Представьтесь: 
			если вы пришли к нам наминаться - нажмите 1,
			если вы наш работник - нажмите 2,
			если посетитель - нажмите 3: """)
		if not check_correct_value(who_are_you, 3, True):
			if who_are_you == str(1):
				print("Заполните, пожалйства, ваш рабский контракт.")
				first_name = input("Введите ваше имя: ")
				last_name = input("Введите вашу фамилию: ")
				adress = input("Введите адрес проживания: ")
				phone = input("Введите телефон (не более десяти цифр): ")
				person_id = set_person(first_name, last_name, adress, phone)
				employee_tax_id = input("Введите желаемую пайку чечевичной похлёбки: ")
				employee_job_category = input("Введите желаемую должность: ")
				set_employee(employee_tax_id, employee_job_category, person_id)
				print('Добро пожаловать в вечное рабство, {}! Ха-ха-ха-ха!!!'.format(first_name))
				
			elif who_are_you == str(2):
				print("Бегом на кухню, лентяй! Принимайся за работу!")
				while  True:
					make_dough = input("Будем готовить тесто? Да или Нет: ")
					if make_dough == "Да" or make_dough == "да":
						dough_description = input("Какое тесто готовим?")
						dough_price = input("по какой цене тесто?")
						add_dough(dough_description, dough_price)
					else:
						break
				while True:
					make_topping = input("Будем делать топпинг? Да или Нет:")
					if make_topping == "Да" or make_topping == "да":
						topping_description = input("Какой топпинг будем готовить? ")
						topping_price = input("По какой цене? ")
						add_topping(topping_description, topping_price)
					else:
						break
				while  True:
					make_snacks = input("Будем готовить закусон? Да или Нет:")
					if make_snacks == "Да" or make_snacks == "да":
						snacks_description = input("Какой закусон делаем? ")
						snacks_price = input("По какой цене? ")
						add_snacks(snacks_description, snacks_price)
					else:
						break

			elif who_are_you == str(3):
				print("Добро пожаловать в хычинную 'У Ашота'. Здась Вас встретят вежливые официянты и накормят вкусной пиццей. Вкуснейшей на всей Малой Арнаутской!!!")
				name_of_your_order = input("Введите имя вашего заказа и ожидайте его выполнения: ")				

				doughs = find_all_doughs()
				dough_list = []
				for dough in doughs:
					dough_list.append({
						'ID: ': dough.id,
						'описание коржа:': dough.dough_description,
						'цена коржа: ': dough.dough_price,
						})
				print("В меню есть следующие типы коржей для пиццы: ", dough_list)
				while True:
					dough_id = input("Введите ID понравившегося коржа: ")
					if not check_correct_value(dough_id, len(dough_list), True):
						choised_dough = find_dough(dough_id)
						print('Вы выбрали корж: ', choised_dough.dough_description)
						break

				toppings = find_all_toppings()
				toppings_list = []
				for topping in toppings:
					toppings_list.append({
						'ID: ': topping.id,
						'описание топпинга: ': topping.topping_description,
						'цена топпинга: ': topping.topping_price,
						})
				print("В меню есть следующие топпинги: ", toppings_list)
				while True:
					topping_id = input("Введите ID понравившегося топпинга или что-либо другое для выхода из меню выбора: ")
					if not check_correct_value(topping_id, len(toppings_list), False):
						choised_topping = find_topping(topping_id)
						print("Вы выбрали топпинг: ", choised_topping.topping_description)
						set_ordered_toppings(name_of_your_order, choised_topping.id)
					else:
						break

				pizza = pizza_construct(dough_id, name_of_your_order)
				print("Вы собрали замечательную пиццу: ", pizza.pizza_title)

				snacks = find_all_snacks()
				snacks_list = []
				for snack in snacks:
					snacks_list.append({
						'ID: ': snack.id,
						'описание закуски: ': snack.snacks_description,
						'цена закуски: ': snack.snacks_price,
						})
				print("В меню есть следующие закуски: ", snacks_list)
				while  True:
					snack_id = input("Введите ID понравившегося закусона или что-то другое для выхода из меню выбора: ")
					if not check_correct_value(snack_id, len(snacks_list), False):
						choised_snack = find_snack(snack_id)
						print("Вы выбрали закусон: ", choised_snack.snacks_description)
						set_list_ordered_snacks(name_of_your_order, choised_snack.id)
					else:
						break

				you_order = set_order(pizza.id, name_of_your_order)
				print("Спасибо за покупку. С вас: ", you_order.price_order, " Кушайт, не обляпайтесь ))")
				your_waiter = find_employee(random.randint(1, len(find_all_employes())))

				print("Вас обслуживал официант: ", your_waiter.first_name, '\n')

				set_transaction(random.randint(1, 1000000))



if __name__ == '__main__':
	try:
		db.connect()
	except peewee.InternalError as px:
		print(str(px))
	main()