'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.prelu\ntorch.nn.functional.prelu(input, weight)\n'
import torch
input = torch.randn(1, 2)
weight = torch.randn(1, 2)
print(torch.nn.functional.prelu(input, weight))