from django.db import models


# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=202)
    image = models.ImageField(upload_to='collection/')

    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class About(models.Model):
    full_name = models.CharField(max_length=202)
    image = models.ImageField(upload_to='about/')
    body = models.TextField()
    twitter = models.CharField(max_length=202)
    instagram = models.CharField(max_length=202)
    fasebook = models.CharField(max_length=202)

    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField(upload_to='blog/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    bodyone = models.TextField()
    bodytwo = models.TextField()
    tag = models.ManyToManyField(Tag, )

    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=202)
    email = models.EmailField()
    phone = models.CharField(max_length=202)
    message = models.TextField()

    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Contact(models.Model):
    full_name = models.CharField(max_length=202)
    email = models.EmailField()
    phone = models.CharField(max_length=202)
    message = models.TextField()

    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Newslatter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
