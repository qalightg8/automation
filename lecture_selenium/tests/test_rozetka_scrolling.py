from lecture_selenium.pages.page_rozetka_notebooks import PageRozetkaNotebooks


class TestRozetkaScrolling:

    def test_goods_count(self, chrome):
        expected_goods_cnt = 60
        page = PageRozetkaNotebooks(chrome)
        page.open()
        assert page.get_goods_count() == expected_goods_cnt

    def test_scroll_to_paginator(self, chrome):
        page = PageRozetkaNotebooks(chrome)
        page.open()
        assert page.is_scroll_to_paginator_works()

    def test_goods_names(self, chrome):
        page = PageRozetkaNotebooks(chrome)
        page.open()
        texts = page.get_goods_names()

        assert len(texts) == 60
