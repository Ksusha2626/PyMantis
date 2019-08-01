from model.project import Project
import random


def test_delete_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.fill_project_form(Project(name='New', description='Try'))
    old_list = db.get_project_list()
    project = random.choice(old_list)
    app.project.delete(project.id)
    new_list = db.get_project_list()
    assert len(old_list) - 1 == len(new_list)
    old_list.remove(project)
    assert sorted(old_list, key=Project.name_key) == sorted(new_list, key=Project.name_key)
