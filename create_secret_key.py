import os

print(os.urandom(12))

from uuid import uuid4

print(uuid4().hex)

import secrets

print(secrets.token_urlsafe(12))
