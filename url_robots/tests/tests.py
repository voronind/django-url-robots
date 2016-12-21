# coding=utf-8

import unittest

from url_robots.utils import clean_pattern, join_patterns, create_rules


class CleanPatternTestCase(unittest.TestCase):

    def clean_equal(self, pattern, result):
        self.assertEqual(clean_pattern(pattern), '/' + result + '*')

    # special sequences tests
    def test_match_contests_of_group(self):
        self.clean_equal(r'ab(123)c\1d', 'ab*c*d')

    def test_start_n_end_of_string(self):
        self.clean_equal(r'\Aabc', 'abc')
        self.clean_equal(r'\Zabc', 'abc')

    def test_empty_string_at_bound_of_word(self):
        self.clean_equal(r'\babc', 'abc')
        self.clean_equal(r'\Babc', 'abc')

    def test_digits(self):
        self.clean_equal(r'\dabc', '*abc')
        self.clean_equal(r'\Dabc', '*abc')

    def test_spaces(self):
        self.clean_equal(r'\sabc', '*abc')
        self.clean_equal(r'\Sabc', '*abc')

    def test_letters(self):
        self.clean_equal(r'\wabc', '*abc')
        self.clean_equal(r'\Wabc', '*abc')

    def test_backslash(self):
        self.clean_equal(r'\\abc', r'%5Cabc')

    # test special characters
    def test_any_character(self):
        self.clean_equal(r'a.b', 'a*b')

    def test_begin_of_string(self):
        self.clean_equal(r'^ab', 'ab')

    def test_end_of_string(self):
        self.assertEqual(clean_pattern(r'ab$'), u'/ab$')
        self.assertEqual(clean_pattern(r'ab.$'), u'/ab*')

    def test_greedy_repetitions(self):
        self.clean_equal(r'a.*b', 'a*b')
        self.clean_equal(r'a.+b', 'a*b')
        self.clean_equal(r'a.?b', 'a*b')
        self.clean_equal(r'a.{2,3}b', 'a*b')

    def test_non_greedy_repetitions(self):
        self.clean_equal(r'a.*?b', 'a*b')
        self.clean_equal(r'a.+?b', 'a*b')
        self.clean_equal(r'a.??b', 'a*b')
        self.clean_equal(r'a.{2,3}?b', 'a*b')

    def test_set(self):
        self.clean_equal(r'a[123]b', 'a*b')

    def test_or(self):
        self.clean_equal(r'a(2|3)b', 'a*b')

    def test_subpattern(self):
        self.clean_equal(r'a(123)b', 'a*b')

    def test_flags(self):
        self.clean_equal(r'(?sux)ab', 'ab')

    def test_non_grouping(self):
        self.clean_equal(r'a(?:23)b', 'a*b')

    def test_grouping(self):
        self.clean_equal(r'a(?P<name>23)b', 'a*b')

    def test_group_matching(self):
        self.clean_equal(r'a(?P<name>23)b', 'a*b')

        self.clean_equal(r'a(?=23)b', 'a*b')
        self.clean_equal(r'a(?!23)b', 'a*b')

        self.clean_equal(r'a(?<=23)b', 'a*b')
        self.clean_equal(r'a(?<!23)b', 'a*b')

        self.clean_equal(r'(?P<name>)a(?(name)2|3)b', '*a*b')

    def test_comments(self):
        self.clean_equal(r'a(?#comments)b', 'ab')

    def test_urlquote(self):
        # escaped star and dollar
        self.clean_equal(r'star-\*', 'star-%2A')
        self.clean_equal(r'dollar-\$', 'dollar-%24')
        # some russian language
        self.clean_equal(u'path/в никуда/', r'path/%D0%B2%20%D0%BD%D0%B8%D0%BA%D1%83%D0%B4%D0%B0/')


class JoinPatternTestCase(unittest.TestCase):
    def join_equal(self, pattern1, pattern2, pattern1_2):
        self.assertEqual(join_patterns(pattern1, pattern2), pattern1_2)

    # concatenation of ^2, 2$, ^2$, 2, '' tests
    def test_caret_1(self):
        self.join_equal('^1', '^2', '^12')
        self.join_equal('^1', '2$', '^1.2$')
        self.join_equal('^1', '^2$', '^12$')
        self.join_equal('^1', '2', '^1.2')
        self.join_equal('^1', '', '^1')

    def test_1_dollar(self):
        self.join_equal('1$', '^2', '1$')
        self.join_equal('1$', '2$', '1$')
        self.join_equal('1$', '^2$', '1$')
        self.join_equal('1$', '2', '1$')
        self.join_equal('1$', '', '1$')

    def test_caret_1_dollar(self):
        self.join_equal('^1$', '^2', '^1$')
        self.join_equal('^1$', '2$', '^1$')
        self.join_equal('^1$', '^2$', '^1$')
        self.join_equal('^1$', '2', '^1$')
        self.join_equal('^1$', '', '^1$')

    def test_1(self):
        self.join_equal('1', '^2', '12')
        self.join_equal('1', '2$', '1.2$')
        self.join_equal('1', '^2$', '12$')
        self.join_equal('1', '2', '1.2')
        self.join_equal('1', '', '1')


class CreateRulesTestCase(unittest.TestCase):
    def setUp(self):
        self.expected_rules = '''Allow: /profiles$
Disallow: /profile/*/private*
Allow: /profile/*/public*'''

    def test_create_rules_for_profiles(self):
        rules = create_rules('url_robots.tests.urls')
        self.assertEqual(rules, self.expected_rules)

