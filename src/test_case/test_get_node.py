import requests
import pytest
import allure
from src.test_get_data import get_excel_data

class Test_get_node(object):
    #domain = 'https://www.v2ex.com/'
    #@pytest.fixture()
    def count(self):
        print('init test')
        return 10

    @allure.feature('Feature1')
    @allure.story('Story1')
    def test_node(self):
        #path = 'api/nodes/show.json?name=python'
        #url = self.domain + path
        url = get_excel_data.read_requestdata("test_get_node")
        if url!="":
            res = requests.get(url).json()
            assert res['id'] == 90
            assert res['name'] == 'python'
            print(res['name'])
        else:
            print("couldn't find test data")

#ts=Test_get_node()
#ts.test_node()
