# -*- mode: python ; coding: utf-8 -*-

import sys

# Exclude TK
sys.modules['FixTk'] = None
excludes = ['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter']

a = Analysis(['./main.py'], pathex=None, binaries=None, datas=None,
             hiddenimports=None, hookspath=None, runtime_hooks=None,
             excludes=excludes, win_no_prefer_redirects=False, win_private_assemblies=False,
             cipher=None, noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas, name='asitop',
          debug=False, strip=False, upx=True, runtime_tmpdir=None, console=True)
