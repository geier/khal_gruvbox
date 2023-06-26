from khal.api import register_color_theme

bg0 = dark0       = '#282828'
bg1 = dark1       = '#3c3836'
bg2 = dark2       = '#504945'
bg3 = dark3       = '#665c54'
bg4 = dark4       = '#7c6f64'

gray_245    = '#928374'
gray_244    = '#928374'

fg0 = light0      = '#fbf1c7'
fg1 = light1      = '#ebdbb2'
fg2 = light2      = '#d5c4a1'
fg3 = light3      = '#bdae93'
fg4 = light4      = '#a89984'

bright_red     = '#fb4934'
bright_green   = '#b8bb26'
bright_yellow  = '#fabd2f'
bright_blue    = '#83a598'
bright_purple  = '#d3869b'
bright_aqua    = '#8ec07c'
bright_orange  = '#fe8019'

neutral_red    = '#cc241d'
neutral_green  = '#98971a'
neutral_yellow = '#d79921'
neutral_blue   = '#458588'
neutral_purple = '#b16286'
neutral_aqua   = '#689d6a'
neutral_orange = '#d65d0e'

faded_red      = '#9d0006'
faded_green    = '#79740e'
faded_yellow   = '#b57614'
faded_blue     = '#076678'
faded_purple   = '#8f3f71'
faded_aqua     = '#427b58'
faded_orange   = '#af3a03'

gruvbox = [
    ('header', '', '', '', fg1, bg2),
    ('footer', '', '', '', fg1, bg2),
    ('line header', 'black', 'white', 'bold', '', ''),
    ('alt header', 'white', '', 'bold'),
    ('bright', 'dark blue', 'white', ('bold', 'standout')),
    ('list', '', ''),
    ('list focused', 'white', 'light blue', 'bold'),
    ('edit', '', '', '', fg1, bg2),
    ('edit focus', '', '', '', fg1, bg3),
    ('button', '', '', '', bg1, neutral_blue),
    ('button focused', 'white', 'light blue', 'bold'),

    ('reveal focus', '', '', 'bold', fg0, bg1),
    ('today focus', 'white', 'dark magenta'),
    ('today', 'dark gray', 'dark green',),

    ('date header', '', '', '', fg1, bg1),
    ('date header focused', '', '', '', fg0, bg4),
    ('date header selected', '', '', '', fg2, bg2),

    ('dayname', '', '', '', fg1 + ',bold', bg0),
    ('monthname', '', '', '', fg1 +',bold', bg0),
    ('weeknumber_right', '', '', '', fg4, bg0),
    ('weeknumber_left', '', ''),
    ('alert', '', ''),
    ('mark', '', '', '', fg0, faded_aqua),
    ('frame', '', '', '', fg4, bg0),
    ('frame focus', '', '', '', faded_green, bg0),
    ('frame focus color', '', '', '', faded_red, bg0),
    ('frame focus top', '', '', '', fg2, bg0),

    ('eventcolumn', '', '', '', fg0, bg0),
    ('eventcolumn focus', '', '', '', fg0, bg0),
    ('calendar', '', '', '', fg1, bg0),
    ('calendar focus', '', '', '', fg1, bg0),
    ('editor', '', '', '', fg1, bg0),
    ('editor focus', '', '', '', fg1, bg0),

    ('editbx', 'light gray', 'dark blue'),
    ('editcp', 'black', 'light gray', 'standout'),
    ('popupbg', 'white', 'black', 'bold'),
    ('popupper', 'white', 'dark cyan'),
    ('caption', '', '', 'bold', fg1 + ',bold', bg0),
]

register_color_theme('gruvbox', gruvbox)
