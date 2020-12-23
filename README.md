# webots-competition-organizer

## Organize

### Make a repository
First, you need to make a repository like this by clicking on the green button `Use this template`.

### Personal Access Token

PAT (Personal Access Token) is necessary to be able to pull a code from a participant's private repositories.

- Generate a new token [here](https://github.com/settings/tokens)
  - If this repository is hosted at a GitHub organization you will need to create a new GitHub account and generate the token for it.
- [Create a new secret](settings/secrets/actions/new), name it `BOT_PAT_KEY` and paste the key you have just generated.
- [Create a new secret again](settings/secrets/actions/new), name it `BOT_USERNAME` and put your username in it.
  - If this repository is hosted at a GitHub organization use your bot's username.
- Let the participants know they have to add your username to `Settings > Manage access` so you have the right to clone their private repositories.
