import tinydb

from torm_storage.Torm import TormStorage

db = tinydb.TinyDB('./tests/dump/test', storage=TormStorage)
c = db.insert({"test": "saja"})
c = db.get(doc_id=1)
print(c)
