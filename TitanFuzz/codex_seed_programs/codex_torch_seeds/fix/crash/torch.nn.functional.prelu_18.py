'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.prelu\ntorch.nn.functional.prelu(input, weight)\n'
import torch
input = torch.randn(2, 3)
weight = torch.randn(1, 3)
output = torch.nn.functional.prelu(input, weight)
print(output)