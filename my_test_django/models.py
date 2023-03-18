from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Worker(models.Model):
    fullname = models.CharField("ФИО",max_length=100)
    position = models.CharField("Должность",max_length=100)
    rank = models.CharField("Уровень",max_length=30)
    email = models.CharField("Эл.Почта",max_length=100)
    login = models.CharField("Логин",max_length=50)

    def __str__(self):
        return self.fullname

class Project(models.Model):
    title = models.CharField("Название проекта",max_length=200)
    key = models.CharField("Ключ проекта",max_length=20)
    manager = models.ForeignKey(Worker, verbose_name="Руководитель", on_delete=models.SET_NULL, null=True)
    id_project_in_jira = models.IntegerField()  # id проекта в Jira

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField("Название",max_length=300)
    key = models.CharField("Ключ",max_length=20)
    time_original_estimate = models.IntegerField('Оценочное время на выполнение (сек)')
    duedate = models.DateField('Дедлайн') # Нет для MLAI !!!
    assignee = models.ForeignKey(Worker,verbose_name='Исполнитель',on_delete = models.PROTECT) # 'ID исполнителя задачи из таблицы worker',
    project = models.ForeignKey(Project,verbose_name='Проект',on_delete = models.CASCADE) # 'ID проекта',
    author = models.ForeignKey(Worker,verbose_name='Автор', on_delete = models.PROTECT,related_name="author_id") # 'ID создатель задачи из таблицы worker',
    start_date = models.DateField('Дата начала работы над задачей')
    deleted = models.DateField() # Дата удаления задачи, None - задача не удалена
    description = models.CharField("Описание", max_length=3000)
    id_task_in_jira = models.IntegerField()  # id задачи в jira
    date_create = models.DateField()  # дата создания задачи

    def __str__(self):
        return self.title