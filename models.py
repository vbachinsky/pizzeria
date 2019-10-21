from peewee import *
import datetime

"""
	Collection of models for pizzerias
"""

db = SqliteDatabase('pizza_peewee.db')

class BaseModel(Model):
	class Meta:
		database = db
		order_by = ('id')

class Dough(BaseModel):
	id = PrimaryKeyField(null = False)
	dough_description = CharField(null = False, max_length = 50)
	dough_price = FloatField(default=None)

	def add_dough(description, price):
		row = Dough(dough_description = description, dough_price = price)
		row.save()

	def find_all_doughs():
		return Dough.select()

	def find_dough(dough_id):
		return Dough.get(Dough.id == dough_id)


class Topping(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	topping_description = CharField(null = False, max_length = 50)
	topping_price = FloatField(default=None)

	def add_topping(description, price):
		row = Topping(topping_description = description, topping_price = price)
		row.save()

	def find_all_toppings():
		return Topping.select()

	def find_topping(topping_id):
		return Topping.get(Topping.id == topping_id)


class Ordered_toppings(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	name_of_your_order = CharField(max_length = 200, default = 'order')
	topping_id = ForeignKeyField(Topping, on_delete = 'CASCADE')

	def set_ordered_toppings(name_of_your_order, topping_id):
		row = Ordered_toppings(name_of_your_order = name_of_your_order, topping_id = topping_id)
		row.save()


class Pizza(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	dough_id = ForeignKeyField(Dough, on_delete = 'CASCADE')
	list_ordered_toppings = ForeignKeyField(Ordered_toppings, field = "name_of_your_order", on_delete = 'CASCADE')
	pizza_title = CharField(null = False, max_length = 200)


class Snacks(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	snacks_description = CharField(null = False, max_length = 50)
	snacks_price = FloatField(default=None)

	def add_snacks(description, price):
		row = Snacks(snacks_description = description, snacks_price = price)
		row.save()

	def find_all_snacks():
		return Snacks.select()

	def find_snack(snacks_id):
		return Snacks.get(Snacks.id == snacks_id)


class Ordered_snacks(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	name_of_your_order = CharField(max_length = 200, default = 'order')
	snacks_id = ForeignKeyField(Snacks, on_delete = 'CASCADE')

	def set_list_ordered_snacks(list_ordered_snacks, snacks_id):
		row = Ordered_snacks(name_of_your_order = list_ordered_snacks, snacks_id = snacks_id)
		row.save()



class Order(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	date_order = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
	pizza_id = ForeignKeyField(Pizza, on_delete = 'CASCADE')
	list_ordered_snacks = ForeignKeyField(Ordered_snacks, on_delete = 'CASCADE')
	price_order = FloatField(default=None)


class Order_payment(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	transaction_id = IntegerField()

	def set_transaction(transaction_id):
		row = Order_payment(transaction_id = transaction_id)
		row.save()



class Person(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	first_name = CharField(null = False, max_length = 20)
	last_name = CharField(max_length = 20)
	adress = CharField(max_length = 100)
	phone = CharField(max_length = 10)


class Client_account(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	credit_card_indicator = BooleanField(default = False)
	client_deposit = BooleanField(default = False)
	date_enroller = DateField()
	date_terminate = DateField()


class Client_account_person(BaseModel):
	client_account_id = ForeignKeyField(Client_account, on_delete = 'CASCADE')
	person_id = ForeignKeyField(Person, on_delete = 'CASCADE')


class Employee(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	person_id = ForeignKeyField(Person, on_delete = 'CASCADE')
	employee_tax_id = FloatField(default=None)
	employee_job_category = CharField(max_length = 100)

	def find_all_employes():
		return Employee.select()


class Client_transaction(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	client_account_id = ForeignKeyField(Client_account, on_delete = 'CASCADE')
	employee_id = ForeignKeyField(Employee, on_delete = 'CASCADE')
	transaction_date = DateTimeField(default = datetime.datetime.now())
	sales_tax = FloatField(default = 0.05)

	def set_client_transaction(client_account_id, employee_id):
		row = Client_transaction(client_account_id = client_account_id, employee_id = employee_id)
		row.save()