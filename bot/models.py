from django.db import models

class Message(models.Model):
    #main
    chat_id = models.CharField(max_length=256, blank=False)
    message_id = models.CharField(max_length=256, blank=False)
    #user meta
    username = models.CharField(max_length=256, default=None, null=True)
    first_name = models.CharField(max_length=256, default=None, null=True)
    last_name = models.CharField(max_length=256, default=None, null=True)
    #message meta
    text = models.TextField(default=None, null=True)
    callback = models.CharField(max_length=256, default=None, null=True)
    video = models.CharField(max_length=256, default=None, null=True)
    audio = models.CharField(max_length=256, default=None, null=True)
    voice = models.CharField(max_length=256, default=None, null=True)
    video_note = models.CharField(max_length=256, default=None, null=True)
    document = models.CharField(max_length=256, default=None, null=True)

    def __str__(self):
        return self.name
    





    class Student:
    def __init__(self, name, age, grade):
        self._name = name
        self._age = age
        self._grade = grade

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def grade(self):
        return self._grade

# Create an instance of the Student class
student = Student("John", 18, "A")

# Access the fields using the properties
print(student.name)   # Output: John
print(student.age)    # Output: 18
print(student.grade)  # Output: A