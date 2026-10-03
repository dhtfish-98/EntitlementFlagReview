# Validation record

Scope: Enabled debug task attachment, JIT, unsigned executable memory and disabled library validation.

Local checks to rerun:

```sh
python -m unittest discover -s tests -v
python cli.py --help
python -m compileall -q review.py cli.py tests
```

Check the exact public GitHub commit and its workflow run separately after publishing. Tests use synthetic input; no production system or external target is exercised. A plist declaration alone does not prove code-signing identity, distribution entitlement grant or runtime behavior.

## Current source result (2026-10-02)

- Python 3.14.6: 6/6 unit and CLI integration tests passed.
- Tests include the specific malformed-input, incomplete-review and declaration cases added during the source audit.
- Selected security entitlement values must be booleans. Duplicate plist keys and malformed XML/binary data are rejected using plistlib's dictionary hook; this is still a declaration-only review.
- Test input is synthetic. No external target, live credential or production cluster is exercised.
- The public commit and its corresponding GitHub workflow must be verified separately after this update.
