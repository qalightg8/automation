import pytest

from lecture_selenium.pages.page_checkbox import PageCheckbox


class TestCheckbox:

    def test_1(self, chrome):
        directories = ['Home', 'Documents', 'WorkSpace']
        target = 'React'
        page = PageCheckbox(chrome)
        page.open()
        page.expand_nodes_from_list(directories)
        page.check_folder(target)
        pass

    def test_2(self, chrome):
        page = PageCheckbox(chrome)
        page.open()
        page.check_folder('Home')
        pass
