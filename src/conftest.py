from .server import create_server as cs
import pytest
from threading import Thread


@pytest.fixture(scope='module', autouse=True)
def server_setup():
    svr = cs()

    proc = Thread(target=svr.serve_forever)
    proc.setDaemon(True)

    proc.start()
