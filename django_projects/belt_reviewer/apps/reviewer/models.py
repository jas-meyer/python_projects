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
				errors['passwords'] = "The confirmation password must match the password"
			if len(postData['password']) < 8:
				errors['password'] = "The password needs to be at least 8 characters" 
			if len(postData['name']) < 3:
				errors["name"] = "First name should be more than 3 characters"
			if len(postData['alias']) < 3:
				errors["alias"] = "Last name should be more than 3 characters"
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
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
class Author(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(Author, related_name="books")
	users = models.ManyToManyField(User, related_name = "books2")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
class Review(models.Model):
	rating = models.IntegerField()
	text = models.TextField()
	user = models.ForeignKey(User, related_name="reviews")
	book = models.ForeignKey(Book, related_name="reviews2")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)



