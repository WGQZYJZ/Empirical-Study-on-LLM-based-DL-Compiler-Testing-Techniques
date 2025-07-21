'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inference_mode\ntorch.inference_mode(mode=True)\n'
import torch
input_data = torch.randn(1, 1, 28, 28, requires_grad=True)
with torch.inference_mode():
    output = torch.nn.functional.relu(input_data)
print(output)