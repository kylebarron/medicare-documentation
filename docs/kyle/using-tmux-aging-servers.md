# Using tmux on the Aging Servers

My VPN connection to the Aging servers often will time out and disconnect for some reason. This causes the SSH connection to be lost, making me sign in again and restart whatever I was doing.

This is really annoying, but there are ways to prevent losing your work and to facilitate running long jobs.

## Set up

Make sure tmux is installed. You can do this from the command line with
```
tmux -V
```

As of January 2018, the version of tmux installed by default is 1.6. That version was released 6 years ago, in January 2012. The current version is 2.6. Follow [this code](#upgrading-tmux) if you wish to install the newest version in your local account on the servers.

You might want to copy my tmux configuration file as well, which makes it easier to start using tmux.


## Signing back into a previous session

Use `tmux ls` to see your currently running sessions of tmux.

```
> tmux ls
0: 1 windows (created Mon Jan  8 11:01:46 2018) [224x61]
```

This tells me that the session with name `0` was created on January 8 and is still running.

To reopen that session, I can do:
```
> tmux attach -t 0
```
and it will reopen all the windows I last had open.


## Upgrading tmux

The following code will install the [latest version](https://github.com/tmux/tmux/releases/latest) of tmux onto your user account.

```bash
mkdir -p ~/local/share
echo 'CPPFLAGS=-I$HOME/local/include' > ~/local/share/config.site
echo 'LDFLAGS=-L$HOME/local/lib' >> ~/local/share/config.site
wget `curl -s https://api.github.com/repos/libevent/libevent/releases/latest | grep 'browser_download_url' | grep -P '.tar.gz(?!\.asc)' | cut -d '"' -f 4` -O libevent.tar.gz
tar -xvzf libevent.tar.gz
mv libevent*stable/ libevent/
cd libevent
./configure --prefix=$HOME/local
make && make install
cd $HOME
rm -rf libevent/ libevent.tar.gz

wget `curl -s https://api.github.com/repos/tmux/tmux/releases/latest | grep 'browser_download_url' | grep -P '.tar.gz(?!\.asc)' | cut -d '"' -f 4` -O tmux.tar.gz
tar -xvzf tmux.tar.gz
mv tmux*/ tmux/
cd tmux
./configure --prefix=$HOME/local
make && make install
cd $HOME
rm -rf tmux/ tmux.tar.gz
```



