#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import markdown
import lxml.html
import lxml.html.clean
from docutils.core import publish_parts

encoding_match = re.compile('encoding=[^>]+')

cleaner = lxml.html.clean.Cleaner(
    scripts=True,
    javascript=True,
    comments=True,
    style=True,
    links=True,
    meta=True,
    page_structure=True,
    processing_instructions=True,
    embedded=True,
    frames=True,
    forms=True,
    annoying_tags=True,
    remove_tags=None,
    allow_tags=None,
    kill_tags=None,
    remove_unknown_tags=True,
    safe_attrs_only=True,
    safe_attrs=frozenset(['abbr', 'accept', 'accept-charset']),
    add_nofollow=False,
    host_whitelist=(),
    whitelist_tags=set(['embed', 'iframe']),
    _tag_link_attrs={'a': 'href', 'applet': ['code', 'object']})


def clean_note(content):
    cleaned = cleaner.clean_html(content)
    raw_text = lxml.html.fromstring(cleaned).text_content()
    return raw_text


def make_mdnote(md_source):
    source_segment = '''<div id="md_source" style="display:none">%s</div>''' \
                     % md_source
    html = markdown.markdown(md_source)
    return '%s\n%s' % (html, source_segment)


def make_rstnote(rst_source):
    source_segment = '''<div id="rst_source" style="display:none">%s</div>''' \
                     % rst_source
    html = publish_parts(rst_source, writer_name='html')['html_body']
    return '%s\n%s' % (html, source_segment)


if __name__ == '__main__':
    md_source = '''
#markdown note
## hello, markdown
### mark language
- markdown
- restructedText
- asciidoc
'''
    print make_mdnote(md_source)
    rst_source = '''
rst note
========

hello, rst
----------

mark language
~~~~~~~~~~~~~

- markdown
- restructedText
- asciidoc
'''
    print make_rstnote(rst_source)