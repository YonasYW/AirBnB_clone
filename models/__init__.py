#!/usr/bin/python3
"""Init make python package and those comannd automatically reload json."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
