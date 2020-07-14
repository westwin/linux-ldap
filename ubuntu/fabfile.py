#!/usr/bin/env python3
# encoding: utf-8
'''
fabfile -- automation script to setup linux with ldap.

@author:     FengXi

USAGE:
    fab2 -e --prompt-for-login-password \
         --prompt-for-sudo-password \
         -H root@server1,root@server2 \
         install-deps config
'''

from fabric2 import task, Connection
from fabric2 import SerialGroup as Group


@task()
def os_version(c):
    """
    test util to print ubuntu version
    """
    c.run("lsb_release -a")


@task()
def install_deps(c):
    """
    install all depedencies to integrate ubuntu with ldap.

    This task suppresses the configuration.
    """
    c.sudo("DEBIAN_FRONTEND=noninteractive apt-get install -y ldap-utils libpam-ldap nscd")


@task()
def config(c):
    """
    apply the configuration. Please make your own changes based on the the configuration template under conf/ .

    The configuration template refers to:
    1. https://www.digitalocean.com/community/tutorials/how-to-authenticate-client-computers-using-ldap-on-an-ubuntu-12-04-vps
    2. https://www.debuntu.org/how-to-set-up-a-ldap-server-and-its-clients-page-2/ 
    """
    def sudo_install(connection, source, dest, *, owner='root', group='root', mode='0644'):
        """
        Helper which installs a file with arbitrary permissions and ownership

        This is a replacement for Fabric 1's `put(…, use_sudo=True)` and adds the
        ability to set the expected ownership and permissions in one operation.
        """

        mktemp_result = connection.run('mktemp', hide='out')
        assert mktemp_result.ok

        temp_file = mktemp_result.stdout.strip()

        try:
            connection.put(source, temp_file)
            connection.sudo(
                f'install -o {owner} -g {group} -m {mode} {temp_file} {dest}')
        finally:
            connection.run(f'rm {temp_file}')

    # backup first, TODO, @fengxi

    # copy changes
    sudo_install(c, "conf/ldap.conf", '/etc/ldap.conf', )
    sudo_install(c, "conf/nscd.conf", '/etc/nscd.conf', )
    sudo_install(c, "conf/nsswitch.conf", '/etc/nsswitch.conf', )
    sudo_install(c, "conf/common-auth", '/etc/pam.d/common-auth')
    sudo_install(c, "conf/common-session", '/etc/pam.d/common-session')
    sudo_install(c, "conf/common-password", '/etc/pam.d/common-password')

    # restart to apply the changes. dangerous please ensure the configuration is correct
    c.sudo("systemctl restart nscd")


@task()
def uninstall_deps(c):
    """
    uninstall the dependencies
    """
    c.sudo("DEBIAN_FRONTEND=noninteractive apt-get remove -y libpam-ldap nscd")
