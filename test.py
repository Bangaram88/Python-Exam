import json


mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
    }
def test_create_success(app, client):

    data = {
        "audioFileType":"song",
        "audioFileMetadata":{
            "name":"Fake Love",
            "duration":240
        }
    }


    response = client.post('/', data=json.dumps(data), headers=headers)
    assert response.status_code == 200



def test_create_failure_400(app, client):
    """duration missing in the data/payload"""

    data = {
        "audioFileType":"song",
        "audioFileMetadata":{
            "name":"Fake Love"
        }
    }

    response = client.post('/', data=json.dumps(data), headers=headers)
    assert response.status_code == 400



def test_create_failure_500(app, client):
    """adding new field (Rating) to payload gives 500"""

    data = {
        "audioFileType":"song",
        "audioFileMetadata":{
            "name":"Fake Love",
            "Rating": 4.7
        }
    }

    response = client.post('/', data=json.dumps(data), headers=headers)
    assert response.status_code == 500



def test_get_one_success(app, client):
    audioFileType = 'song'
    audioFileID = "6043b4f86910bbcc3fb43e09"
    response = client.get('/media/{}/{}'.format(audioFileType, audioFileID))
    assert response.content_type == mimetype
    assert response.status_code == 200



def test_get_one_failure(app, client):
    """wrong audioFileType gives 500"""

    audioFileID = "604330705ac133f1fb5159"
    response = client.get('/media/{}/{}'.format('invalid_type', audioFileID))
    assert response.status_code == 500



def test_get_all_success(app, client):
    audioFileType = 'song'
    response = client.get('/media/{}/'.format(audioFileType))
    assert response.content_type == mimetype
    assert response.status_code == 200



def test_put_success(app, client):
    data = {
        "audioFileType":"song",
        "audioFileMetadata":{
            "name":"BTS",
            "duration":248
        }
    }

    audioFileMetadata = data['audioFileMetadata']
    audioFileType = data['audioFileType']


    audioFileID = "6043b4f86910bbcc3fb43e09"

    response = client.put('/media/{}/{}'.format(audioFileType, audioFileID), data = json.dumps(data), headers=headers)
    assert response.content_type == mimetype
    assert response.status_code == 200



def test_put_failure_400(app, client):
    """invalid audioFileID gives 400"""
    data = {
        "audioFileType":"song",
        "audioFileMetadata":{
            "name":"Bad File"
        }
    }

    audioFileMetadata = data['audioFileMetadata']
    audioFileType = data['audioFileType']


    audioFileID = "604330705c133f1fb5159"

    response = client.put('/media/{}/{}'.format(audioFileType, audioFileID), data = json.dumps(data), headers=headers)
    assert response.status_code == 400


def test_delete_success(app, client):
    audioFileType = 'song'
    audioFileID = "6043b4f86910bbcc3fb43e09"

    response = client.delete('/media/{}/{}'.format(audioFileType, audioFileID))
    assert response.content_type == mimetype
    assert response.status_code == 200



def test_delete_failure(app, client):
    """invalid audioFileID gives 400"""
    audioFileType = 'song'
    audioFileID = "6043b809d97d9ceab834"

    response = client.delete('/media/{}/{}'.format(audioFileType, audioFileID))
    assert response.content_type == mimetype
    assert response.status_code == 400