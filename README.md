# cover-letter-cli-agent

LLM Agent for creating cover letters from a CLI

## Project Description

**cover-letter-cli-agent** is a command-line tool that leverages a LLM to automatically generate cover letters. It uses `langchain` and structured  YAML configuration file with a Markdown promt template to tailor each letter to the candidate and job description. The agent runs inside a secure Docker container and interacts with the LLM via a proxy endpoint(any OpenAI compatible service should work).

## Features

- Generates markdown-formatted cover letters based on configurable templates
- Uses YAML config for candidate and job details
- Outputs ready-to-use cover letters in the `/llm-agent-workdir` directory
- Runs securely in a containerized environment
- Supports OpenAI-compatible LLMs (e.g., Llama-3)

## Project Structure

```
llm-agent-workdir/
  ├── main.py                # Main entrypoint for the agent logic
  ├── prompts/
  │     ├── config.yaml      # Candidate and job configuration
  │     └── cover_letter_template.md  # Prompt template for the LLM
  └── ...
entrypoint.sh                # Entrypoint script for Docker
run.sh                       # Script to launch the Docker container
.env                         # Environment variables (API keys, endpoints)
```

## Prerequisites

- Docker installed on your system
- An OpenAI-compatible API key and endpoint (set in `.env`)

## How to Run

1. **Configure your environment:**
   - Edit `.env` with your API key and endpoint.
   - Edit `llm-agent-workdir/prompts/config.yaml` with your candidate and job details.

2. **Build the Docker image (if not already built):**
   ```
   docker build -t llm-agent-safe .
   ```

3. **Run the agent:**
   ```
   ./run.sh
   ```

   This will:
   - Set permissions for the work directory
   - Launch the agent in a secure, read-only Docker container
   - Output the generated cover letter in `/llm-agent-workdir` 

## Customization

- **Templates:** Modify `llm-agent-workdir/prompts/cover_letter_template.md` for different letter styles.
- **Config:** Change `llm-agent-workdir/prompts/config.yaml` for new candidates or job postings.

## Notes

- The agent is designed for security and privacy; it does not expose your API key or data outside the container.
- Generated cover letters are saved in Markdown format for easy editing or conversion to PDF.

## License

MIT License
