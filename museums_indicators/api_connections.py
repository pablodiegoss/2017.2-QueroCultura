import json
import requests
from quero_cultura.views import ParserYAML


class RequestMuseumRawData(object):

    def __init__(self, last_update_time, url):
        self._filters = {'@select': 'mus_tipo, mus_tipo_tematica, esfera, '
                                   + 'mus_servicos_visitaGuiada, '
                                   + 'mus_arquivo_acessoPublico, '
                                   + 'createTimestamp',
                        'createTimestamp': "GT("+last_update_time+")"}
        self._response = requests.get(url, self._filters)
        self._data = json.loads(self._response.text)

    @property
    def response(self):
        return self._response

    @property
    def data(self):
        return self._data

    @property
    def data_length(self):
        return len(self._data)
