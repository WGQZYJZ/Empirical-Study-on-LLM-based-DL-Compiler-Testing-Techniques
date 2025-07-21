'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.selu\ntorch.nn.functional.selu(input, inplace=False)\n'
import torch
input_data = torch.randn(1, 3)
output = torch.nn.functional.selu(input_data)
print(output)
'\nTask 4: Call the API torch.selu\ntorch.selu(input, inplace=False)\n'
output = torch.selu(input_data)
print(output)