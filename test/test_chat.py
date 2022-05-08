import sqlite3

import pytest
import sys

sys.path.append("..")
from Modules import chat

db_dir = '../DB/database.db'


def test_send_chat_invalid_receiver():
    with pytest.raises(KeyError):
        conn = chat.create_connection(db_dir)
        chat.send_chat(conn, 'admin', '1000', 'message', "invalid receiver")
        conn.close()


def test_send_chat_invalid_sender():
    with pytest.raises(KeyError):
        conn = chat.create_connection(db_dir)
        chat.send_chat(conn, '1000', 'admin', 'message', "invalid sender")
        conn.close()


def test_send_empty_chat():
    conn = chat.create_connection(db_dir)
    res = chat.send_chat(conn, 'rose', 'jack', 'message', '')
    conn.close()
    assert res is None


@pytest.mark.parametrize('sender, to, message_type, content, output',
                         [('rose', 'jack', 'message', '', None),
                          # ('rose', 'jack', 'message', '', "('rose', 'jack', 'message', '')",
                          ('rose', 'jack', 'message', 'hello', 6)])
def test_send_chat(sender, to, message_type, content, output):
    conn = chat.create_connection(db_dir)
    res = chat.send_chat(conn, 'rose', 'jack', 'message', 'hello')
    conn.close()
    assert res is not None


def test_chat_history():
    with pytest.raises(KeyError):
        conn = sqlite3.connect("../DB/database.db")
        chat.get_chat_history(conn, '1000')
        conn.close()


def test_one_chat_history():
    with pytest.raises(KeyError):
        conn = chat.create_connection(db_dir)
        chat.get_one_chat(conn, 'rose', 'admin')
        conn.close()


def test_get_one_chat():
    conn = chat.create_connection(db_dir)
    res = chat.get_one_chat(conn, 'rose', 'jack')
    assert res != None
    conn.close()


def test_delete_chat():
    conn = chat.create_connection(db_dir)
    last_id = chat.delete_chat(conn, '6')
    conn.close()
    assert last_id == 0
