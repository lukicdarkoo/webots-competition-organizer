# webots-competition-organizer-template

## Apply
- Make a new repository out of [the template](https://github.com/lukicdarkoo/webots-competition-participant-template).
- Add a deploy key `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMUXWdf+lWW/RYM2ScBUsqzmq4xbU/RCLyFoPSI5eO05 lukicdarkoo@gmail.com` in [here](../../settings/keys/new).
- Add your repository to [competitors.txt](edit/main/competitors.txt).

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
