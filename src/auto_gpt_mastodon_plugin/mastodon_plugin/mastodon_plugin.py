import os
from mastodon import Mastodon


def getClientId():
    return getEnvString("MASTODON_CLIENT_ID")


def getClientSecret():
    return getEnvString("MASTODON_CLIENT_SECRET")


def getEnvString(env_key: str):
    information = os.getenv(env_key)
    if not information:
        return f"Error: toot not sent, {env_key} is not set in the environment (.env)"
    return information


def getMastodonHost():
    return getEnvString("MASTODON_HOST")


def getPwd():
    return getEnvString("MASTODON_PASSWORD")


def getUser():
    return getEnvString("MASTODON_USER")


def send_toot(content: str):
    mastodon = Mastodon(client_id=getClientId(), client_secret=getClientSecret(), api_base_url=getMastodonHost())
    mastodon.log_in(getUser(), getPwd(), scopes=['read', 'write'])
    mastodon.toot(content)
    return f"successfully tooted {content}!"