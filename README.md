# Automate Linux-LDAP

python automation script to setup linux authentication with yufu.

the script tested on macos, and the tested target linux box on **Ubuntu 18.04.1 LTS**

## Dependencies

1. python 3.x
2. [fabric2](https://github.com/fabric/fabric): `pip3 install fabric2`

## How to Use

1. prepare your config, see conf/ldap.conf, search "replace-me"
2. setup for fengxi@xfd1 and fengxi@xfd2:

   ```shell
   fab2 --prompt-for-login-password --prompt-for-sudo-password -H fengxi@xfd1,fengxi@xfd2 install-deps config
   ```

## Reference

The configuration template refers to:

1. https://www.digitalocean.com/community/tutorials/how-to-authenticate-client-computers-using-ldap-on-an-ubuntu-12-04-vps
2. https://www.debuntu.org/how-to-set-up-a-ldap-server-and-its-clients-page-2/
