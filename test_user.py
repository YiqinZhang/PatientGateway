import sqlite3
import pytest
import Modules.user as user


def test_abort_if_user_id_doesnt_exist():
    with pytest.raises(KeyError):
        conn = sqlite3.connect("../DB/database.db")
        user.abort_if_user_doesnt_exist(conn, '10000')


def test_abort_empty_user_id():
    with pytest.raises(KeyError):
        conn = sqlite3.connect("../DB/database.db")
        user.abort_if_user_doesnt_exist(conn, '')


def test_abort_if_id_exists():
    with pytest.raises(KeyError):
        conn = sqlite3.connect("../DB/database.db")
        user.abort_if_user_exists(conn, 'rose')


def test_get_user_id_doesnt_exist():
    with pytest.raises(KeyError):
        conn = sqlite3.connect("../DB/database.db")
        test_user = user.get_user(conn, '1000')


def test_get_user():
    conn = sqlite3.connect("../DB/database.db")
    test_user = user.get_user(conn, 'rose')
    assert test_user[0][1] == 'rose'


def test_add_user_exists():
    with pytest.raises(Exception):
        conn = sqlite3.connect("../DB/database.db")
        user.add_user(conn, 'jack', '123', '2/22/2000')


@pytest.mark.parametrize('username, password, fn, ln, gender, role, phone, dob, h, w, output',
                         [('evaa','123', 'evaa', 'Z', 'other', 'patient', '123456', '2000-02-22', 170, 55, None),
                          ('jassica', '123', 'jassica', 'Atlantic', '', 'family', '9876543210', '2000-2-22', 160, 42, None),
                          ('adam', '123', 'adam', 'Fu', 'male', '', '9999999999', '1998-11-22', 180, 60, None),
                          ('rose','123', 'rose', 'Atlantic', 'female', 'patient', '1010101010', '1998-11-22', 165, 50, None)])
def test_add_user(username, password, fn, ln, gender, role, phone, dob, h, w, output):
    conn = sqlite3.connect("../DB/database.db")
    last_id = user.add_user(conn, username, password, fn, ln, gender, role, phone, dob, h, w)
    conn.close()
    assert last_id == output


def test_update_user_exists():
    with pytest.raises(Exception):
        conn = sqlite3.connect("../DB/database.db")
        user.add_user(conn, 'eva', '1230000000', 170, 50)


@pytest.mark.parametrize('name, phone, h, w, output',
                         [('jassica', '3333333333', 160, 52, "3333333333"),
                          ('Mark', '1111111111', 180, 70, "1111111111")])
def test_update_user(name, phone, h, w, output):
    conn = sqlite3.connect("../DB/database.db")
    update_user = user.update_user(conn, name, phone, h, w)
    conn.close()
    assert str(update_user[0][7]) == output


@pytest.mark.parametrize('name, output',
                         [('Jassica', 0),
                          ('eva', 0)])
def test_delete_user(name, output):
    conn = sqlite3.connect("../DB/database.db")
    last_id = user.delete_user(conn, name)
    conn.close()
    assert last_id == output
