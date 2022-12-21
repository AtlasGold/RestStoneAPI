from tinydb import TinyDB
from tinydb.storages import MemoryStorage

database = TinyDB(storage=MemoryStorage)
