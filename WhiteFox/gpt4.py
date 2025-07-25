"""
You will need to use your own OpenAI API key to run this script.
"""

import argparse
# import openai
import time
import os
import json
from pathlib import Path
from openai import OpenAI

# You need to create a file named "openai.key" and put your API key in it
# OpenAI.api_key = Path("openai.key").read_text().strip()
system_message = "You are a source code analyzer for {}."

def process_msg(msg):
    """Extract code blocks."""
    if "```" not in msg:
        # the whole response message is a python program
        return msg
    code_st = False
    code = ""
    for line in msg.splitlines():
        if code_st:
            if line.strip().startswith("```"):
                # end of code block
                # but there might be more code blocks
                code_st = False
                continue
            code += line + "\n"
        else:
            if line.strip().startswith("```"):
                code_st = True
    return code


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt-dir", type=str, default="prompt/demo")
    parser.add_argument("--outdir", type=str, default="chatgpt/zero-shot")
    parser.add_argument("--iter", type=int, default=1)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--prompt-only", action="store_true")
    parser.add_argument("--target", type=str, default="PyTorch")
    parser.add_argument("--model", type=str, default="gpt-4")

    args = parser.parse_args()

    system_message = system_message.format(args.target)

    prompt_dir = Path(args.prompt_dir)
    opts = {}
    for prompt_file in prompt_dir.iterdir():
        if not prompt_file.is_file():
            continue
        opts[prompt_file.stem] = prompt_file.read_text()

    outdir = args.outdir
    iteration = args.iter
    top_p = 1.0
    temperature = args.temperature
    n_batch_size = args.batch_size

    for opt_idx, opt in enumerate(opts):
        if os.path.exists(os.path.join(outdir, opt, f"{opt}_1.py")):
            print("Skipping opt ", opt)
            continue

        code_idx = 0
        ret = {"opt": opt}
        ret["response"] = {}
        os.makedirs(os.path.join(outdir, opt), exist_ok=True)
        user_input = opts[opt]
        with open(os.path.join(outdir, opt, f"prompt.txt"), "w") as f:
            f.write(user_input)

        if args.prompt_only:
            print(opt_idx)
            continue

        for i in range(iteration):
            while True:
                try:
                    t_start = time.time()
                    client = OpenAI(base_url='https://xiaoai.plus/v1', api_key = 'sk-CqyEysmgXjYHAii5TWsSmWilaQS4G3L5f3URxoEAszjQHrEL')
                    response = client.chat.completions.create(
                    # response = openai.ChatCompletion.create(
                        model='gpt-4o',
                        messages=[
                            {"role": "system", "content": system_message},
                            {"role": "user", "content": user_input},
                        ],
                        # max_tokens=256,
                        max_tokens=512,
                        top_p=top_p,
                        temperature=temperature,
                        n=n_batch_size,
                        # request_timeout=300,
                        timeout=300,
                    )
                    g_time = time.time() - t_start
                    break
                except Exception as e:
                    print(e)
                    time.sleep(10)
            print(f"[{opt_idx+1}/{len(opts)}] {opt} used time: ", g_time)
            # msgs = [resp.message.content for resp in response["choices"]]
            msgs = [choice.message.content for choice in response.choices]
            codes = []
            for msg in msgs:
                code = process_msg(msg)
                codes.append(code)
                code_idx += 1
                with open(os.path.join(outdir, opt, f"{opt}_{code_idx}.py"), "w") as f:
                    f.write(code)
                with open(os.path.join(outdir, opt, f"{opt}_{code_idx}.txt"), "w") as f:
                    f.write(msg)
            
            response_dict = {
                "id": response.id,
                "object": response.object,
                "created": response.created,
                "model": response.model,
                "choices": [
                    {
                        "message": {
                            "role": choice.message.role,
                            "content": choice.message.content
                        },
                        "finish_reason": choice.finish_reason
                    }
                    for choice in response.choices
                ],
                "usage": {
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                    "total_tokens": response.usage.total_tokens
                }
            }
            ret["response"][i] = {"raw": response_dict, "code": codes, "g_time": g_time}
            
        with open(os.path.join(outdir, "outputs.json"), "a") as f:
            f.write(json.dumps(ret, indent=4) + "\n")
            # ret["response"][i] = {"raw": response, "code": codes, "g_time": g_time}
        
        # with open(os.path.join(outdir, "outputs.json"), "a") as f:
            # f.write(json.dumps(ret, indent=4) + "\n")
