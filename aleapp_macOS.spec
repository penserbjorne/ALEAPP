# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['aleapp.py'],
    pathex=['scripts/artifacts'],
    binaries=[],
    datas=[('scripts/', 'scripts')],
    hiddenimports=[
        'bcrypt',
        'bencoding',
        'blackboxprotobuf',
        'Crypto.Cipher.AES',
        'Crypto.Util.Padding',
        'fitdecode',
        'folium',
        'PIL.Image',
        'polyline',
        'xmltodict',
        'xlsxwriter',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='aleapp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity='42F9AD88C52A9888352AB869F1E6EC207A29D308',
    entitlements_file=None,
)
