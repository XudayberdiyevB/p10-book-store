from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    class LanguageTypes(models.TextChoices):
        UZBEK = 'uzbek', 'Uzbek'
        RUSSIAN = 'russian', 'Russian'
        ENGLISH = 'english', 'English'

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.FloatField()
    sales_price = models.PositiveSmallIntegerField(default=0)
    best_seller = models.BooleanField(default=False)
    pub_year = models.PositiveIntegerField(null=True)
    page_size = models.PositiveIntegerField()
    lang = models.CharField(max_length=50, choices=LanguageTypes.choices)
    file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="books")
    author = models.ForeignKey("BookAuthor", on_delete=models.CASCADE, related_name="books")
    tags = models.ManyToManyField("books.Tag", related_name="books")

    def __str__(self):
        return self.title

    @property
    def images_count(self):
        return self.images.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class BookAuthor(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)


class BookImage(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="books")

    def __str__(self):
        return str(self.book)
