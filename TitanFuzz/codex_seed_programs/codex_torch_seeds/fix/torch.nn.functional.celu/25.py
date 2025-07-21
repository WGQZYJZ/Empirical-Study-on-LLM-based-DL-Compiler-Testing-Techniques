'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.celu\ntorch.nn.functional.celu(input, alpha=1., inplace=False)\n'
import torch
input = torch.randn(3, 5)
print(input)
output = torch.nn.functional.celu(input)
print(output)