from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
	def basic_validator(self, postData, data):
		errors = {}
		if len(data) > 1:
			errors['email'] = "Email is already in the database!"   
		else:
			if postData['password'] != postData['confirm']:
				errors['password'] = "The confirmation password must match the password"
			if len(postData['firstname']) < 3:
				errors["firstname"] = "First name should be more than 3 characters"
			if len(postData['lastname']) < 3:
				errors["lastname"] = "Last name should be more than 3 characters"
			if not EMAIL_REGEX.match(postData['email']):
				errors["email"] = "Please enter a valid email address"
		return errors
	def password_check(self, postData, data):
		errors = {}
		if len(postData['logemail']) < 1:
			errors["email"] = "Email field should not be blank"
		elif len(data) < 1:
			errors['email'] = "Email is not in database!"
		else:
			logpass = str(postData['logpassword'])
			storedpass = data[0].password
			if not bcrypt.checkpw(logpass .encode(), storedpass .encode()):
				errors['password'] = "Password does not match"
		return errors
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
# Create your models here.
