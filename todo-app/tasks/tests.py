from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):

    def test_task_creation(self):
        """Un task créé doit avoir done=False par défaut"""
        task = Task(title="Apprendre Jenkins")
        self.assertEqual(task.done, False)

    def test_mark_done(self):
        """mark_done() doit passer done à True"""
        task = Task.objects.create(title="Configurer SonarQube")
        task.mark_done()
        self.assertTrue(task.done)

    def test_str_representation(self):
        """__str__ doit retourner le titre"""
        task = Task(title="Finir le projet")
        self.assertEqual(str(task), "Finir le projet")
