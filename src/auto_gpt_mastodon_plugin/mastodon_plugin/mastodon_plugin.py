import os
from mastodon import Mastodon
from .check_env import get_env_string


def send_toot(content: str):
    try:
        mastodon = Mastodon(
            client_id=get_env_string('MASTODON_CLIENT_ID'),
            client_secret=get_env_string('MASTODON_CLIENT_SECRET'),
            api_base_url=get_env_string('MASTODON_HOST')
        )
        mastodon.log_in(get_env_string('MASTODON_USER'), get_env_string('MASTODON_PASSWORD'), scopes=['read', 'write'])
        toot = mastodon.toot(content)
    except Exception as e:
        return f"Error: toot was not sent, {e}"
    return f"toot was successfully sent, the url to the toot is: {toot.url}"
