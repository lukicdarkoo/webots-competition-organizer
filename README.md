# webots-competition-organizer-template

## Organize
First, generate a private-public key pair:
```bash
ssh-keygen -C "lukicdarkoo@gmail.com" -t ed25519 -f /tmp/sshkey -q -N ""
```

Then [create a new secret](settings/secrets/actions/new), name it `DEPLOY_KEY_PRIVATE` and paste the key from `/tmp/sshkey` (generated in the previous step).

Share the public key (located in `/tmp/sshkey.pub`) with participants.

## Participate

To start developing clone the necessary repositories:
```bash
git clone https://github.com/lukicdarkoo/webots-competition-template.git
git clone https://github.com/lukicdarkoo/webots-competition-participant-template.git webots-competition-template/controllers/participant_controller
```
and run Webots:
```bash
webots webots-competition-template/worlds/ratslife_round.wbt
```
