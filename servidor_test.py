import servidor
def test_index():
servidor.app.testing = True
client = servidor.app.test_client()
r = client.get('/')
assert r.status_code == 200
assert 'Hello World!' in r.data.decode('utf-8')
