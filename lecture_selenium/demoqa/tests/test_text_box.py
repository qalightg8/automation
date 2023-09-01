from lecture_selenium.pages.page_text_box import PageTextBox


def test_text_box_set_fullname(chrome):
    page = PageTextBox(driver=chrome)
    page.open()
    page.set_full_name(fullname='Artem Svarych')
    page.set_email('pupkin@mail.com')
    page.set_current_address('My current address')
    page.set_permanent_address('My permanent address')
    # page.submit()
    page.click_button_by_name('Submit')


def test_text_1(chrome):
    expected_result = 'pupkin@mail.com'
    page = PageTextBox(driver=chrome)
    page.open()
    page.set_email('pupkin@mail.com')
    page.submit()
    result_email = page.get_result_email()
    assert result_email == expected_result
