pytest_plugins = [
   "fixtures.engine",
]

def pytest_addoption(parser):
   parser.addoption("--username", action="store", default="xyz", help="Use this flag to pass the username used to login.")
   parser.addoption("--password", action="store", default="xyz", help="Use this flag to pass the password used to login.")
   parser.addoption("--record_video", action="store", default="yes", help="Use this flag to record the video if yes it will else it wont.")
