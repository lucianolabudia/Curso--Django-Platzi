from audioop import reverse
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.

# Models
class QuestionModelTests(TestCase):

    # se define cada test, cada test es un metodo de esta clase
    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime. timedelta(days=30)
        future_question = Question(question_text="¿Quien es el mejor Course Diretor de Platzi?", pub_date=time)
        #verificamos q el resultado de aplicar el metodo es igual a falso
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_past_questions(self):
        """was_published_recently() must return Flase for questions whose pub_date is more than 1 day in the past"""
        time = timezone.now() - datetime.timedelta(days=30)
        past_question = Question(question_text="¿Quien es el mejor Course Direct de Platzi?",pub_date=time)
        self.assertIs(past_question.was_published_recently(),False)

    def test_was_published_recently_with_present_questions(self):
        """was_published_recently() must return True for questions whose pub_date is actual"""
        time = timezone.now()
        present_question = Question(question_text="¿Quien es el mejor Course Direct de Platzi?",pub_date=time)
        self.assertIs(present_question.was_published_recently(),True)


# Views
class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        """If no question exist, an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])