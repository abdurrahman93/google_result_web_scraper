from bs4 import BeautifulSoup


class DocumentScraper:

    def __init__(self, html_source):
        self.bs = BeautifulSoup(html_source, "html.parser")

    def get_g_divs(self):
        return self.bs.find_all('div', {'class': 'g'})

    def get_url_and_text_list(self):
        url_text_list = list()
        for g_div in self.get_g_divs():
            anchor_tag = g_div.find('a')
            if anchor_tag:
                href = anchor_tag.get('href', '')
                ellip_tag = anchor_tag.find('div', {'class': 'ellip'})
                text = ellip_tag.text if ellip_tag else ''
                url_text_list.append({'text': text, 'url': href})
        return url_text_list
