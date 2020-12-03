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


# 练习创建多对多字段
class people(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return '姓名: %s' % self.name


class tag(models.Model):
    """这是使用 models 的自带的 manytomany字段 ， 很好用，但是缺点生成的第三张表只有三列"""
    _property = models.CharField(max_length=64)
    people_to_tag = models.ManyToManyField(to="people", related_name="ptt")

    def __str__(self):
        return "%s 特征: %s" % (self.people_to_tag.all().values("name")[0]["name"], self._property)


class peo_to_tag(models.Model):
    """自己编写的第三张表函数, 想要多少列就可以自己自定义，
    这二种方式选一种就可以了， 不需要二个都设置"""
    p = models.ForeignKey(to="people", db_index=True, on_delete=models.CASCADE)
    t = models.ForeignKey(to="tag", db_index=True, on_delete=models.CASCADE)
    n_date = models.DateField()

    class Meta:
        # 这是元类型， 联合唯一 还没涉及到
        unique_together = [
            ('p', 't'),
        ]

    def __str__(self):
        return "%s 特征: %s" % (self.p.name, self.t._property)
