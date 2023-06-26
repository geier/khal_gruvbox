# Gruvbox khal color scheme

This is a [gruvbox](https://github.com/morhetz/gruvbox) color scheme for
[khal](https://github.com).

**This is work in progress and highly experimental preview and anything can
change at anytime** and only publicated as a preview for people helping in the
development process.


**Note: I will force push into this repository until this notice is removed**

This will only work if you are currently running the
[config_based_theming branch](https://github.com/pimutils/khal/pull/1279) (which
also supports plugins for color themes).

Clone this repo to `$XDG_DATA_HOME/khal/plugins/` (which probably is
`~/.local/share/khal/plugins/`) and make the following
settings in your khal config file:

```
[view]
theme = gruvbox
```
