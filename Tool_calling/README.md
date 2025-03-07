# Tool Calling

Step-by-Step Tutorial Medium Link- https://medium.com/@charikshith.work/tool-calling-made-easy-supercharge-your-llm-with-json-schema-or-langchains-965ff99e0428

Steps to run the code
Install the libraries as mentioned in the imports.
Get your API Keys and place them in the code block.
Run the notebook

docker run -d -p 3000:8080 --gpus all -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:cuda

docker run -d -p 3000:8080 --gpus all -e OLLAMA_BASE_URL=http://localhost:11434/v1 -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main