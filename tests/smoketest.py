import tinydb

from torm_storage.Torm import TormStorage

db = tinydb.TinyDB('test', storage=TormStorage)
# c = db.insert({"test": "saja"})
# print(c)
# db.truncate()
c = db.get(doc_id=1)
print(c)

# print(c)
# db.c
# print(c)
