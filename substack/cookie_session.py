# substack/cookie_session.py
import json, os, requests
from requests.utils import cookiejar_from_dict

class CookieSession(requests.Session):
    """
    A requests.Session that loads cookies from Chrome/Firefox export
    (JSON list of {name,value,domain,path,...}).  If a CSRF token is
    present it is copied to the required headers so every POST works.
    """
    def __init__(self, cookie_file: str | os.PathLike, verify_ssl: bool = True):
        super().__init__()
        with open(cookie_file, "r", encoding="utf-8") as f:
            raw = json.load(f)
        self.cookies = cookiejar_from_dict({c["name"]: c["value"] for c in raw})
        self.verify = verify_ssl
