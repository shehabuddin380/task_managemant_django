from django.contrib.staticfiles.storage import ManifestStaticFilesStorage


class IgnoreMissingManifestStaticFilesStorage(ManifestStaticFilesStorage):
    """
    Django's own ManifestStaticFilesStorage (one of the backends Vercel's
    Django integration officially supports), patched to not crash
    collectstatic when a CSS file references a static asset that doesn't
    actually exist.

    This happens with Django's own admin CSS, which references a couple of
    icon files (e.g. admin/img/sorting-icons.svg) that aren't shipped in
    some Django versions - harmless in practice (the icon just won't
    render), but by default Django's hashed_name() raises a hard ValueError
    for it and aborts the whole collectstatic run.

    Note: this is different from the `manifest_strict` attribute, which
    only affects runtime lookups of already-hashed filenames (stored_name),
    not the hashed_name() step that runs during collectstatic itself - so
    manifest_strict alone doesn't prevent this particular crash.
    """

    def hashed_name(self, name, content=None, filename=None):
        try:
            return super().hashed_name(name, content, filename)
        except ValueError:
            # Referenced file doesn't exist on disk. Skip hashing it and
            # keep the original (unhashed) name instead of crashing the
            # build over a harmless dangling reference.
            print(f"Warning: static file referenced but not found, skipping: {name}")
            return name