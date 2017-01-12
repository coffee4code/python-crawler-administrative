from urllib.parse import urlencode
from hashlib import md5
import requests
import os
import config


class JSONReader:
    def __init__(self):
        self.cache_dir = config.cache_dir
        self.cache_suffix = config.cache_suffix

    def read(self, city_name, subdistrict):
        cached = self._get_cache(city_name)
        if cached:
            return cached
        data = self._load(city_name, subdistrict)
        self._set_cache(city_name, data)
        return data

    @staticmethod
    def _load(city_name, subdistrict):
        param = {
            "subdistrict": subdistrict,
            "key": config.url_key,
            "s": config.url_s,
            "output": config.url_output,
            "keywords": city_name

        }
        query_string = urlencode(param)
        url = config.url_base + '?' + query_string
        data = requests.get(url)
        return data.content.decode(config.cache_encode)

    def _set_cache(self, city_name, value):
        cache_path = self._get_cache_file(city_name)
        file_output = open(cache_path, 'w', newline="\r\n")
        file_output.write(value)
        file_output.close()

    def _get_cache(self, city_name):
        cache_path = self._get_cache_file(city_name)

        if os.path.isfile(cache_path):
            try:
                file_input = open(cache_path, "r")
                data = file_input.read()
            finally:
                file_input.close()
            if data:
                return data
        return False

    def _get_cache_file(self, city_name):
        m = md5(city_name.encode(config.cache_encode))
        cache_name = m.hexdigest()
        cache_key = cache_name + self.cache_suffix
        cache_path = os.path.join(self.cache_dir, cache_key)
        return cache_path
