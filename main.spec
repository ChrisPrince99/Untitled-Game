# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew, gstreamer

block_cipher = None


a = Analysis(['C:\\Users\\soloc\\PycharmProjects\\Untitled Game\\main.py'],
             pathex=['C:\\Users\\soloc\\PycharmProjects\\Untitled Game'],
             binaries=[],
             datas=[( 'main.kv', '.' )],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='Untitled Game',
          icon='Film.ico',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
