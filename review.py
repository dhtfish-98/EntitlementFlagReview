"""Offline review prompts for selected Apple entitlement declarations."""

from __future__ import annotations

import plistlib

RISK_FLAGS = {
    "com.apple.security.cs.disable-library-validation": "Library validation is disabled",
    "com.apple.security.cs.allow-unsigned-executable-memory": "Unsigned executable memory is allowed",
    "com.apple.security.get-task-allow": "Debug task attachment is allowed",
    "com.apple.security.cs.allow-jit": "JIT is allowed and needs a trust review",
}


def review_bytes(data: bytes) -> list[dict[str, str]]:
    try:
        entitlements = plistlib.loads(data)
    except (ValueError, TypeError, OSError, OverflowError) as exc:
        raise ValueError("invalid entitlement plist") from exc
    if not isinstance(entitlements, dict):
        raise ValueError("entitlements must be a dictionary")
    findings = []
    for key, note in RISK_FLAGS.items():
        if entitlements.get(key) is True:
            findings.append({"rule": "enabled-entitlement", "location": key, "note": note})
    return findings


def review_text(text: str) -> list[dict[str, str]]:
    return review_bytes(text.encode("utf-8"))
