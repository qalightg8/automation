def test_move_between_tabs_1(chrome):
    url1 = 'https://demoqa.com/books'
    url2 = 'https://demoqa.com/text-box'

    chrome.get(url1)
    url1_window = chrome.current_window_handle

    chrome.execute_script("window.open('', '_blank');")
    handles = chrome.window_handles
    chrome.switch_to.window(handles[0])
    chrome.get(url2)

    pass
