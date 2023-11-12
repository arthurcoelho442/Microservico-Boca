from app import api

from os import environ

if __name__ == '__main__':
    api.run(host='0.0.0.0',port=8080, debug=(not environ.get('ENV') == 'PRODUCTION'), threaded=False)