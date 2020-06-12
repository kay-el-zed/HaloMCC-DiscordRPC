# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Halo_MCC_Rich_Presence.py'],
             pathex=['C:\\Users\\Gurrman375D\\Documents\\GitHub\\HaloMCC-DiscordRPC\\Halo MCC Rich Presence'],
             binaries=[],
             datas=[],
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
          name='Halo_MCC_Rich_Presence',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='Images\\halo.ico')
