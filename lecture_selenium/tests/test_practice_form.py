from lecture_selenium.pages.page_practice_form import PagePracticeForm


class TestPracticeForm:

    def test_select_state(self, chrome):
        state_name = 'Rajasthan'
        page = PagePracticeForm(driver=chrome)
        page.open()
        page.select_state(state_name)
        pass
