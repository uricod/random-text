from randomText.src.base_meta import Meta
import pandas as pd


class RandomObject8(Meta):
    def __init__(self):
        super().__init__()

    def get_paragraphs(self, size=1):
        """
        Get a random amount of paragraphs
        :return: df of text
        """
        method = 'GET'
        url = f'paragraphs/{str(size)}'
        parameters = {}
        body = None
        return self.make_request(url, method, parameters, body)

    def get_sentences(self, size=1):
        """
        Get a random amount of sentences
        :return: df of text
        """
        method = 'GET'
        url = f'sentences/{str(size)}'
        parameters = {}
        body = None
        return self.make_request(url, method, parameters, body)

    def get_doc(self, paragraph_size=1, sentence_size=1):
        """
        Get a random amount of sentences
        :return: df of text
        """
        method = 'GET'
        url = f'paragraphs/{str(paragraph_size)}/{str(sentence_size)}'
        parameters = {}
        body = None
        return self.make_request(url, method, parameters, body)

