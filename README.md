# webots-competition-organizer

## Organize

### Make a repository
First, you need to make a repository like this by clicking on the green button `Use this template`.

### Personal Access Token

PAT (Personal Access Token) is necessary to be able to pull a code from a participant's private repositories.

- Generate a new token [here](https://github.com/settings/tokens)
  - If this repository is hosted at a GitHub organization you will need to create a new GitHub account and generate the token for it.
- [Create a new secret](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository), name it `BOT_PAT_KEY` and paste the key you have just generated.
- [Create a new secret again](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository), name it `BOT_USERNAME` and put your username in it.
  - If this repository is hosted at a GitHub organization use your bot's username.
- Let the participants know they have to add your username to `Settings > Manage access` so you have the right to clone their private repositories.

### Customize
The sample competition is just a sample and you probably want implement a custom scenario and rules.

- Change the scenario in the world file ([`worlds/ratslife_round.wbt`](worlds/ratslife_round.wbt)).
- Change the [`contest manager controller`](controllers/contest_manager):
  - The purpose of this [supervisor](https://www.cyberbotics.com/doc/reference/supervisor) controller is to keep a track of the competitors and their points, something like a referee.
  - You should write the competition results to `/tmp/winner.txt`, so the results can be parsed by CI.
  - Once the match is over, you should use the [Emitter](https://www.cyberbotics.com/doc/reference/emitter) node to send `done` on channel 1024 so our animation recorder is aware the match is done.
