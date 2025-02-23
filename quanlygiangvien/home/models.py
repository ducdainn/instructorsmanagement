from django.db import models
import random

class Department(models.Model):
    departmentID = models.CharField(max_length=5, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.departmentID

    
class Instructor(models.Model):
    instructorID = models.CharField(max_length=7, primary_key=True, editable=False)
    image =models.ImageField(upload_to='images/instructorAvatars/') 
    name = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    POSITION_CHOICES = [
        ('Trợ giảng', "Trợ giảng"),
        ('Giảng viên', "Giảng viên"),
        ('Phó giáo sư', "Phó giáo sư"),
        ('Giáo sư', "Giáo sư"),
    ]
    EDUCATIONLEVEL_CHOICES = [
        ('Cử nhân', "Cử nhân"),
        ('Thạc sĩ', "Thạc sĩ"),
        ('Tiến sĩ', "Tiến sĩ"),
    ]
    DEPARTMENT_CHOICES = [
        ('FME', 'Khoa Công nghệ Cơ khí'),
        ('FIT', 'Khoa Công nghệ Thông tin'),
        ('FEET', 'Khoa Công nghệ Điện tử'),
        ('FHRE', 'Khoa Công nghệ Nhiệt lạnh'),
        ('FFS', 'Khoa Khoa học Cơ bản'),
        ('FCE', 'Khoa Công nghệ Hoá học'),
        ('FGD', 'Khoa Công nghệ may- Thời trang'),
        ('FPT', 'Khoa Lý luận Chính trị'),
        ('FFL', 'Khoa Ngoại ngữ'),
        ('FBA', 'Khoa Quản trị Kinh doanh'),
        ('FCT', 'Khoa Thương mại- Du lịch'),
        ('LF', 'Khoa Luật'),
        # More
    ]
    STATUS_CHOICES = [
        ('Đang dạy', "Đang dạy"),
        ('Nghỉ hưu', "Nghỉ hưu"),
        ('Nghỉ việc', "Nghỉ việc"),
        ('Hợp đồng', "Hợp đồng"),
        ('Nghỉ phép', "Nghỉ phép"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    place_of_birth = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100, choices=EDUCATIONLEVEL_CHOICES)
    job_position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    status = models.CharField(max_length=50,choices= STATUS_CHOICES)
    def save(self, *args, **kwargs):
        if not self.instructorID:
            self.instructorID = self.generate_instructorID()
        super().save(*args, **kwargs)
    @staticmethod
    def generate_instructorID():
        prefix = "GV"
    # Lấy số lượng Instructor hiện tại
        count = Instructor.objects.count()
    # Kiểm tra nếu không có Instructor nào tồn tại
        if count == 0:
            return f"{prefix}00001"
    # Tạo ID dựa trên số lượng hiện tại
        next_id = f"{prefix}{count+1:05}"
    # Kiểm tra nếu ID đã tồn tại
        while Instructor.objects.filter(instructorID=next_id).exists():
        # Tăng biến đếm và tạo lại ID
            count += 1
            next_id = f"{prefix}{count+1:05}"
        return next_id

    def __str__(self):
        return self.name
    
# bài báo
class Article(models.Model):
    articleID = models.CharField(max_length=7, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/articleImg/', blank=True, null=True)
    upload_file = models.FileField(upload_to='files/', blank=True, null=True)  
    content = models.TextField()
    publish_date = models.DateField(auto_now=True)
    def save(self, *args, **kwargs):
        if not self.articleID:
            self.articleID = self.generate_articleID()
        super().save(*args, **kwargs)
    @staticmethod
    def generate_articleID():
        prefix = "AR"
        count = Article.objects.count()
        if count == 0:
            return f"{prefix}00001"

        next_id = f"{prefix}{count+1:05}"
        while Article.objects.filter(articleID=next_id).exists():
            count += 1
            next_id = f"{prefix}{count+1:05}"
        return next_id
    def __str__(self):
        return self.title