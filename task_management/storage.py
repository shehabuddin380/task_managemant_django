from whitenoise.storage import CompressedManifestStaticFilesStorage


class IgnoreMissingManifestStaticFilesStorage(CompressedManifestStaticFilesStorage):
    """
    Same as WhiteNoise's CompressedManifestStaticFilesStorage (which Vercel
    officially supports for serving static files from its CDN), except it
    doesn't crash the whole `collectstatic` run when a CSS file references
    a static asset that can't be found.

    This happens with Django's own admin CSS, which references a couple of
    icon files (e.g. admin/img/sorting-icons.svg) that aren't always shipped
    depending on the Django version. That's harmless in practice - the
    missing icon just won't render - but the default manifest storage treats
    it as a fatal error and aborts collectstatic entirely.

    This subclass logs a warning for any such file instead of raising.
    """

    def post_process(self, *args, **kwargs):
        for name, hashed_name, processed in super().post_process(*args, **kwargs):
            if isinstance(processed, Exception):
                print(f"Warning: ignoring missing static file reference: {name} ({processed})")
                continue
            yield name, hashed_name, processed