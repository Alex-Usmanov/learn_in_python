__author__ = 'Nicole'
# -*- coding: utf-8 -*-
"""
    mini_blog Tests
    ~~~~~~~~~~~~

    Tests the mini_blog application.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import pytest

import os
import mini_blog
import tempfile


@pytest.fixture
def client(request):
    db_fd, mini_blog.app.config['DATABASE'] = tempfile.mkstemp()
    mini_blog.app.config['TESTING'] = True
    client = mini_blog.app.test_client()
    with mini_blog.app.app_context():
        mini_blog.init_db()

    def teardown():
        os.close(db_fd)
        os.unlink(mini_blog.app.config['DATABASE'])

    request.addfinalizer(teardown)

    return client


def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)


def test_empty_db(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert b'No entries here so far' in rv.data


def test_login_logout(client):
    """Make sure login and logout works"""
    rv = login(client, mini_blog.app.config['USERNAME'],
               mini_blog.app.config['PASSWORD'])
    assert b'You were logged in' in rv.data
    rv = logout(client)
    assert b'You were logged out' in rv.data
    rv = login(client, mini_blog.app.config['USERNAME'] + 'x',
               mini_blog.app.config['PASSWORD'])
    assert b'Invalid username' in rv.data
    rv = login(client, mini_blog.app.config['USERNAME'],
               mini_blog.app.config['PASSWORD'] + 'x')
    assert b'Invalid password' in rv.data


def test_messages(client):
    """Test that messages work"""
    login(client, mini_blog.app.config['USERNAME'],
          mini_blog.app.config['PASSWORD'])
    rv = client.post('/add', data=dict(
        title='<Hello>',
        text='<strong>HTML</strong> allowed here'
    ), follow_redirects=True)
    assert b'No entries here so far' not in rv.data
    assert b'&lt;Hello&gt;' in rv.data
    assert b'<strong>HTML</strong> allowed here' in rv.data