#!/bin/bash
# Uplaod via gcloud to gs://ai-characters/public/jess
gsutil -m cp -r . gs://ai-characters/public/jess

# Make public
gsutil -m acl ch -r -u AllUsers:R gs://ai-characters/public/jess