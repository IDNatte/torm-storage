import pytest
import tinydb

from torm_storage.Torm import TormStorage


@pytest.fixture
def mock_db():
    db = tinydb.TinyDB('test.ndb', storage=TormStorage)
    yield db
    db.close()

class Test_rw:
    def test_write(self, mock_db):
        c = mock_db.insert({'test': 'saja'})
        assert mock_db.get(doc_id=c)

    def test_read(self, mock_db):
        c = mock_db.all()
        assert c != []
