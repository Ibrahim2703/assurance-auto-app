[app]
title = Assurance Auto
package.name = assuranceauto
package.domain = com.assurance.auto

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
source.exclude_dirs = tests, bin, venv, .git, __pycache__, .buildozer

version = 1.0

requirements = python3,kivy==2.1.0,kivymd,pillow,requests,hostpython3

presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png

orientation = portrait
fullscreen = 0

# Android specific
android.minapi = 21
android.api = 33
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True
android.arch = arm64-v8a

android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Simplification des dépendances Gradle
android.gradle_dependencies = 

# Configuration Gradle
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1