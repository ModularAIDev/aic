#!/bin/bash
gsutil -m cp -r . gs://ai-characters/public/fs

# Make public
gsutil -m acl ch -r -u AllUsers:R gs://ai-characters/public/fs