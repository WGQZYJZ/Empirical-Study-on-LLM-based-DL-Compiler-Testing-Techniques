'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.selu\ntorch.nn.functional.selu(input, inplace=False)\n'
import torch
input = torch.randn(5, 5)
output = torch.nn.functional.selu(input)
print(output)