import urllib3
import json

http = urllib3.PoolManager()


def handler(event, context):
    print("calling slack!!!")
    url = "https://hooks.slack.com/services/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"
    msg = {
        "channel": "#aws-cdk-events",
        "text": event["Records"][0]["Sns"]["Message"],
    }

    encode_msg = json.dumps(msg).encode("utf-8")
    resp = http.request("POST", url, body=encode_msg)
    print(
        {
            "message": event["Records"][0]["Sns"]["Message"],
            "status_code": resp.status,
            "response": resp.data,
        }
    )
