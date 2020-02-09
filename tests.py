import unittest
from unittest import TestCase

from requests.exceptions import HTTPError

from chuck_norris_facts import (
    get_random_fact,
    get_available_categories,
    search_facts,
)

class TestGetRandomFact(TestCase):

    def test_no_category(self):
        result = get_random_fact()
        self.assertTrue(isinstance(result, dict))

    def test_category(self):
        result = get_random_fact(category='movie')
        self.assertTrue(isinstance(result, dict))

    def test_invalid_category(self):
        with self.assertRaises(HTTPError):
            get_random_fact(category='random category')

class TestGetAvailableCategories(TestCase):

    def test_available_category(self):
        result = get_available_categories()
        self.assertTrue(isinstance(result, list))

class TestSearchFacts(TestCase):

    def test_small_query(self):
        result = search_facts(query='war')
        self.assertTrue(result, dict)

    def test_random_query(self):
        result = search_facts(query='uhasuhdhasdhuasuhd')
        self.assertTrue(result, dict)

    def test_no_query(self):
        with self.assertRaises(HTTPError):
            search_facts(query='')

if __name__ == '__main__':
    unittest.main()
