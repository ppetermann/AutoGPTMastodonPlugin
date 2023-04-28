import os


def get_env_string(env_key: str):
    information = os.getenv(env_key)
    if not information:
        raise Exception(f"Error: toot not sent, {env_key} is not set in the environment (.env)")
    return information


def check_env():
    try:
        get_env_string("MASTODON_CLIENT_ID")
        get_env_string("MASTODON_CLIENT_SECRET")
        get_env_string("MASTODON_HOST")
        get_env_string("MASTODON_PASSWORD")
        get_env_string("MASTODON_USER")
    except Exception as e:
        print(e)
        return False
    return True
