import os
from mastodon import Mastodon
from .check_env import get_env_string


def get_client():
    mastodon = Mastodon(
        client_id=get_env_string('MASTODON_CLIENT_ID'),
        client_secret=get_env_string('MASTODON_CLIENT_SECRET'),
        api_base_url=get_env_string('MASTODON_HOST')
    )
    mastodon.log_in(get_env_string('MASTODON_USER'), get_env_string('MASTODON_PASSWORD'), scopes=['read', 'write'])
    return mastodon


def send_toot(content: str):
    try:
        toot = get_client().toot(content)
    except Exception as e:
        return f"Error: toot was not sent, {e}"
    return f"toot was successfully sent, the url to the toot is: {toot.url}"


def reply_to_toot(content: str, toot_id: int):
    try:
        client = get_client()
        original_toot = client.status(toot_id)
        toot = client.status_reply(original_toot, content)
    except Exception as e:
        return f"Error: the reply was not sent, {e}"
    return f"the reply was successfully sent, the url to the toot is: {toot.url}"


def check_mastodon_notifications():
    try:
        client = get_client()
        notifications = client.notifications()
        result = parse_notifications(notifications)
        client.notifications_clear()

    except Exception as e:
        print(f"{e}{type(e)=}")
        return f"Error: could not check notifications:\n{e}\n"

    return result


def parse_notifications(notifications):
    parsed = []

    for notification in notifications:
        if 'status' in notification:
            target = f"the toot with the id {notification['status']['id']}, the url {notification['status']['url']} " \
                     f"and the content:\n" \
                     f"{notification['status']['content']}"
        else:
            target = "us"
        item = f"Notification {notification['id']}:\n" \
               f"The sender is {notification['account']['display_name']} with the Mastodon user id {notification['account']['acct']} " \
               f"has {notification['type']} " \
               f"{target} "

        parsed.append(item)
    return parsed


def boost_toot(toot_id: int):
    try:
        client = get_client()
        original_toot = client.status(toot_id)
        toot = client.status_reblog(original_toot)
    except Exception as e:
        return f"Error: the boost was not sent, {e}"
    return f"the boost was successfully posted, the url to the new toot is: {toot.url}"


def favorite_toot(toot_id: int):
    try:
        toot = get_client().status_favourite(toot_id)
    except Exception as e:
        return f"Error: the toot was not made a favorite: {e}"
    return f"the the toot was successfully made a favorite: {toot.url}"