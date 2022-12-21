from tinydb import TinyDB, where, Query
from tinydb.storages import MemoryStorage


def test_storage_access():

    """
    Testing the initial database connection
    """

    db = TinyDB(storage=MemoryStorage)

    assert isinstance(db.storage, MemoryStorage)


def test_drop_tables():
    """
    Drop an empty table right after it's created
    Drop an empty table right after it's created
    """
    db = TinyDB(storage=MemoryStorage)
    db = TinyDB(storage=MemoryStorage)
    db.drop_tables()

    db.insert({})
    db.drop_tables()

    assert len(db) == 0


def test_creating_new_tables():
    """
    Creating new ten tables on
    empty database
    Creating new ten tables on
    empty database
    """
    db = TinyDB(storage=MemoryStorage)
    db = TinyDB(storage=MemoryStorage)

    db.drop_tables()

    for i in range(10):
        db.insert({})

    assert len(db.all()) == 10


def test_insert():
    """
    Test to enter numeric and text ID values
    Test to enter numeric and text ID values
    to see if all are actually entered
    """
    db = TinyDB(storage=MemoryStorage)
    db = TinyDB(storage=MemoryStorage)

    db.drop_tables()

    db.insert({"int": 1, "char": "a"})
    db.insert({"int": 1, "char": "b"})
    db.insert({"int": 1, "char": "c"})
    db.insert({"num": 1, "letter": "a"})
    db.insert({"num": 1, "letter": "b"})
    db.insert({"num": 1, "letter": "c"})

    assert db.count(where("int") == 1) == 3
    assert db.count(where("char") == "a") == 1
    assert db.count(where("num") == 1) == 3
    assert db.count(where("letter") == "a") == 1


def test_insert_on_existing_db(tmpdir):

    """
    Test the insertion of new data in a
    previously registered database
    """
    path = str(tmpdir.join("db.json"))

    db = TinyDB(path, ensure_ascii=False)
    db.insert({"key": "value"})

    assert len(db) == 1

    db.close()

    db = TinyDB(path, ensure_ascii=False)
    db.insert({"key": "value"})
    db.insert({"key": "value"})

    assert len(db) == 3


def test_query():

    """
    Test a value-checking query
    to identify logical operators
    AND verifies that the values are not
    changed at the end of the query
    """

    db = TinyDB(storage=MemoryStorage)
    db.insert_multiple(
        [
            {"name": "Python Da Silva", "value": 13},
            {"name": "João Flask", "value": -9000},
        ]
    )

    query = where("value") > 0

    results = db.search(query)
    assert len(results) == 1

    db._tables[db.table(db.default_table_name).name]._read_table = lambda: {}

    results.extend([1])
    assert db.search(query) == [{"name": "Python Da Silva", "value": 13}]


def test_delete_specific_value(tmpdir):

    """
    Creates a temporary directory to store insertion values
    in a json to test file deletion and checks if the specific
    deleted file is no longer found
    """

    path = str(tmpdir.join("db.json"))

    db = TinyDB(path, ensure_ascii=False)
    q = Query()
    db.insert({"network": {"id": "97", "name": "Luan", "API": "rest", "Game": "Souls"}})
    assert db.search(q.network.id == "97") == [
        {"network": {"id": "97", "name": "Luan", "API": "rest", "Game": "Souls"}}
    ]
    db.remove(q.network.id == "97")
    assert db.search(q.network.id == "97") == []


def test_empty_db_length():

    """
    Create a new, clean database to test that
    it starts up with no previous values
    """

    db = TinyDB(storage=MemoryStorage)
    assert len(db) == 0
