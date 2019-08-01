
class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def fill_project_form(self, project):
        self.fill_form_value("name", project.name)
        self.fill_form_value("description", project.description)

    def fill_form_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def add_new_project(self, project):
        wd = self.app.wd
        self.app.open_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.app.open_project_page()

    def delete(self, id):
        wd = self.app.wd
        self.app.open_project_page()
        wd.find_element_by_xpath("//a[contains(@href,'manage_proj_edit_page.php?project_id=%s')]" % id).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.app.open_project_page()


