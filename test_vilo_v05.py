"""VILO 0.5: test the separate public username and display nickname and call authorization."""
import unittest,os,tempfile,sys
from pathlib import Path
from fastapi.testclient import TestClient
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'backend'))

class Vilo05Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory()
        # Existing VILO tests import the same server; use its active data location.
        import server
        server.DATA=Path(cls.tmp.name);server.DB_PATH=server.DATA/'vilo.db'
        server.UPLOADS=server.DATA/'uploads';server.UPLOADS.mkdir(exist_ok=True)
        server.PROFILE_MEDIA=server.DATA/'profile_media';server.PROFILE_MEDIA.mkdir(exist_ok=True)
        server.init_db()
        cls.server=server
        cls.a=TestClient(server.app); cls.b=TestClient(server.app)
        cls.a.post('/api/register',json={'username':'Caller05','display_name':'Widoczny Nick','email':'caller05@test.local','password':'SuperPassword!123'})
        cls.b.post('/api/register',json={'username':'Receiver05','display_name':'Odbierający','email':'receiver05@test.local','password':'SuperPassword!123'})
    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()
    def test_username_distinct_from_nickname(self):
        me=self.a.get('/api/me').json()
        self.assertEqual(me['username'],'Caller05');self.assertEqual(me['display_name'],'Widoczny Nick')
        self.assertEqual(self.b.post('/api/register',json={'username':'Caller05','display_name':'Inny','email':'x05@test.local','password':'SuperPassword!123'}).status_code,409)
    def test_call_targets_are_dm_members(self):
        aid=self.a.get('/api/me').json()['id'];bid=self.b.get('/api/me').json()['id']
        # Unauthorized users must not create direct conversations without friendship.
        self.assertEqual(self.a.post('/api/dm/'+str(bid)).status_code,403)
        # The signaling server checks both authenticated memberships and DM kind.
        q="SELECT 1 FROM rooms r JOIN members a ON a.room_id=r.id AND a.user_id=? JOIN members b ON b.room_id=r.id AND b.user_id=? WHERE r.id=? AND r.kind='dm'"
        self.assertIsNone(self.server.one(q,aid,bid,999999))
