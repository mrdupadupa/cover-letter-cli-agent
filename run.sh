#!/bin/bash
mkdir -p "$PWD/workdir/cover_letters"
chmod -R 777 "$PWD/workdir/cover_letters"

# Run the agent in a Docker container with read-only filesystem and tmpfs

docker run -it --rm \
  --read-only \
  -v "$PWD/workdir:/workspace:rw" \
  -w /workspace \
  --tmpfs /tmp \
  --cap-drop ALL \
  llm-agent-safe


