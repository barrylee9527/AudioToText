# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['avi_to_text.py'],
             pathex=['H:\\pythonitems\\first\\PYQT5\\avi_text'],
             binaries=[],
             datas=[('./static/index.html', './static'), ('./static/js/*', './static/js'), ('./static/css/*', './static/css'), ('./static/css/fonts/*', './static/css/fonts')],
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
          [],
          name='avi_to_text',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='logo.ico')
