
import sre_parse
from sre_constants import LITERAL, AT, AT_BEGINNING, AT_END

try:
    # Python 3
    from urllib.parse import quote, unquote
    unichr = chr
except ImportError:
    # Python 2
    from urllib import quote, unquote

from django.conf.urls import url
from django.core.urlresolvers import get_urlconf, get_resolver, RegexURLResolver


def robots_decorator(url_function):
    """
    Decorator for django.conf.urls.url
    """
    def url_extended(regex, view, kwargs=None, name=None, robots_allow=None):
        resolver_or_pattern = url_function(regex, view, kwargs=kwargs, name=name)

        resolver_or_pattern.robots_allow = robots_allow
        return resolver_or_pattern

    return url_extended

url = robots_decorator(url)


def create_rules(urlconf=None):
    """
    Creates rules from conf
    """
    if urlconf is None:
        urlconf = get_urlconf()

    root_resolver = get_resolver(urlconf)
    rule_list = create_rule_list(root_resolver, '')

    return u'\n'.join(rule_list)


def create_rule_list(parent_resolver, abs_pattern):
    """
    Creates usable rule list
    """
    rule_list = []

    for resolver in parent_resolver.url_patterns:
        pattern = join_patterns(abs_pattern, resolver.regex.pattern)

        rule = ''
        robots_allow = getattr(resolver, 'robots_allow', None)

        if robots_allow is None:
            pass
        elif robots_allow:
            rule = 'Allow: '
        else:
            rule = 'Disallow: '

        if rule:
            path = clean_pattern(pattern)
            rule += path
            rule_list.append(rule)

        if isinstance(resolver, RegexURLResolver):
            rule_list += create_rule_list(resolver, pattern)

    return rule_list


def join_patterns(pattern1, pattern2):
    """
    Joins URL patterns
    """
    if pattern1.endswith('$'):
        return pattern1

    if pattern2.startswith('^'):
        return pattern1 + pattern2[1:]

    if pattern2:
        return pattern1 + '.' + pattern2

    return pattern1


def clean_pattern(pattern):
    """
    Cleans URL patterns
     * pattern => token
     * '2'     => ('literal', 50)
     * '2|3'   => ('in', [('literal', 50), ('literal', 51)])
    """
    star = '*'
    parsed = sre_parse.parse(pattern)
    literals = []

    for token in parsed:
        if token[0] == LITERAL:
            character = quote(unichr(token[1]).encode('utf8'))
            literals.append(character)
        elif token[0] == AT:
            pass

        elif literals[-1:] != [star]:
            literals.append(star)

    rule = '/' + ''.join(literals)

    if parsed and not rule.endswith(star):
        if parsed[-1] == (AT, AT_END):
            rule += '$'
        else:
            rule += star

    return rule
