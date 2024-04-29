# Gruvbox khal color scheme

This is a [gruvbox](https://github.com/morhetz/gruvbox) color scheme for
[khal](https://github.com/pimutils/khal/) which makes use of the new
[plugin system](https://github.com/pimutils/khal/pull/1303).
At the moment of this writing (2024-04-29), the plugin system has not made it
into the latest release of khal, so you will have to install from khal's master
branch.

## Installation

Install the python project in this repository, e.g.

```bash
pip install git+https://github.com/geier/khal_gruvbox@importlib
```

and add the following to your khal configuration file (usually `~/.config/khal/khal.conf`):

```
[view]
theme = gruvbox
```
<img width="868" alt="image" src="https://github.com/geier/khal_gruvbox/assets/275330/60ba54c9-2bff-4ba7-8630-c144f2705898">
