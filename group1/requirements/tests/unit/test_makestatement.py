from django.test import TestCase
from django.contrib.auth.models import User
from requirements import models
from requirements.models import project
from requirements.models import project_api
from requirements.models import user_association
from requirements.models import user_manager
from requirements.models import story
from requirements.models.project import Project
from requirements.models.user_association import UserAssociation
from requirements.models.iteration import Iteration
from requirements.models.story import Story
from requirements.models import filemaker
import datetime

class MakeStateMentTestCase(TestCase):

    def setUp(self):
        self.__clear()

        self.__project = Project(title="title", description="desc")
        self.__project.save()
        self.__user = User(username="testUser", password="pass")
        self.__user.save()

    def tearDown(self):
        self.__clear()

    def __clear(self):
        UserAssociation.objects.all().delete
        Project.objects.all().delete
        User.objects.all().delete

    def test_make_Story_Statement(self):
        fields = {"title": "title",
                  "description": "desc",
                  "reason": "reason",
                  "test": "test",
                  "status": 1}
        s = models.story.create_story(self.__project, fields)
        statement = models.filemaker.make_Story_Statement(s)
        self.assertEqual(statement, "\ttitle\n\tDescription:desc\n\tImportance:0\n\n")

    def test_make_Iteration_Statement(self):
        title = "title"
        description = "description"
        start_date = datetime.date.today()
        end_date = datetime.date.max
        iteration = models.project_api.add_iteration_to_project(title,
                                                                description,
                                                                start_date,
                                                                end_date, self.__project.id)
        statement = models.filemaker.make_Iteration_Statement(iteration)
        self.assertEqual(statement, "title\nIteration Description:description\n")

    def test_make_Project_Statement(self):
        statement=models.filemaker.make_Project_Statement(self.__project)
        self.assertEqual(statement, "Project:title\n---------------------\nDescription:desc\n\n")

    def test_make_Statement(self):
        statement=models.filemaker.make_Statement(self.__project.id)
        self.assertEqual(statement,"Project:title\n---------------------\nDescription:desc\n\nIceBox:\n")