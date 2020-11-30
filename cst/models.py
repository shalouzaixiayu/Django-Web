from django.db import models


# Create your models here.

class Student(models.Model):
    # 定义学生表属性
    name = models.CharField(verbose_name="学生名", max_length=20)
    age = models.IntegerField(verbose_name="年龄")
    choice = [
        ("boy", "男性"),
        ("girl", "女性"),
    ]
    gender = models.CharField(verbose_name="性别", choices=choice, default="boy", max_length=10)
    phone_number = models.CharField(verbose_name="移动电话", default=None, max_length=11, blank=True)

    student_class = models.ForeignKey("Class", related_name="stu_class", on_delete=models.CASCADE)

    def __str__(self):
        class_nid = ""
        for obj in self.student_class.class_name:
            class_nid += obj
        return f"姓名: {self.name} | 年龄: {self.age} | 性别: {self.gender} \t\t\t|" \
               f"所在班级: {class_nid}"


class Class(models.Model):
    #  定义班级字段属性
    class_name = models.CharField(verbose_name="班级名称", max_length=30)

    class_teacher = models.ManyToManyField("Teacher", related_name="class_teacher")

    def __str__(self):
        teacher_name = ""
        for obj in self.class_teacher.values("name"):
            teacher_name += (obj.get("name", None) + "\t")

        return f"班级名称: {self.class_name}|  班级教师总数: {self.class_teacher.count()}\t\t|" \
               f"教师名称: {teacher_name}"


class Teacher(models.Model):
    # 定义教师表属性
    name = models.CharField(verbose_name="教师名", max_length=20)
    age = models.IntegerField(verbose_name="年龄")
    choice = [
        ("boy", "男性"),
        ("girl", "女性"),
    ]
    gender = models.CharField(verbose_name="性别", choices=choice, default="boy", max_length=10)
    phone_number = models.CharField(verbose_name="移动电话", default=None, max_length=11, blank=True)

    teacher_object = models.CharField(verbose_name="所授课程", max_length=30, blank=True, default=None)
    teacher_worked_years = models.IntegerField(verbose_name="任教年限", default=None, blank=True)

    def __str__(self):
        gender_s = "男性" if self.gender == "boy" else "女性"
        return f"姓名: {self.name} | 年龄: {self.age}  | 性别: {gender_s} |  所授课程：{self.teacher_object} |  授课年限： {self.teacher_worked_years}"


