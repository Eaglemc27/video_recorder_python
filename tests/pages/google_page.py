from selene.tools import s, ss, visit


class GooglePage(object):

    def open(self):
        visit("http://google.com/ncr")
        return self

    def search(self, text):
        s("[name='q']").set(text).press_enter()
        return SearchResultsPage()


class SearchResultsPage(object):

    def __init__(self):
        self.results = ss("#ires span.st")