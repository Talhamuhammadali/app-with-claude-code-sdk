FROM python:3.13
WORKDIR /wd
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y nodejs npm && rm -rf /var/lib/apt/lists/*
RUN npm install -g @anthropic-ai/claude-code
COPY .env .
COPY app .
RUN echo '#!/bin/bash\nexport $(cat .env | grep -v "^#" | xargs)\npython main.py' > start.sh && chmod +x start.sh
ENTRYPOINT ["./start.sh"]