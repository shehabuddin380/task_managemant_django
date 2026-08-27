from django.contrib.staticfiles.storage import ManifestStaticFilesStorage


class IgnoreMissingManifestStaticFilesStorage(ManifestStaticFilesStorage):
  
    manifest_strict = False