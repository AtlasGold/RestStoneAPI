from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

database = TinyDB(storage=MemoryStorage)