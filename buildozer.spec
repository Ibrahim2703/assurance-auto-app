[app]
title = Assurance Auto
package.name = assuranceauto
package.domain = com.assurance.auto

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0

requirements = python3,kivy,kivymd,pillow,requests

presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0

# Android specific
android.minapi = 21
android.api = 33
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True
android.arch = arm64-v8a

android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Java compatibility fixes
android.gradle_dependencies = com.sun.xml.bind:jaxb-core:2.3.0.1, com.sun.xml.bind:jaxb-impl:2.3.0.1, javax.xml.bind:jaxb-api:2.3.0
android.add_compile_options = --add-modules ALL-SYSTEM

[buildozer]
log_level = 2
warn_on_root = 1