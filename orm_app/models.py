# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogEntryScores(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_entry_scores'


class BlogInfo(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'blog_info'


class BlogUniversities(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.SmallIntegerField()
    link = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog_universities'


class Countries(models.Model):
    country_id = models.TextField(primary_key=True)
    country_name = models.TextField()
    region = models.ForeignKey('Regions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'countries'


class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.TextField()
    location = models.ForeignKey('Locations', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'departments'


class Dependents(models.Model):
    dependent_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    relationship = models.TextField()
    employee = models.ForeignKey('Employees', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dependents'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField()
    email = models.TextField()
    phone_number = models.TextField(blank=True, null=True)
    hire_date = models.TextField()
    job = models.ForeignKey('Jobs', models.DO_NOTHING)
    salary = models.TextField()  # This field type is a guess.
    manager = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employees'


class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.TextField()
    min_salary = models.TextField()  # This field type is a guess.
    max_salary = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'jobs'


class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    street_address = models.TextField(blank=True, null=True)
    postal_code = models.TextField(blank=True, null=True)
    city = models.TextField()
    state_province = models.TextField(blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'locations'


class Regions(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'regions'
