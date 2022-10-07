#!/bin/sh

app_name=eta-exit
app_version=0.1.1

xgettext --default-domain=eta-exit \
         --from-code=utf-8 \
         --language=Python \
         --output=eta-exit.pot \
         --package-name=$app_name \
         --package-version=$app_version \
         eta-exit

msgmerge --lang=tr \
         --update \
         po/tr/LC_MESSAGES/eta-exit.po \
         eta-exit.pot \

msgfmt --check --directory=po/tr/LC_MESSAGES/ \
       --output-file=po/tr/LC_MESSAGES/eta-exit.mo \
       eta-exit.po \
