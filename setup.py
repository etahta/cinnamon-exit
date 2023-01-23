#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

data_files = [
    ("/usr/share/applications", ["tr.org.pardus.eta-exit.desktop"]),
    ("/usr/share/locale/tr/LC_MESSAGES", ["po/tr/LC_MESSAGES/eta-exit.mo"]),
    ("/usr/share/eta/eta-exit", ["eta-exit.glade", "icon.svg"]),
    ("/usr/share/icons", ["myshutdown.png"]),
    ("/usr/share/icons", ["start.svg"]),
    ("/usr/share/icons/Adwaita/48x48/legacy", ["system-shutdown.png"])
]

setup(
    name="ETA Exit",
    version="0.3.0",
    packages=find_packages(),
    scripts=["eta-exit"],
    install_requires=["PyGObject"],
    data_files=data_files,
    author="Fatih Altun",
    author_email="fatih.altun@pardus.org.tr",
    description="ETA Exit Application",
    license="GPLv3",
    keywords="eta etap",
    url="https://www.pardus.org.tr",
)
