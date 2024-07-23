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
mkdir virus-game
cd virus-game
git clone https://github.com/xxowaa/virus.git
python3 main.py
```

You now have the **Virus** game on your linux os.

## Install on Windows

The ways of installing python on windows is listed below:


#### 1. **Chocolatey**
1. Open Command Prompt or PowerShell as an administrator.
2. Install Chocolatey using the following command:
    ```powershell
    Set-ExecutionPolicy Bypass -Scope Process -Force; `
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
    iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    ```
3. Install Python using Chocolatey:
    ```powershell
    choco install python
    ```

#### 2. **Scoop**
1. Open PowerShell.
2. Install Scoop using the following command:
    ```powershell
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    irm get.scoop.sh | iex
    ```
3. Install Python using Scoop:
    ```powershell
    scoop install python
    ```

#### 3. **WinGet**
1. Open Command Prompt or PowerShell.
2. Install Python using WinGet:
    ```powershell
    winget install Python.Python.3
    ```

### Using the Microsoft Store
1. Open the Microsoft Store.
2. Search for "Python".
3. Select the version of Python you want to install (e.g., Python 3.9, Python 3.10).
4. Click "Get" or "Install" to download and install Python.

Once you are done with any of the above run these commands in the command prompt:

```batch
mkdir virus-game && cd virus-game
```

Click this button:




[![Download game](https://lelbois.nekoweb.org/download.svg)](https://github.com/xxowaa/virus/raw/main/virus.zip)

Drop the `virus.zip` folder into the `virus-game` folder.



