---
type: topic
status: active
theme: ai-engineering
updated: 2026-10-01
---

# AI Infrastructure

Registry id: `ai-infrastructure`. Covers inference servers, GPU serving and serving performance (vLLM, Triton, TensorRT).

## Current State

- **vLLM:** latest release recorded is v0.30.0 (2026-09-22). Upgrading to it needs config changes; see Practical Impact.
- Nothing is recorded yet for Triton, TensorRT or other serving stacks.

## Key Developments

- **2026-09-22 — vLLM v0.30.0.** Breaking changes to `vllm serve` flags, GPTQ and several environment variables. New: a "Fast Start" GPU weight-cache daemon for quick engine restarts, and Gumbel-max watermarking. → [[2026-09-22-vllm-v0-30-0-release]]

## Recent News

- [[2026-09-22-vllm-v0-30-0-release]] — action

## Practical Impact

Before upgrading a vLLM deployment to v0.30.0:

- Scale-out endpoints are off unless `--enable-scale-out` is passed. The `VLLM_ENABLE_SCALE_OUT_ENDPOINTS` environment variable no longer works.
- `VLLM_PREFIX_CACHE_RETENTION_INTERVAL` and `VLLM_MM_HASHER_ALGORITHM` are removed.
- GPTQ activation ordering (`g_idx`) is removed.
- `python -m vllm.entrypoints.grpc_server` is deprecated; use `vllm serve --grpc`.
- Vendor YaRN aliases no longer re-scale `max_model_len`.
- The default wheel targets CUDA 13.0; CUDA 12.9 needs the separate wheels or images.

## Open Questions

- Does Fast Start (`--load-format ipc_cache`) deliver the restart times the release notes claim on other hardware? The 28.9s → 8.2s engine-init figure is the project's own number, on H200.
- vLLM shipped v0.28, v0.29 and v0.30 within about four weeks. How often do breaking changes land at this pace?

## Related Topics

- [[model-deployment|Model Deployment]] — the vLLM note is filed under both topics; no Topic note exists for this one yet
