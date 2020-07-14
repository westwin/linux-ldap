# RHEL sssd

## Refs

1. https://linux.die.net/man/5/sssd-ldap
2. https://tylersguides.com/guides/configure-sssd-for-ldap-on-centos-7/

## configure sssd

1. Set the permissions on the configuration file:

chown root:root /etc/sssd/sssd.conf
chmod 600 /etc/sssd/sssd.conf

2. Enable and Start SSSD
The following command will enable SSSD to start at boot time.

3. systemctl enable sssd

4. systemctl start sssd

## mkhome pre-requsite

1. install semanager: dnf install policycoreutils-python-utils
2. semanage fcontext -a -e /home /home/locale

## Configure NSS and PAM

Run the following command as root to configure PAM and NSS.

 authconfig --enablesssdauth --enablesssd --enablemkhomedir --updateall

## Limitations

1. sudo failed to sync with ldap: use local sudoer