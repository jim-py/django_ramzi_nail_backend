from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    role = models.ForeignKey('Role', verbose_name='Роль', on_delete=models.CASCADE, null=True, blank=True)
    telephone = models.BigIntegerField(verbose_name='Телефон', null=True, blank=True, unique=True)
    USERNAME_FIELD = 'telephone'

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
        ordering = ['last_name']

    def __str__(self):
        return f'{self.first_name} - {self.telephone}'


class Role(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название роли')

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Status(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название статуса')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class TypeDocument(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип документ'
        verbose_name_plural = 'Типы документа'
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Course(models.Model):
    type_document = models.ForeignKey('TypeDocument', verbose_name='Документ', on_delete=models.CASCADE)
    name = models.TextField(verbose_name='Название')
    cost = models.IntegerField(verbose_name='Цена')
    old_cost = models.IntegerField(verbose_name='Старая цена')
    format = models.TextField(verbose_name='Формат обучения')
    term = models.TextField(verbose_name='Срок обучения')
    program = models.TextField(verbose_name='Программа')
    extra = models.TextField(verbose_name='Дополнительно')
    show = models.BooleanField(verbose_name='Отображать на главной странице?')
    photo = models.ImageField(upload_to='Courses', verbose_name='Фото')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['pk']

    def __str__(self):
        return f'{self.name} - {self.cost} руб.'


class Request(models.Model):
    user = models.ForeignKey('User', verbose_name='Пользователь', on_delete=models.CASCADE)
    timesheet = models.ForeignKey('Timesheet', verbose_name='Расписание', on_delete=models.CASCADE)
    status = models.ForeignKey('Status', verbose_name='Статус', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'
        ordering = ['-date']

    def __str__(self):
        return f'{self.user} - {self.timesheet} - {self.status}'


class Timesheet(models.Model):
    course = models.ForeignKey('Course', verbose_name='Курс', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количество мест')
    date = models.DateField(verbose_name='Дата начала')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
        ordering = ['-date']

    def __str__(self):
        return f'{self.date} - мест: {self.quantity}'
