from page_objects import PageObject, PageElement
import time


class GooglePage(PageObject):
    uri = 'https://www.google.com/search?q='

    def make_search_query(self, query_param):
        self.get(self.uri + query_param)
        # TODO replace this with Wait.Untill selenium feature.
        time.sleep(3)
    
    def get_page_source(self):
        return self.w.page_source