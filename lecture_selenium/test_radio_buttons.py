from lecture_selenium.pages.page_radio_button import PageRadioButton


class TestRadioButtons:
    dct = {
        'Yes': {
            'is_selected': False,
            'is_enabled': True},
        'Impressive': {
            'is_selected': False,
            'is_enabled': True},
    }

    def test_yes_radio(self, chrome):
        page = PageRadioButton(driver=chrome)
        page.open()
        page.select_yes_button()
        self.dct['Yes']['is_selected'] = page.is_yes_button_selected()
        assert self.dct.get('Yes').get('is_selected') is True
