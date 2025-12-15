# Documentation

This repository contains two kinds of documentation:

- **Handwritten docs**: small project docs you should read first (this file, plus future additions).
- **Generated docs snapshot**: a large, generated single-page reference that aggregates TomTom Traffic API documentation pages.

## What’s in here

- `tomtom-traffic-api.md`
  - A **generated** aggregation of TomTom Traffic API documentation content (TomTom Maps + TomTom Orbis Maps variants).
  - This file is used by tests to ensure the SDK covers all non-gated endpoints mentioned in the snapshot.

- `spec/tomtom-traffic-api.yml`
  - A **downloaded** OpenAPI spec referenced by the snapshot.

## How to use the docs

- Start with the SDK README at `../README.md` for installation and usage.
- Use `tomtom-traffic-api.md` when you need a full parameter listing / response examples, or when adding support for new endpoints.

## Licensing and third-party materials

See `../NOTICE` and `../LICENSES/CC-BY-SA-4.0.txt`.
