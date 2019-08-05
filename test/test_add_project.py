from model.project import Project


def test_add_project(app, db, json_project):
    project = json_project
    # old_list = db.get_project_list()
    old_list = app.soap.get_projects()
    app.project.add_new_project(project)
    # new_list = db.get_project_list()
    new_list = app.soap.get_projects()
    assert len(old_list) + 1 == len(new_list)
    old_list.append(project)
    assert sorted(old_list, key=Project.name_key) == sorted(new_list, key=Project.name_key)

