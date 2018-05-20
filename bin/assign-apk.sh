#!/usr/bin/env bash
keytool -genkey -v -keystore pyne2018.jks -keyalg RSA -keysize 2048 -validity 10000 -alias pug-pb
apksigner sign --ks pyne2018.jks --out PythonNordeste2018-1.0.0.apk PythonNordeste2018-1.0.0-release-unsigned.apk
apksigner verify PythonNordeste2018-1.0.0.apksigner

