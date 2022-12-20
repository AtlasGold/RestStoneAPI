from tinydb import TinyDB
from tinydb.storages import MemoryStorage

database = TinyDB("/api/schema/database.json")
