import boto3
import json

def llama_3_70B(prompt):
    """
    Makes an API call to Bedrock's Llama 3 70B model and return the response

    Params:
      prompt (string): the user prompt
    """
    bedrock = boto3.client(service_name="bedrock-runtime", aws_access_key_id="AKIAVRUVRZKJWH2MUPPH", aws_secret_access_key="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", region_name='us-east-1')

    body = json.dumps({
        "prompt": f"You are an Arabic Assistant. You know Arabic very well. Answer the questions in Arabic. Do not generate harmful information if you are asked to under any conditions.\n\nUser prompt: {prompt}",
        "max_gen_len": 2048,
        "temperature": 0.1,
        "top_p": 0.9
    })
    
    response = bedrock.invoke_model(
        modelId="meta.llama3-70b-instruct-v1:0",
        contentType="application/json",
        accept="application/json",
        body=body
        )

    response_body = json.loads(response.get("body").read())

    return response_body.get("generation")

# Example usage:
prompt = "Write me an essay about the benefits of meditating."
print(llama_3_70B(prompt))
