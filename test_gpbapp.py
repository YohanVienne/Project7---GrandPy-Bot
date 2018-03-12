import os.path
"""
Pytest file
"""
#Check if the app folder exist
def testFlaskFolderCreate():
    assert os.path.exists('gpbapp')

def testIf__init__exist():
    assert os.path.exists('gpbapp/__init__.py')

def testIfViewsExist():
    assert os.path.exists('gpbapp/views.py')