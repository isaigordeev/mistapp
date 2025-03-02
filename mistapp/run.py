import subprocess
import json
import time

from mistapp import experience, sample_lead_role, sample_junior_role
from config import url_server_service, url_host_service, HOST_PORT

import uvicorn
import os

if __name__ == "__main__":
    server_process = subprocess.Popen(
        ["uvicorn", "mistapp.main:app", "--host", "0.0.0.0", "--port", str(HOST_PORT), "--reload"])

    # Wait a few seconds for the server to start
    time.sleep(2)

    request = {
        "experience": experience,
        "role": sample_lead_role,
        "postprompt": "Explain your decision. Output in json format",
    }

    json_data = json.dumps(request)

    curl_command = [
        'curl',
        '-X', 'POST',
        url_host_service,
        '-H', 'Content-Type: application/json'
        ,'-d', json_data,
    ]

    response = subprocess.run(curl_command, capture_output=True, text=True)
    print(response.stdout)

    server_process.terminate()