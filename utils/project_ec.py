def text_is_not_empty_in_element(locator):
    def _predicate(driver):
        element = driver.find_element(*locator)
        return len(element.text) > 0

    return _predicate
