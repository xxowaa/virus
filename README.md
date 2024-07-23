# Virus 

Virus is a 0 player game inspired by "Conway's Game Of Life" made in python using the `matplotlib` package.
<P>                                                                    



</P>

Here is how to install:

## On Linux Based Distros
Make sure you have installed the `Git` package:
The commands for each os is under:

### Debian-based Systems (e.g., Ubuntu, Linux Mint)
```bash
sudo apt update
sudo apt install git
```

### RHEL-based Systems (e.g., CentOS, Fedora, RHEL)
For CentOS and RHEL:
```bash
sudo yum install git
```
For Fedora:
```bash
sudo dnf install git
```

### Arch-based Systems (e.g., Arch Linux, Manjaro)
```bash
sudo pacman -S git
```

### openSUSE
```bash
sudo zypper install git
```

### Gentoo
```bash
sudo emerge --ask dev-vcs/git
```

### Using Snap (For Distributions that Support Snap)
```bash
sudo snap install git --classic
```

### Using Flatpak (For Distributions that Support Flatpak)
```bash
flatpak install flathub org.freedesktop.Sdk.Extension.git
```

Then make sure you have the `python3` package

The commands for each os is under:


### Debian-based Systems (e.g., Ubuntu, Linux Mint)
```bash
sudo apt update
sudo apt install python3
```

### RHEL-based Systems (e.g., CentOS, Fedora, RHEL)
For CentOS and RHEL:
```bash
sudo yum install python3
```
For Fedora:
```bash
sudo dnf install python3
```

### Arch-based Systems (e.g., Arch Linux, Manjaro)
```bash
sudo pacman -S python
```

### openSUSE
```bash
sudo zypper install python3
```

### Gentoo
```bash
sudo emerge --ask dev-lang/python
```

### Using Snap (For Distributions that Support Snap)
```bash
sudo snap install python38
```

### Using Flatpak (For Distributions that Support Flatpak)
First, ensure that you have the Flathub repository added:
```bash
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```
Then, install Python:
```bash
flatpak install flathub org.python.Python
```

### Verifying Installation
After installing Python using any of the methods above, you can verify the installation by running:
```bash
python3 --version
```

Once you are done, run these commands:

```shell
$ mkdir virus-game
$ cd virus-game
$ git clone https://github.com/xxowaa/virus.git
```





