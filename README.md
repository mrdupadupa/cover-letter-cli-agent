# cover-letter-cli-agent

LLM Agent for creating cover letters from a CLI

## Project Description

**cover-letter-cli-agent** is a command-line tool that leverages an LLM to automatically generate cover letters. It uses `langchain` and a structured YAML configuration file with a Markdown prompt template to tailor each letter to the candidate and job description. The agent runs inside a secure Docker container and interacts with the LLM via a proxy endpoint (any OpenAI-compatible service should work).

## Features

- Generates markdown-formatted cover letters based on configurable templates
- Uses YAML config for candidate and job details
- Outputs ready-to-use cover letters in the `workdir/cover_letters` directory
- Runs securely in a containerized environment
- Supports OpenAI-compatible LLMs (e.g., Llama-3)

## Project Structure

```
workdir/
  ├── main.py                # Main entrypoint for the agent logic
  ├── prompts/
  │     ├── config.yaml      # Candidate and job configuration
  │     └── cover_letter_template.md  # Prompt template for the LLM
  └── cover_letters/         # Output directory for generated cover letters
entrypoint.sh                # Entrypoint script for Docker
run.sh                       # Script to launch the Docker container
.env                         # Environment variables (API keys, endpoints)
requirements.txt             # Python dependencies
Dockerfile                   # Docker build instructions
```

## Prerequisites

- Docker installed on your system
- An OpenAI-compatible API key and endpoint (set in `.env`)

## How to Run

1. **Configure your environment:**
   - Copy `.env.example` to `.env`:
   ```
   cp .env.example .env
   ```
   - Edit `.env` with your API key and endpoint.
   - Edit `workdir/prompts/config.yaml` with your candidate and job details.

3. **Build the Docker image (if not already built):**
   ```
   docker build -t llm-agent-safe .
   ```

4. **Run the agent:**
   ```
   ./run.sh
   ```

   This will:
   - Set permissions for the output directory
   - Launch the agent in a secure, read-only Docker container
   - Output the generated cover letter in `workdir/cover_letters/`

## Customization

- **Templates:** Modify `workdir/prompts/cover_letter_template.md` for different letter styles.
- **Config:** Change `workdir/prompts/config.yaml` for new candidates or job postings.

## Notes

- The agent is designed for security and privacy; it does not expose your API key or data outside the container.
- Generated cover letters are saved in Markdown format for easy editing or conversion to PDF.
- You can convert the Markdown files to PDF using tools like [md2pdf](https://github.com/jmaupetit/md2pdf) or Pandoc.

## License

MIT License