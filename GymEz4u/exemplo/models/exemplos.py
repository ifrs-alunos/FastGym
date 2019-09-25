from exemplo.models.base import *
from django.contrib.auth.models import User

class Example(BaseModel):
    owner = models.ManyToManyField(User, verbose_name="Account Owner")
    description = models.CharField(max_length=200, help_text='The description for you example')
    number = models.CharField(max_length=20, help_text='Insert your example number here')
    balance = models.FloatField(default=0, help_text='Insert your initial balance')
 
    class Meta:
        pass

    def __str__(self):
        return "{}: {} - {} ".format(self.number, self.description, self.balance)

    def update_balance(self, value):
        try:
            self.balance = self.balance + float(value)
            return True
        except:
            return False

    def get_balance(self):
        return self.balance

