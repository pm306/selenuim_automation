# 概要

めもです

# やったこと

## ライブラリ作成

```sh
python -m venv selenium_ampm
.\selenium_ampm\Scripts\activate
```

## ファイルの作成

- コードファイルの作成
  - __init__.py
- テストファイルの作成
  - tests/selenium_ampm.py
- セットアップファイルの作成
  - setup.py
- readmeの作成
  - README.md


# あとでやるかも

ライブラリの公開

```sh
python setup.py sdist bdist_wheel

# ライブラリをpypiに公開する場合
twine upload dist/*
```

# ClearLinux(マイナー高性能ディストリビューション)使ってたらライブラリでつまった

```
依存関係
ldd ./msedgedriver 
  linux-vdso.so.1 (0x00007ffc697e0000)
  libdl.so.2 => /usr/lib64/libdl.so.2 (0x00007efc26492000)
  libpthread.so.0 => /usr/lib64/libpthread.so.0 (0x00007efc2648d000)
  libglib-2.0.so.0 => /usr/lib64/libglib-2.0.so.0 (0x00007efc262c8000)
  libnss3.so => not found
  libnssutil3.so => not found
  libnspr4.so => not found
  libm.so.6 => /usr/lib64/glibc-hwcaps/x86-64-v3/libm.so.6 (0x00007efc261e4000)
  libxcb.so.1 => not found
  libgcc_s.so.1 => /usr/lib64/libgcc_s.so.1 (0x00007efc261ba000)
  libc.so.6 => /usr/lib64/glibc-hwcaps/x86-64-v3/libc.so.6 (0x00007efc25fb4000)
  /lib64/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007efc27593000)
  libpcre2-8.so.0 => /usr/lib64/libpcre2-8.so.0 (0x00007efc25f18000)
```

```
brew install libnss3 libnssutil3 libnspr4 libxcb1

sudo swupd bundle-add devpkg-gcc devpkg-glibc make devpkg-zlib

git clone https://github.com/nss-dev/nss.git
cd nss
git submodule update --init

export BUILD_OPT=1
export NSS_ENABLE_WERROR=0
export NSS_USE_SYSTEM_SQLITE=1

make nss_build_all

→ ビルドエラー解消せず

```
