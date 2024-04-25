from django.db import models


class Author(models.Model):
    ID = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True)
    fam = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    otc = models.CharField(max_length=255, verbose_name='Отчество')
    phone = models.CharField(max_length=15, verbose_name='Телефон')


class Category(models.Model):
    Tanks = 'TK'
    Healers = 'HL'
    Damage_Dealer = 'DD'
    Merchants = 'MC'
    Guild_Masters = 'GM'
    Quest_Givers = 'QG'
    Blacksmiths = 'BM'
    Tanners = 'TN'
    Potion_Makers = 'PM'
    Spell_Masters = 'SM'

    STATUS_CHOICES = (
        ('TK', 'Танки'),
        ('HL', 'Хилы'),
        ('DD', 'ДД'),
        ('MC', 'Торговцы'),
        ('GM', 'Гилдмастеры'),
        ('QG', ' Квестгиверы'),
        ('BM', 'Кузнецы'),
        ('TN', 'Кожевники'),
        ('PM', 'Зельевары'),
        ('SM', 'Мастера заклинаний'),
    )


class Post(models.Model):
    status = models.CharField(max_length=2, choices=Category.STATUS_CHOICES, default=Category.Tanks)

    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Image(models.Model):
    data = models.CharField(max_length=2083)
    title = models.CharField(max_length=255, verbose_name='заголовок')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.pk} {self.title}'


class Video(models.Model):
    data = models.CharField(max_length=2083)
    title = models.CharField(max_length=255, verbose_name='заголовок')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return f'{self.pk} {self.title}'


class File(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return f'{self.pk} {self.title}'


class Reply(models.Model):
    reply_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
