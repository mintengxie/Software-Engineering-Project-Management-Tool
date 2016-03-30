from django.db import models
from django.contrib.auth.models import User
from story import Story
from base import ProjMgmtBase
from iteration import Iteration
from user_association import UserAssociation
from django.http import HttpResponse

from requirements.models import project_api
from project import Project


def make_Statement(ProjectID):
    try:
        statement = ""

        project = project_api.get_project(ProjectID)
        statement += make_Project_Statement(project)

        iterations = project_api.get_iterations_for_project(project)

        iceboxStories = project_api.get_stories_with_no_iteration(project)
        statement+="IceBox:\n"

        for iceboxStory in iceboxStories:
            statement += make_Story_Statement(iceboxStory)
        for iteration in iterations:
            statement += make_Iteration_Statement(iteration)
            stories = project_api.get_stories_for_iteration(iteration)
            for story in stories:
                statement += make_Story_Statement(story)
        return statement

    except Exception as e:
        return "None1"


#def fetch_Project(ProjectID):
#    try:
#        return project_api.get_project(ProjectID)
#    except Exception as e:
#        return "None2"

def make_Project_Statement(Project):
    try:
        return "Project:"+Project.title+"\n"+"---------------------"+"\n"+"Description:"+Project.description+"\n"+"\n"
    except Exception as e:
        return "None3"

def make_Iteration_Statement(iteration):
    try:
        return iteration.title+"\nIteration Description:"+iteration.description+"\n"
    except Exception as e:
        return "None4"

def make_Story_Statement(story):
    try:
        return "\t"+story.title+"\n\tDescription:"+story.description+"\n\tImportance:"+str(story.points)+"\n\n"
    except Exception as e:
        return "None5"