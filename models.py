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


class Topping(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	topping_description = CharField(null = False, max_length = 50)
	topping_price = FloatField(default=None)


class Ordered_toppings(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	name_of_your_order = CharField(max_length = 200, default = 'order')
	topping_id = ForeignKeyField(Topping, on_delete = 'CASCADE')


class Pizza(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	dough_id = ForeignKeyField(Dough, on_delete = 'CASCADE')
	list_ordered_toppings = ForeignKeyField(Ordered_toppings, field = "name_of_your_order", on_delete = 'CASCADE')
	pizza_title = CharField(null = False, max_length = 200)


class Snacks(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	snacks_description = CharField(null = False, max_length = 50)
	snacks_price = FloatField(default=None)


class Ordered_snacks(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	name_of_your_order = CharField(max_length = 200, default = 'order')
	snacks_id = ForeignKeyField(Snacks, on_delete = 'CASCADE')


class Order(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	date_order = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
	pizza_id = ForeignKeyField(Pizza, on_delete = 'CASCADE')
	list_ordered_snacks = ForeignKeyField(Ordered_snacks, on_delete = 'CASCADE')
	price_order = FloatField(default=None)


class Order_payment(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	transaction_id = IntegerField()


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


class Client_transaction(BaseModel):
	id = IntegerField(null = False, primary_key = True)
	client_account_id = ForeignKeyField(Client_account, on_delete = 'CASCADE')
	employee_id = ForeignKeyField(Employee, on_delete = 'CASCADE')
	transaction_date = DateTimeField(default = datetime.datetime.now())
	sales_tax = FloatField(default = 0.05)