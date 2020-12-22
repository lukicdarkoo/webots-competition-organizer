# webots-competition-organizer

## Organize

### Make a repository
First, you need to make a repository like this by clicking on the green button `Use this template`.

### Deploy keys

Deploy keys are necessary to be able to pull a code from participant's private repositories.

- Generate a private-public key pair:

    ```bash
    ssh-keygen -C "lukicdarkoo@gmail.com" -t ed25519 -f /tmp/sshkey -q -N ""
    ```

- [Create a new secret](settings/secrets/actions/new), name it `DEPLOY_KEY` and paste the key from `/tmp/sshkey` (generated in the previous step).

- Share the public key (located in `/tmp/sshkey.pub`) with participants.
