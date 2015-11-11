#!/usr/bin/env python3

import epicbox

epicbox.configure(
    profiles=[
        epicbox.Profile('base', 'stepic/epicbox-base'),
        epicbox.Profile('python', 'stepic/epicbox-python', network_disabled=False),
    ],
    selinux_enforced=False,
)
files = [{'name': 'main.py', 'content': b'print(42)\n'}]

r = epicbox.run('python', 'python3 main.py', files=files, limits={'cputime': 1})

print(r)