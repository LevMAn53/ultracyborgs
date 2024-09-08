# Red Flags API

## Get started

Firstly, add anthropic API key:

1. Create `.env` file in the root of the project
2. Add `ANTHROPIC_API_KEY=your_api_key` to the file

### Run API without docker

```bash
fastapi run main.py --proxy-headers --port 8080
```

### Run API with docker

```bash
docker build -t red_flags_image .
docker run -p 8080:8080 red_flags_image
```

or

```bash
docker pull yehorkhod/red_flags:latest
docker run -p 8080:8080 yehorkhod/red_flags:latest
```

## API usage

### Request

Post request to the `http://localhost:8080/red_flags` with the following body:

```json
{
  "text": "text to be analyzed"
}
```

### Response

Response will be in the following format:

```json
[
  {
    RedFlagId: [1/2/3/4],
    Phrase: [string],
    Explanation: [string]
  },
  ...
]
```

## Red flags

  - 1: Whataboutism
  - 2: Emotional Clickbait
  - 3: Trolling
  - 4: Polarization
