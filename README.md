# Automate Linux-LDAP

python automation script to setup linux authentication with yufu.

the script tested on macos, and the tested target linux box on **Ubuntu 18.04.1 LTS**

## Dependencies

1. python 3.x
2. [fabric2](https://github.com/fabric/fabric): `pip3 install fabric2`

## How to Use

pre-conditions:

1. setup a yufu tenant
2. enable yufu-ldap feature(contact yufu), get a yufu-ldap svc account/passwod
3. setup posix schema in your yufu tenant
    - posix account setup
    - posix group setup
4. setup linux sudoers
    - setup a posix group with name of **sudo** in your yufu tenant
    - assign some users to sudo group in yufu

***NOTE***, before executing the script:

**please keep a logged-in terminal for your target linux box in case the configuration is incorrect, you might can not login back.**

Then run the script:

1. prepare your config, see conf/ldap.conf, search "replace-me"
2. setup for fengxi@xfd1 and fengxi@xfd2:

   ```shell
   fab2 --prompt-for-login-password --prompt-for-sudo-password -H fengxi@xfd1,fengxi@xfd2 install-deps config
   ```

## Reference

The configuration template refers to:

1. https://www.digitalocean.com/community/tutorials/how-to-authenticate-client-computers-using-ldap-on-an-ubuntu-12-04-vps
2. https://www.debuntu.org/how-to-set-up-a-ldap-server-and-its-clients-page-2/
