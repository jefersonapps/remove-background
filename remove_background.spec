# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['remove_background.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['scipy._lib.array_api_compat.numpy.fft', 'scipy.special', 'scipy.special._special_ufuncs', 'PIL._tkinter_finder'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='remove_background',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets/icon.png'],
)
