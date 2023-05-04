# AutoGPTMastodonPlugin

Simple Mastodon plugin for Auto-GPT. At this time it only supports posting to Mastodon, no reading. You will have to 
manually register the account, as well as the app.

USE AT YOUR OWN RISK

### Plugin Installation Steps

1. **Clone or download the plugin repository:**
   Clone the plugin repository, or download the repository as a zip file.

2. **Install the plugin's dependencies (if any):**
   Note: If you run auto-gpt in docker, you will have to rebuild the container with the plugins requirements (Mastodon.py) added to the requirements.txt file.  (or run a custom more complex setup)

   Navigate to the plugin's folder in your terminal, and run the following command to install any required dependencies:

   ``` shell
      pip install -r requirements.txt
   ```

3. **Package the plugin as a Zip file:**
   If you cloned the repository, compress the plugin folder as a Zip file.

4. **Copy the plugin's Zip file:**
   Place the plugin's Zip file in the `plugins` folder of the Auto-GPT repository.

5. **Allowlist the plugin (optional):**
   Add the plugin's class name to the `ALLOWLISTED_PLUGINS` in the `.env` file to avoid being prompted with a warning when loading the plugin: (remove ,OtherPlugin from example ;)

   ``` shell
   ALLOWLISTED_PLUGINS=AutoGPTMastodonPlugin,OtherPlugin
   ```
   If the plugin is not allowlisted, you will be warned before it's loaded.

6. **More Config**
   you will have to add the credentials for the mastodon account to your .env file:
```
MASTODON_USER=mail@example.com
MASTODON_PASSWORD=examplepassword
MASTODON_HOST=https://mstdn.social
MASTODON_CLIENT_ID=
MASTODON_CLIENT_SECRET=
```

to get the client_id and the client_secret, you will have to run a call to mastodons api,
you can do this with curl:

```shell
    curl -X POST \ 
        -F 'client_name=Test Application' \
        -F 'redirect_uris=urn:ietf:wg:oauth:2.0:oob' \
        -F 'scopes=read write push' \
        -F 'website=https://yourwebsite.ai' \
        https://mstdn.social/api/v1/apps
```
the response should have the necessary credentials.

the commands for your agent to use are
 * "send_toot", in my own experience, it works best if you actually tell it something like "`send a toot saying...`" instead of "please toot ..."
 * "check_mastodon_notifications" will check for new notifications, and if there are any, it will return a list of them, and mark them as read.
 * "reply_to_toot", will reply to a toot, needs the id of the toot it replies to. Using this can look like
   * `reply to toot 123456789 saying hello world`
   * `check your mastodon notifications and reply to any toot that mentions you`
 * "boost_toot", will boost/reblog a toot with the given id. Using this can look like
   * `boost toot 123456789`
   * `check your mastodon notifications and boost any toot that mentions you`