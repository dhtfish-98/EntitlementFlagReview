# EntitlementFlagReview

Review selected security-relevant declarations in a local Apple entitlements plist. It runs locally, does not contact targets, and reports review prompts instead of exploit instructions.

## Input and checks

- Input: XML or binary plist from a system you own or are authorized to inspect.
- Checks: Enabled debug task attachment, JIT, unsigned executable memory and disabled library validation.
- Output: rule, local location and short note. No source snippets, credential values or log identities are printed.

## Run

```sh
python cli.py ./owned-input
python cli.py ./owned-input --json
python -m unittest discover -s tests -v
```

Exit code 0 means no findings, 1 means review findings, 2 means invalid input or read failure. A clean result is not a security guarantee. The file input limit is 4 MiB; ArtifactDigestReview also limits each artifact to 128 MiB.

## Boundaries

A plist declaration alone does not prove code-signing identity, distribution entitlement grant or runtime behavior. Work only on local, authorized inputs. The analysis does not send data to a service or modify the inspected files.

## Source and policy context

- Technical reference: https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.cs.disable-library-validation
- See [ORIGIN.md](ORIGIN.md) for implementation provenance and [VALIDATION.md](VALIDATION.md) for checks performed.
- CVP eligibility depends on a real, legitimate defensive task affected by Claude's cyber safeguards and the applicant's organization/identity review; this repository alone does not establish eligibility or approval. [Anthropic CVP guidance](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet).
