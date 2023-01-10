from django.db import models
from django.urls import reverse
from slugify import slugify
import uuid


class Incident(models.Model):

    class LegalChoices(models.TextChoices):
        YES = 'YES', 'Легетимно'
        NONE = 'NONE', 'Не определено'
        NO = 'NO', 'Нарушение'

    title = models.CharField(max_length=255,
                            db_index=True,
                            verbose_name='Название инцидента',
                            blank=False,
                            null=False,
                            default='Неизвестный инцидент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Тип инцидента')
    # legal = models.BooleanField(default=True, verbose_name='Легетимность')
    legal = models.CharField(max_length=5, choices=LegalChoices.choices, default=LegalChoices.NONE, verbose_name='Легетимность')
    image = models.ImageField(upload_to='icons/example/%Y/%m/%d/', null=True, blank=True, verbose_name='Изображение')
    ip = models.GenericIPAddressField(protocol='IPv4',
                            verbose_name='Ip адресс источника',
                            blank=True,
                            null=True,
                            default='0.0.0.0')
    hostname = models.CharField(max_length=255,
                                verbose_name='Имя компьютера источника',
                                blank=True,
                                null=True,
                                default='ARM')

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('incident', kwargs={'pk':self.pk})

    def get_label_choice(self):
        return Incident.LegalChoices(self.legal).label

    def save(self, *args, **kwargs):
        '''Incident autocomplete'''
        if self.category is None:
            example_incident = ExampleIncident.objects.select_related('category').filter(title=self.title)
            if example_incident:
                example_incident = example_incident[0]
            if not bool(example_incident):
                example_incident = ExampleIncident.objects.select_related('category').get(title='Неизвестный инцидент')
            self.category = example_incident.category
            self.image = example_incident.image
            self.legal = example_incident.legal
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Инцидент'
        verbose_name_plural = 'Инциденты'
        ordering = ['-created_at']

    

class Category(models.Model):
    title = models.CharField(max_length=255,
                            db_index=True,
                            verbose_name='Тип инцидента',
                            blank=False,
                            null=False,
                            default='Неизвестный тип')
    slug = models.SlugField(null=False, blank=False, editable=False, unique=True)
    image = models.ImageField(upload_to='icons/category/%Y/%m/%d/', null=True, blank=True, verbose_name='Изображение')

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        if not bool(Category.objects.filter(slug=slug)):
            self.slug = slug
            return super().save(*args, **kwargs)
        like_slug_list = Category.objects.filter(slug__contains=slug)
        if like_slug_list:
            slug = f'{slug}-{len(like_slug_list)+1}'
        has_slug = Category.objects.filter(slug=slug)
        if has_slug:
            slug = f'{slugify(self.title)}-{len(like_slug_list)-1}'
        self.slug = slug
        print(f'SLUG {self.slug}')
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
        ordering = ['title']
    
    
class ExampleIncident(models.Model):

    class LegalChoices(models.TextChoices):
        YES = 'YES', 'Легетимно'
        NONE = 'NONE', 'Не определено'
        NO = 'NO', 'Нарушение'

    title = models.CharField(max_length=255,
                            db_index=True,
                            verbose_name='Название известного инцидента',
                            blank=False,
                            null=False,
                            default='Неизвестный инцидент')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, verbose_name='Тип инцидента', related_name='category')
    legal = models.CharField(max_length=5, choices=LegalChoices.choices, default=LegalChoices.NONE, verbose_name='Легетимность')
    image = models.ImageField(upload_to='icons/example/%Y/%m/%d/', null=True, blank=True, verbose_name='Изображение')

    def get_absolute_url(self):
        return reverse('example', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

    def get_label_choice(self):
        return Incident.LegalChoices(self.legal).label


    class Meta:
        verbose_name = 'Известный инцидент'
        verbose_name_plural = 'Известные инциденты'
        ordering = ['category']
